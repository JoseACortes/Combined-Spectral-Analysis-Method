import scipy.optimize as opt
import pandas as pd
import numpy as np

def linear_combination(x, *params):
    return sum(p * xi for p, xi in zip(params, x))

def least_squares(params, x, y):
    return np.average((y - linear_combination(x, *params))**2)

def least_squares_relative(params, x, y):
    residual = (y - linear_combination(x, *params))**2
    residual = np.where(y==0, 0, residual)
    _y = np.where(y==0, 1, y)
    return np.average(residual/_y**2)

def convex(params, x, y, alpha=1):
    residual = np.average((y - linear_combination(x, *params))**2)
    return residual + alpha*(1-np.sum(params))**2

def convex_relative(params, x, y, alpha=1):
    residual = (y - linear_combination(x, *params))**2
    residual = np.where(y==0, 0, residual)
    _y = np.where(y==0, 1, y)
    residual = np.average(residual/_y**2)

    return residual + alpha*(1-np.sum(params))**2

def correlation(params, x, y):
    predicted = linear_combination(x, *params)
    return 1-np.corrcoef(predicted, y)[0,1]

minimizers = {
    'least_squares': least_squares,
    'least_squares_relative': least_squares_relative,
    'convex': convex,
    'convex_relative': convex_relative,
    'correlation': correlation,
}

def find_linear_combination(x, y, minimizer='least_squares', initial_guess=None, normalize=False):
    if initial_guess is None:
        initial_guess = [1/x.shape[0]] * x.shape[0]
    to_minimize = minimizers[minimizer]
    if normalize:
        original_to_minimize = to_minimize
        to_minimize = lambda params, x, y: (original_to_minimize(params, x, y)/np.sum(original_to_minimize(params, x, y)))+(original_to_minimize(params, x, y))
    res = opt.minimize(to_minimize, x0=initial_guess, args=(x, y), bounds=([[0,1]]*x.shape[0]), tol=1e-16)
    return res.x

def Decompose(
    df,
    train_cols=None,
    normalize=False,
    minimizer='least_squares',
    initial_guess=None,
):
    # Calculate the linear combination of the columns
    x = np.array(df.values.T)
    if train_cols is None:
        train_cols = df.columns
    x_train = np.array(df[train_cols].values.T)

    coeffss = []
    for _x in x:
        coeffs = find_linear_combination(x_train, _x, minimizer=minimizer, initial_guess=initial_guess, normalize=normalize)
        coeffss.append(coeffs)
    coeffs = np.array(coeffss)
    # if normalize:
        
    #     coeffs = coeffs/np.sum(coeffs, axis=1)[:, np.newaxis]

    # Create a new DataFrame with the results
    fitting_df = pd.DataFrame(coeffs, index=df.columns, columns=train_cols)

    return fitting_df

def Analyze(
    df,
    bins=None,
    train_cols=None,
    true_c_concentrations=None,
    minimizer='least_squares',
    normalize=False,
    initial_guess=None,
    window = None,
):
    """
    Analyze the data frame and return a new data frame with the results.

    Parameters
    ----------
    df : pandas.DataFrame
        The input data frame.
    
    Returns
    -------
    pandas.DataFrame
        The new data frame with the results.
    """
    # Calculate the linear combination of the columns
    
    if bins is None:
        bins = np.arange(len(df))

    if window is None:
        window = [bins[0], bins[-1]]
    
    
    x = np.array(df.values.T)


    bin_index = np.array([i for i in range(len(bins)) if bins[i] >= window[0] and bins[i] <= window[1]])
    x = x[:, bin_index]

    if train_cols is None:
        x_train = x
        true_c_train = np.array(true_c_concentrations)
    elif isinstance(train_cols, list):
        # print("len train", len(train_cols))
        x_train = np.array(df[train_cols].values.T)[:, bin_index]
        train_cols_index = [df.columns.get_loc(col) for col in train_cols]
        true_c_train = np.array(true_c_concentrations)[train_cols_index]
    else:
        x_train = x[train_cols]
        true_c_train = np.array(true_c_concentrations)[train_cols]

    coeffss = []
    for _x in x:
        coeffs = find_linear_combination(
            x_train, 
            _x,
            minimizer=minimizer,
            initial_guess=initial_guess)
        coeffss.append(coeffs)
    coeffs = np.array(coeffss)
    if normalize:
        coeffs = coeffs/np.sum(coeffs, axis=1)[:, np.newaxis]
    determined_c = np.sum(coeffs*true_c_train, axis=1)

    fitting_df = pd.DataFrame(coeffs, index=df.columns, columns=df.columns[train_cols_index])
    predicted_df = pd.DataFrame(determined_c, index=df.columns, columns=['Carbon Portion'])

    return fitting_df, predicted_df

