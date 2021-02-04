# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:21:19 2020

Project: chemplot (Chemical Space Visualization)
Content: Descriptor operation methods

@author: murat cihan sorkun
"""

from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import math
import mordred
from mordred import Calculator, descriptors #Dont remove these imports
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

def get_mordred_descriptors(smiles_list):
    """
    Calculates the Mordred descriptors for given smiles list
    
    :param smiles_list: List of smiles
    :type smiles_list: list
    :returns: The calculated descriptors list for the given smiles
    :rtype: Dataframe
    """     
    
    return generate_mordred_descriptors(smiles_list, Chem.MolFromSmiles, 'SMILES')


def get_mordred_descriptors_from_inchi(inchi_list):
    """
    Calculates the Mordred descriptors for given InChi list
    
    :param inchi_list: List of InChi
    :type inchi_list: list
    :returns: The calculated descriptors list for the given smiles
    :rtype: Dataframe
    """     
    
    return generate_mordred_descriptors(inchi_list, Chem.MolFromInchi, 'InChi')

    
def generate_mordred_descriptors(encoding_list, encoding_function, encoding_name):
    """
    Calculates the Mordred descriptors for list of molecules encodings
    
    :param smiles_list: List of molecules encodings
    :type smiles_list: list
    :returns: The calculated descriptors list for the given molecules encodings
    :rtype: Dataframe
    """      
    
    calc = mordred.Calculator()  
        
    calc.register(mordred.AtomCount)        #16
    calc.register(mordred.RingCount)        #139
    calc.register(mordred.BondCount)        #9   
    calc.register(mordred.HydrogenBond)     #2  
    calc.register(mordred.CarbonTypes)      #10
    calc.register(mordred.SLogP)            #2
    calc.register(mordred.Constitutional)   #16    
    calc.register(mordred.TopoPSA)          #2
    calc.register(mordred.Weight)           #2
    calc.register(mordred.Polarizability)   #2
    calc.register(mordred.McGowanVolume)    #1
    
    name_list=[]
    for desc_name in calc.descriptors:
        name_list.append(str(desc_name))
        
    descriptors_list=[]   
    erroneous_encodings=[]
    encodings_none_descriptors=[]
    for encoding in encoding_list:
        mol=encoding_function(encoding)
        if mol is None:
            descriptors_list.append([None]*len(name_list))
            erroneous_encodings.append(encoding)
        else:
            mol=Chem.AddHs(mol)
            calculated_descriptors = calc(mol)
            for i in range(len(calculated_descriptors._values)):
                if math.isnan(calculated_descriptors._values[i]):
                    calculated_descriptors._values = [None]*len(name_list)
                    encodings_none_descriptors.append(encoding)
                    break
            descriptors_list.append(calculated_descriptors._values)      
    
    if len(erroneous_encodings)>0:
        print("The following erroneous {} have been found in the data:\n{}.\nThe erroneous {} will be removed from the data.".format(encoding_name, '\n'.join(map(str, erroneous_encodings)), encoding_name))

    if len(encodings_none_descriptors)>0:
        print("For the following {} not all descriptors can be computed:\n{}.\nThese {} will be removed from the data.".format(encoding_name, '\n'.join(map(str, encodings_none_descriptors)), encoding_name))
        
    df_descriptors=pd.DataFrame(descriptors_list,columns=name_list)
    df_descriptors = df_descriptors.select_dtypes(exclude=['object'])    
    return df_descriptors
    
def select_descriptors_lasso(df_descriptors,target_list, R_select=0.05, C_select=0.05, kind="R"):
    """
    Selects descriptors by LASSO 
    
    :param df_descriptors: descriptors of molecules 
    :type df_descriptors: Dataframe
    :param target_list: list of target values 
    :type target_list: list
    :param R_select: alpha value for Lasso 
    :type R_select: float
    :param C_select: C value for LogisticRegression 
    :type C_select: float
    :param kind: kind of target R->Regression C->Classification 
    :type kind: string
    :returns: The selected descriptors
    :rtype: Dataframe
    """      
    
    # Remove erroneous data
    df_descriptors = df_descriptors.assign(target=target_list.values)
    df_descriptors = df_descriptors.dropna(how='any')
    target_list = df_descriptors['target'].to_list()
    df_descriptors = df_descriptors.drop(columns=['target'])
    
    df_descriptors_scaled = StandardScaler().fit_transform(df_descriptors)
    
    if(kind=="C"):   
        model = LogisticRegression(C=C_select,penalty='l1', solver='liblinear',random_state=1).fit(df_descriptors_scaled, target_list)
    else:
        model = Lasso(alpha=R_select,max_iter=10000,random_state=1).fit(df_descriptors_scaled, target_list)
   
    
    selected = SelectFromModel(model, prefit=True)
    X_new_lasso = selected.transform(df_descriptors)
    # Get back the kept features as a DataFrame with dropped columns as all 0s
    selected_features = pd.DataFrame(selected.inverse_transform(X_new_lasso), index=df_descriptors.index, columns=df_descriptors.columns)
    # Dropped columns have values of all 0s, keep other columns 
    selected_columns_lasso = selected_features.columns[selected_features.var() != 0]    
    selected_data = df_descriptors[selected_columns_lasso] 
    
    return selected_data, target_list


def get_ecfp(smiles_list, target_list, radius=2, nBits=2048):
    """
    Calculates the ECFP fingerprint for given SMILES list
    
    :param smiles_list: List of SMILES
    :type smiles_list: list
    :param radius: The ECPF fingerprints radius.
    :type radius: int
    :param nBits: The number of bits of the fingerprint vector.
    :type nBits: int
    :returns: The calculated ECPF fingerprints for the given SMILES
    :rtype: Dataframe
    """  
    
    return generate_ecfp(smiles_list, Chem.MolFromSmiles, 'SMILES', target_list, radius=2, nBits=2048)


def get_ecfp_from_inchi(inchi_list, target_list, radius=2, nBits=2048):
    """
    Calculates the ECFP fingerprint for given InChi list
    
    :param inchi_list: List of InChi
    :type inchi_list: list
    :param radius: The ECPF fingerprints radius.
    :type radius: int
    :param nBits: The number of bits of the fingerprint vector.
    :type nBits: int
    :returns: The calculated ECPF fingerprints for the given InChi
    :rtype: Dataframe
    """  
    
    return generate_ecfp(inchi_list, Chem.MolFromInchi, 'InChi', target_list, radius=2, nBits=2048)


def generate_ecfp(encoding_list, encoding_function, encoding_name, target_list, radius=2, nBits=2048):
    """
    Calculates the ECFP fingerprint for given list of molecules encodings
    
    :param encoding_list: List of molecules encodings
    :type encoding_list: list
    :param encoding_function: Function used to extract the molecules from the encodings
    :type encoding_function: fun
    :param radius: The ECPF fingerprints radius.
    :type radius: int
    :param nBits: The number of bits of the fingerprint vector.
    :type nBits: int
    :returns: The calculated ECPF fingerprints for the given molecules encodings
    :rtype: Dataframe
    """  
    
    # Generate ECFP fingerprints
    ecfp_fingerprints=[]
    erroneous_encodings=[]
    for encoding in encoding_list:
        mol=encoding_function(encoding)
        if mol is None:
            ecfp_fingerprints.append([None]*nBits)
            erroneous_encodings.append(encoding)
        else:
            mol=Chem.AddHs(mol)
            list_bits_fingerprint = []
            list_bits_fingerprint[:0] = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits).ToBitString()
            ecfp_fingerprints.append(list_bits_fingerprint)  
    
    # Create dataframe of fingerprints
    df_ecfp_fingerprints = pd.DataFrame(data = ecfp_fingerprints, index = encoding_list)
    # Remove erroneous data
    if len(erroneous_encodings)>0:
        print("The following erroneous {} have been found in the data:\n{}.\nThe erroneous {} will be removed from the data.".format(encoding_name, '\n'.join(map(str, erroneous_encodings)), encoding_name))
    
    if len(target_list)>0:
        df_ecfp_fingerprints = df_ecfp_fingerprints.assign(target=target_list.values)
        
    df_ecfp_fingerprints = df_ecfp_fingerprints.dropna(how='any')
    
    if len(target_list)>0:
        target_list = df_ecfp_fingerprints['target'].to_list()
        df_ecfp_fingerprints = df_ecfp_fingerprints.drop(columns=['target'])
    
    # Remove bit columns with no variablity (all "0" or all "1")
    df_ecfp_fingerprints = df_ecfp_fingerprints.loc[:, (df_ecfp_fingerprints != 0).any(axis=0)]
    df_ecfp_fingerprints = df_ecfp_fingerprints.loc[:, (df_ecfp_fingerprints != 1).any(axis=0)]
    
    return df_ecfp_fingerprints, target_list