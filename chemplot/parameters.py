# Authors: Murat Cihan Sorkun <m.c.sorkun@differ.nl>, Dajt Mullaj <d.mullaj@differ.nl>
#
# License: BSD 3 clause
import math

######### Linear Models Functions #########
validator = lambda x: max(2, int(x))
predictor = lambda t, m, x: t+m*(x)
  
######### Perplexity Parameters #########
P_INTERCEPT_STRUCTURAL = -37.360438135651975
P_COEFFICIENT_STRUCTURAL = 8.578963490544542
def perplexity_structural(sample_length):
    prediction = predictor(P_INTERCEPT_STRUCTURAL,
                           P_COEFFICIENT_STRUCTURAL,
                           math.log(sample_length))
    prediction = validator(prediction)
    return prediction

P_INTERCEPT_TAILORED = -2.1210847692307038
P_COEFFICIENT_TAILORED = 0.9442229439797486
def perplexity_tailored(sample_length):
    prediction = predictor(P_INTERCEPT_TAILORED,
                           P_COEFFICIENT_TAILORED,
                           math.log(sample_length))**2
    prediction = validator(prediction)
    return prediction

P_INTERCEPT_STRUCTURAL_PCA = -4.897067968319856
P_COEFFICIENT_STRUCTURAL_PCA = 1.415629186176671
def perplexity_structural_pca(sample_length):
    prediction = predictor(P_INTERCEPT_STRUCTURAL_PCA,
                           P_COEFFICIENT_STRUCTURAL_PCA,
                           math.log(sample_length))**2
    prediction = validator(prediction)
    return prediction

######### N_neighbors Parameters #########
N_INTERCEPT_STRUCTURAL = -2.050415832404518
N_COEFFICIENT_STRUCTURAL = 0.617757208655686
def n_neighbors_structural(sample_length):
    prediction = math.exp(predictor(N_INTERCEPT_STRUCTURAL,
                           N_COEFFICIENT_STRUCTURAL,
                           math.log(sample_length)))
    prediction = validator(prediction)
    return prediction

N_INTERCEPT_TAILORED = -12.268898898548853
N_COEFFICIENT_TAILORED = 3.516519699104097
def n_neighbors_tailored(sample_length):
    prediction = predictor(N_INTERCEPT_TAILORED,
                           N_COEFFICIENT_TAILORED,
                           math.log(sample_length))
    prediction = validator(prediction)
    return prediction

N_INTERCEPT_STRUCTURAL_PCA = -1.267586478241988
N_COEFFICIENT_STRUCTURAL_PCA = 0.49349366477471657
def n_neighbors_structural_pca(sample_length):
    prediction = math.exp(predictor(N_INTERCEPT_STRUCTURAL_PCA,
                           N_COEFFICIENT_STRUCTURAL_PCA,
                           math.log(sample_length)))
    prediction = validator(prediction)
    return prediction

######### Min_dist Parameters #########
MIN_DIST_STRUCTURAL = 0.485
MIN_DIST_TAILORED = 0.47
MIN_DIST_STRUCTURAL_PCA = 0.36

######### Tooltips Parameters #########
TOOLTIPS_TARGET = """
        <div>
            <div>
                <img
                    src="@imgs" height="130" alt="@imgs" width="200"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 15px;">Target Value:</span>
                <span style="font-size: 13px; color: #696;">@target</span>
            </div>
        </div>
    """
    
TOOLTIPS_NO_TARGET = """
        <div>
            <div>
                <img
                    src="@imgs" height="130" alt="@imgs" width="200"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
        </div>
    """