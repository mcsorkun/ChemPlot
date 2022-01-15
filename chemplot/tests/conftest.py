"""
Session Testing Fixtures

To share the data accross the different tests.
"""
import pytest
import pandas as pd
import pkg_resources
from chemplot import Plotter, load_data
from pathlib import Path

THIS_DIR = Path(__file__).parent

@pytest.fixture(scope="session")
def logs():
    return load_data('R_1291_LOGS').head(20)

@pytest.fixture(scope="session")
def bbbp():
    return load_data('C_2039_BBBP_2').head(100)

@pytest.fixture(scope="session")
def sampl():
    return load_data('R_642_SAMPL').head(20)

@pytest.fixture(scope="class")
def logs_data(request, logs):
    request.cls.data_LOGS = logs
    
@pytest.fixture(scope="class")
def bbbp_data(request, bbbp):
    request.cls.data_BBBP = bbbp
    
@pytest.fixture(scope="class")
def error(request):
    file_BBBP_erroneous_smiles = pkg_resources.resource_stream('chemplot.tests', 'test_data/C_2039_BBBP_2_erroneous_smiles.csv')
    request.cls.data_BBBP_erroneous_smiles = pd.read_csv(file_BBBP_erroneous_smiles) 
    file_CLINTOX_2_erroneous_smiles = pkg_resources.resource_stream('chemplot.tests', 'test_data/C_1484_CLINTOX_2_erroneous_smiles.csv')
    request.cls.data_CLINTOX_2_erroneous_smiles = pd.read_csv(file_CLINTOX_2_erroneous_smiles) 
    request.cls.list_BBBP_erroneous_smiles = ['C12CCN(CC1)Cc1cccc(c1)OCCCNC(=O)CC12', 'C(Cl)Cl1', 'Nc1nc(c(N@)n1)c2c=ccc(Cl)c2Cl', 'non_smile', 'non_smile', 'non_smile', 
                                          'non_smile', 'non_smile', 'CNc1CCCN1c2ccccc2CCc3ccccc13', 'non_smile', '[O-]][N+](=O)c1ccc2NC(=O)CN=C(c3ccccc3)c2c1', 'non_smile', 
                                          'CC(Ccccccc1)NO', 'non_smile', 'non_smile', 'non_smile', 'C1=C2C=CC2=C1C3N(CC2)CCNC3', 'C1=C(CC)SC2=C1C(=NCC(N2C)=O)C3=CC=CC=C3Cl12', 
                                          'CC(O)C31(O)CCC4C2CCC1=CC(=O)C=CC1(C)C2C(O)CC34C', 'C1=C-(OC)C(=CC2=C1C(=NN=C(C2)C)C3=CC=CC(=C3)Cl)OC', 'CN(C)C[=O]COC2c1ccccc1CCc3ccccc23', 
                                          'non_smile', '[[C@]4([C@@]3([C@H]([C@H]2[C@]([C@@]1(C(=CC(=O)C=C1)CC2)C)(F)[C@H](C3)O)C[C@@H]4C)C)(OC(CC)=O)C(CCl)=O', 'C1=CC=CC=C1CN2C(CC((C2)CN)=O', 
                                          'C1=C(OC)C=CC3=C1N(C2=C(C=CC=C2)S3)CC(CN4CCC(O)CC4))C', '[[C@@H]1(C[C@H]3[C@H]2[C@@]1(O[C@H](O[C@H]2OC)[C@@H]3C)CN4CCCCC4)O', 'non_smile']
    request.cls.list_CLINTOX_2_erroneous_smiles = ['[NH4][Pt]([NH4])(Cl)Cl', 'c1ccc(cc1)n2c(=O)c(c(=O)n2c3ccccc3)CCS(=O)c4ccccc4', 'Cc1cc2c(cc1C)N3C=N2[Co+]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)[O-])C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)O', 
                                               'Cc1cc2c(cc1C)N3C=N2[Co]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)O)C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)C#N', 
                                               'CCCCc1c(=O)n(n(c1=O)c2ccc(cc2)O)c3ccccc3', 'CCCCc1c(=O)n(n(c1=O)c2ccccc2)c3ccccc3']
    request.cls.list_BBBP_erroneous_descriptors = ['[N+](=[N-])=O']
    request.cls.list_CLINTOX_2_erroneous_descriptors = ['*C(=O)[C@H](CCCCNC(=O)OCCOC)NC(=O)OCCOC', '[N+](=O)([O-])[O-]', '[N]=O', '[O-][99Tc](=O)(=O)=O', '[O-]P(=O)([O-])F', 
                                                    '[O-]S(=O)(=O)[O-]', '[O-]S(=O)(=S)[O-]', '[Se]', 'C#N', 'C(#N)[Fe-2](C#N)(C#N)(C#N)(C#N)N=O', 'C1CC(C1)(C(=O)O)C(=O)O.N.N.[Pt]', 
                                                    'C1CC2(C1)C(=O)O[Pt]OC2=O', 'CCP(=[Au]S[C@H]1[C@@H]([C@H]([C@@H]([C@H](O1)COC(=O)C)OC(=O)C)OC(=O)C)OC(=O)C)(CC)CC', 'Cl[201Tl]', 'Cl[Cr](Cl)Cl', 
                                                    'Cl[Cu]Cl', 'Cl[Mn]Cl', 'Cl[Zn]Cl', 'II', 'N(=O)[O-]', 'O1[As]2O[As]1O2', 'O[32P](=O)([O-])[O-]', 'O=[Al]O[Al]=O', 'O[Si](=O)O', 'O=[Ti]=O', 
                                                    'O=[Zn]', 'OCl(=O)(=O)=O', 'S=[Se]=S']
    
@pytest.fixture(scope="class")
def logs_plotter(request, logs):
    request.cls.plotter_tailored_LOGS = Plotter.from_smiles(logs["smiles"], target=logs["target"], target_type="R")
    request.cls.plotter_no_target_LOGS = Plotter.from_smiles(logs["smiles"], target_type="R", sim_type="structural")

@pytest.fixture(scope="class")
def logs_structural(request, logs):
    request.cls.plotter_structural_LOGS = Plotter.from_smiles(logs["smiles"], target=logs["target"], target_type="R", sim_type="structural")

@pytest.fixture(scope="class")
def visualize_data(request, logs, bbbp, sampl):
    request.cls.plotter_pca_LOGS = Plotter.from_smiles(logs["smiles"], target=logs["target"], target_type="R", sim_type="tailored")
    request.cls.plotter_pca_BBBP = Plotter.from_smiles(bbbp["smiles"], target=bbbp["target"], target_type="C", sim_type="tailored")
    request.cls.plotter_pca_LOGS.pca()
    request.cls.plotter_pca_BBBP.pca()
    
    request.cls.plotter_sampl = Plotter.from_smiles(sampl["smiles"], target=sampl["target"], target_type="R", sim_type="tailored")
