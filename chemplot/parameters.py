# Authors: Murat Cihan Sorkun <mcsorkun@gmail.com>, Dajt Mullaj <dajt.mullai@gmail.com>
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
    
TOOLTIPS_CLUSTER = """
        <div>
            <div>
                <img
                    src="@imgs" height="130" alt="@imgs" width="200"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 13px;">@clusters</span>
            </div>
        </div>
    """

######### Sample Dataset
SAMPLE_DATASETS = {
    'C_1478_CLINTOX_2' : ['C_1478_CLINTOX_2.csv', 'Clintox', 'C_1478_CLINTOX_2'],
    'C_1513_BACE_2' : ['C_1513_BACE_2.csv', 'C_1513_BACE_2'],
    'C_2039_BBBP_2' : ['C_2039_BBBP_2.csv', 'BBBP', 'C_2039_BBBP_2'],
    'C_41127_HIV_3' : ['C_41127_HIV_3.csv', 'HIV', 'C_41127_HIV_3'],
    'R_642_SAMPL' : ['R_642_SAMPL.csv', 'SAMPL', 'R_642_SAMPL'],
    'R_1513_BACE' : ['R_1513_BACE.csv', 'BACE', 'R_1513_BACE'],
    'R_4200_LOGP' : ['R_4200_LOGP.csv', 'LOGP', 'R_4200_LOGP'],
    'R_1291_LOGS' : ['R_1291_LOGS.csv', 'LOGS', 'R_1291_LOGS'],
    'R_9982_AQSOLDB' : ['R_9982_AQSOLDB.csv', 'AQSOLDB', 'R_9982_AQSOLDB']
}

INFO_DATASET = """\
============ Sample Datasets ============
- Clintox (Toxicity):
    type: C
    size: 1478
    name: CLINTOX
    classes: 2
- BACE (Inhibitor):
    type: C
    size: 1513
    name: BACE
    classes: 2
- BBBP (Blood-brain barrier penetration):
    type: C
    size: 2039
    name: BBBP
    classes: 2
- HIV:
    type: C
    size: 41127
    name: HIV
    classes: 3
- SAMPL (Hydration free energy):
    type: R
    size: 642
    name: SAMPL
- BACE (Binding affinity):
    type: R
    size: 1513
    name: BACE
- LOGP (Lipophilicity):
    type: R
    size: 4200
    name: LOGP
- LOGS (Aqueous Solubility):
    type: R
    size: 1291
    name: LOGS
- AQSOLDB (Aqueous Solubility):
    type: R
    size: 9982
    name: AQSOLDB
=========================================\
"""