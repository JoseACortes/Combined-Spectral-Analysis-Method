# Revisons

- issue
= Possible Response
> Completed Response

## MCNP

- The MCNP simulation model should be explained in detail, including all aspects such as the detectors used and neutron energy. The accuracy of the model should be proven with reference to the literature.
= refer to galina and aleksandr

- its methodological gain is limited and in its current form the paper reads more as a collection of different simulation results than a conclusive study.
= Include more comparison between methods

- The authors try to take into consideration a many different variables, however, that covers only a fraction of potential environmental parameters - without comparisons to measurements it is not clear how certain and relevant the current parameter space is.
- The authors have gathered a large number of spectra in the past. It is not clear to the reviewer why not even a single one is shown as a comparison or used as a validation. This has a second shortcoming beyond the omission: The results of the authors show that within there rather narrow set of parameters the combined methodology as presented here seems to be advantageous. Given that, looking more closely at the simulations, there are a large amount of uncertainties and systematics the methodology therefore might lose its benefit. The authors themselves acknowledge that the reconstructed spectrum does not exactly match the observed spectrum, that the final coefficients are close to the initial values and that the method exhibits greater variability than peak fitting for similar true C contents, precisely due to the influence of O and Si. This raises the concern that confronted with actual data, it might simply not work out as straight forward as presented.
- The description of the training/test split seems to be misleading, as the text suggests that calibration is performed on the test set. Furthermore, all the simulations are from the same family of simmulations, so it seems that there would not be non-deterministic parameter drifts or variations in the data set.
= Include tests on real data?

- The introduction of the manuscript lacks to describe the state of the art in the necessary way. Neither works of similar groups are referenced (Neutron Gamma analysis in soil sciences or pulsed neutron neutron or neutron gamma, mostly with respect to soil water though) nor the own history with respect to the instrument is detailed.
= section on state of the art

- What is actually the goal of this device? The actual intended use case. This instrument is certainly costly. Deriving a useful measure of SoC requires the knowledge of the soil bulk density - if there is no way to obtain this otherwise, it needs soil sampling and oven drying. SoC develops on the scale of months and years, so there is definitely no need to take snapshots. SoC is laterally rather homogeneous, but vertically not. So one can easily have several percent in the upper 10 cm and below practically nothing. Hence this instrument seems to provide a spatial resolution (where not needed) with no depth resolution (where required).
= ?

- precisely the practical parameters that would be important for the claimed application are missing: There is no statement regarding penetration depth, no quantitative information on measurement duration (or number of pulses), and no realistic experimental accuracy or uncertainty analysis.
= refer to Auburn?

- Methodologically, the manuscript lacks balance in clarity in several places. The curve-fitting section is at the level of a generic textbook description, it is not clearly specified which optimizer was actually used, whether bounds were set, how initial values were chosen and which energy windows were fitted. Furthermore, the peak fit is kept potentially very simple a Gaussian peak plus baseline, so one would rather also like to know how appropriate that assumption is.
= expand on methodology
> added optimizer
= multi peak management
> bounds and starting parameters

- The endmember fitting also is methodologically unclear. Although a linear mixture model with normalized components is initially introduced, this is subsequently reformulated into a linear combination of reference spectra without clearly specifying whether physical constraints such as non-negativity or sum-to-one are actually set.
> constraints
= explain convexity

- In terms of content, the authors demonstrate that O and Si signals interfere with the C range and that additional O/Si features can improve predictions in the synthetic dataset. At the same time, although water content is systematically varied from 0 to 20 wt% and water primarily contributes O in this model, the influence of soil water is not analyzed as a separate factor, after all this seems to be the quantity which varies the most in real-world scenarios. It is therefore unclear how suitable the approach would actually be against relevant systematic errors that are unavoidable in the field.
= ?

- equations are part of the text body, therefore they follow the usual rules of interpunctuation.
= Fix this? is this putting periods in the equation?

- partially awkward or wrong phrases, like describing conventional methods as "traditional", the materials in the simulation model as "architecture" or the repeated usage of "edgemember" instead of "endmember".
> changed "traditional" to conventional
> changed "edgemember" to "endmember"

- usually one would, where appropriate, format all y-axis to counts per 1e6 neutrons.
= is this correct?

- in an author-blind peer-review, as it is potentially intended here, the acknowledgements or author contribution statement should be removed.
= Remove author contrib

- many of the figure labels and text elements tend to be too small (if reduced in size due to the two-column layout of NIMA).
= change text size

- Title: Should be rephrased. Without soil density one cannot determine the elemental content but only ratios. Secondly, the manuscript mainly addresses carbon and not the entire or a large part of the elemental content.
= change to "carbon ratios?"

- Stating that SoC analysis from soil samples is time-consuming, expensive and requires laboratory analysis is a potentially misplaced statement considering the fact that the authors bring a small laboratory into the field (vs. practically no specific tools needed to take samples, except the cylinders and a scale) and that this small laboratory costs at least around half a million dollars, not taking into account that the neutron generator also has a limited lifespan of 50h to 100h. The reviewer is not convinced that the statement of the authors is fully developed against obvious objections.
= refer to Tobert

- The section on 'Multivariate Calibration Using Singular Value Decomposition' consists mostly of textbook material and should be significantly streamlined. The real contribution is not SVD itself, but the combination of features, if so. Instead, the pseudoinverse and standard decomposition are explained in detail, whereas the relevant questions like feature scaling, collinearity, regularization or the implementation of the bias term are unaddressed.
= address relevant questions

- MSE is defined for carbon prediction, but the scale of the target variable seems to be unclear, which makes the numbers in Table 5 difficult to interpret.
= Does this mean add a baseline?


NEW SUBSECTIONS:

## State of the art

Single feature approaches use minimal amounts of features and data points neccessarry 

Peak fitting relies on calibration

endmember fitting does not rely on callibration but instead derives the concentration from 

In contrast, deep learning methods take thousands of sample spectra to approach accurraccy.

This is a multimodal approach to combine the features of both into a single prediction.

## Double vs Single Peak

comparison of the results with different baselines

## ls vs ls-Convex results

- In taking single-variable callibration, convexity enhances the results
- With all three variables (Carbon, Silicon, Oxygen), non-convex slimly outperforms convex methods.

## multivariate 