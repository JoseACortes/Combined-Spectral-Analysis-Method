import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots
from tabulate import tabulate
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

min_width = 30 / 25.4
single_col_width = 90 / 25.4
one_half_col_width = 140 / 25.4
double_col_width = 190 / 25.4

plt.style.use('science')
plt.rcParams['figure.figsize'] = [3.54, 2.36]
dpi = 300
plt.rcParams['savefig.dpi'] = dpi
plt.rcParams['figure.dpi'] = dpi

sns.color_palette("colorblind")
# set color palette
palette = sns.color_palette("colorblind")

analysis_results = pd.read_pickle('analysis_results.pkl')
detector_readings = pd.read_csv('../Simulation/DetectorReadings.csv', index_col=0)
sims = pd.read_csv('../Simulation/sims.csv', index_col=1)
soilinfos = pd.read_json('../Simulation/soilinfos.json')
sims['element_mat'] = soilinfos['element_mat'].apply(lambda x: x[0])
figure_folder = '../Cortes2026/Figures/Analysis/'