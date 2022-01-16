"""
Performance Test for ChemPlot methods.

Output will be a .txt file containing the metadata about performance (machine
processor, RAM...) and a .csv file containing a report about performance.
"""

from chemplot import Plotter, load_data
from pathlib import Path

import platform
import time
import pandas as pd 
import gc
import datetime

THIS_DIR = Path(__file__).parent

class PerformanceTest(object):
    
    def __init__(self):
        file_LOGS = 'R_1291_LOGS.csv'
        file_LOGP = 'R_4200_LOGP.csv'
        file_BACE = 'R_1513_BACE.csv'
        file_SAMPL = 'R_642_SAMPL.csv'
        file_AQSOLDB = 'R_9982_AQSOLDB.csv'
        file_BBBP = 'C_2039_BBBP_2.csv'
        file_HIV_3 = 'C_41127_HIV_3.csv'
        file_BACE_2 = 'C_1513_BACE_2.csv'
        file_CLINTOX_2 = 'C_1478_CLINTOX_2.csv'
        
        self.data_LOGS = load_data(file_LOGS) 
        self.data_LOGP = load_data(file_LOGP)
        self.data_BACE = load_data(file_BACE)
        self.data_SAMPL = load_data(file_SAMPL) 
        self.data_AQSOLDB = load_data(file_AQSOLDB) 
        self.data_BBBP = load_data(file_BBBP) 
        self.data_HIV_3 = load_data(file_HIV_3) 
        self.data_BACE_2 = load_data(file_BACE_2)
        self.data_CLINTOX_2 = load_data(file_CLINTOX_2)
        
        self.df_perf_test = pd.DataFrame(columns=['name', 'data_samples', 'target_type', 'sym_type','execution_time_from_smiles','execution_time_pca','execution_time_tsne','execution_time_umap'])
        
    def fun_performace_test(self, data, name, data_samples, target_type, sim_type, index):
        t0 = time.time()
        cp = Plotter.from_smiles(data["smiles"], target=data["target"], target_type=target_type, sim_type=sim_type)
        t1 = time.time()
        cp.pca()
        t2 = time.time()
        cp.tsne()
        t3 = time.time()
        cp.umap()
        t4 = time.time()
        self.df_perf_test.loc[index] = [name, data_samples, target_type, sim_type, "%.2f" % (t1-t0), "%.2f" % (t2-t1), "%.2f" % (t3-t2), "%.2f" % (t4-t3)]
        
    def run(self, file_name): 
        # For R data sets
        self.fun_performace_test(self.data_LOGS, 'R_1291_LOGS', '1291', 'R', 'tailored', 0)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored LOGS (1291)')
        gc.collect()
        self.fun_performace_test(self.data_LOGS, 'R_1291_LOGS', '1291', 'R', 'structural', 1)
        print('CHEMPLOT - PerformanceTest - Running functions with structural LOGS (1291)')
        gc.collect()
        self.fun_performace_test(self.data_LOGP, 'R_4200_LOGP', '4200', 'R', 'tailored', 2)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored LOGP (4200)')
        gc.collect()
        self.fun_performace_test(self.data_LOGP, 'R_4200_LOGP', '4200', 'R', 'structural', 3)
        print('CHEMPLOT - PerformanceTest - Running functions with structural LOGP (4200)')
        gc.collect()
        self.fun_performace_test(self.data_BACE, 'R_1513_BACE', '1513', 'R', 'tailored', 4)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored BACE (1513)')
        gc.collect()
        self.fun_performace_test(self.data_BACE, 'R_1513_BACE', '1513', 'R', 'structural', 5)
        print('CHEMPLOT - PerformanceTest - Running functions with structural BACE (1513)')
        gc.collect()
        self.fun_performace_test(self.data_SAMPL, 'R_642_SAMPL', '642', 'R', 'tailored', 6)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored SAMPL (642)')
        gc.collect()
        self.fun_performace_test(self.data_SAMPL, 'R_642_SAMPL', '642', 'R', 'structural', 7)
        print('CHEMPLOT - PerformanceTest - Running functions with structural SAMPL (642)')
        gc.collect()
        self.fun_performace_test(self.data_AQSOLDB, 'R_9982_AQSOLDB', '9982', 'R', 'tailored', 8)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored AQSOLDB (9982)')
        gc.collect()
        self.fun_performace_test(self.data_AQSOLDB, 'R_9982_AQSOLDB', '9982', 'R', 'structural', 9)
        print('CHEMPLOT - PerformanceTest - Running functions with structural AQSOLDB (9982)')
        gc.collect()
        # For C data sets
        self.fun_performace_test(self.data_BBBP, 'C_2039_BBBP_2', '2039', 'C', 'tailored', 10)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored BBBP (2039)')
        gc.collect()
        self.fun_performace_test(self.data_BBBP, 'C_2039_BBBP_2', '2039', 'C', 'structural', 11)
        print('CHEMPLOT - PerformanceTest - Running functions with structural BBBP (2039)')
        gc.collect()
        self.fun_performace_test(self.data_HIV_3, 'C_41127_HIV_3', '41127', 'C', 'tailored', 12)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored HIV (41127)')
        gc.collect()
        self.fun_performace_test(self.data_HIV_3, 'C_41127_HIV_3', '41127', 'C', 'structural', 13)
        print('CHEMPLOT - PerformanceTest - Running functions with structural HIV (41127)')
        gc.collect()
        self.fun_performace_test(self.data_BACE_2, 'C_1513_BACE_2', '1513', 'C', 'tailored', 14)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored BACE (1513)')
        gc.collect()
        self.fun_performace_test(self.data_BACE_2, 'C_1513_BACE_2', '1513', 'C', 'structural', 15)
        print('CHEMPLOT - PerformanceTest - Running functions with structural BACE (1513)')
        gc.collect()
        self.fun_performace_test(self.data_CLINTOX_2, 'C_1478_CLINTOX_2', '1478', 'C', 'tailored', 16)
        print('CHEMPLOT - PerformanceTest - Running functions with tailored CLINTOX (1478)')
        gc.collect()
        self.fun_performace_test(self.data_CLINTOX_2, 'C_1478_CLINTOX_2', '1478', 'C', 'structural', 17)
        print('CHEMPLOT - PerformanceTest - Running functions with structural CLINTOX (1478)')
        gc.collect()
        
        self.df_perf_test.to_csv(file_name + '.csv')  
    
    
if __name__ == '__main__':
    date = datetime.datetime.now()
    date_test =  str(date.day) + "_" + str(date.month) + "_" + str(date.year)
    file_name = "performance_test_" + date_test
    
    # Create metadata
    py_version = f"Python version: {platform.python_version()}\n"
    cpu_version = f"Processor version: {platform.processor()}\n"
    os_version = f"Operating System version: {platform.platform()}"
    metadata = open(file_name + '_metadata.txt',"w") 
    metadata.writelines([py_version, cpu_version, os_version])  
    metadata.close()
    
    # Run performance tests
    PerformanceTest().run(file_name)
