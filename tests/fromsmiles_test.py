import unittest
from unittest.mock import patch
import pytest

from chemplot import Plotter
from io import StringIO

@pytest.mark.usefixtures("logs_data")
class TestFromSmilesR(unittest.TestCase):

    def test_target_type_assigned_tailored(self):
        """
        1. Test checks if target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="tailored")
        self.assertEqual(cp._Plotter__target_type, "R")
        
    def test_sym_type_assigned_tailored(self):
        """
        2. Test checks if sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="tailored")
        self.assertEqual(cp._Plotter__sim_type, "tailored")

    def test_df_descriptors_created_tailored(self):
        """
        3. Test checks if df_descriptors is created
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="tailored")
        self.assertNotIsInstance(cp._Plotter__df_descriptors, type(None))
        
    def test_df_descriptors_non_empty_tailored(self):
        """
        4. Test checks if df_descriptors is non empty
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="tailored")
        self.assertTrue(len(cp._Plotter__df_descriptors) > 0)
        
    def test_target_sent_tailored(self):
        """
        5. Test checks if target is sent from user
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R", sim_type="tailored")
            
        self.assertTrue('Target values missing' in str(context.exception))
        
    def test_target_type_assigned_structural(self):
        """
        6. Test checks if target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="structural")
        self.assertEqual(cp._Plotter__target_type, "R")

    def test_sym_type_assigned_structural(self):
        """
        7. Test checks if sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="structural")
        self.assertEqual(cp._Plotter__sim_type, "structural")

    def test_df_descriptors_created_structural(self):
        """
        8. Test checks if df_descriptors is created
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="structural")
        self.assertNotIsInstance(cp._Plotter__df_descriptors, type(None))
        
    def test_df_descriptors_non_empty_structural(self):
        """
        9. Test checks if df_descriptors is non empty
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="structural")
        self.assertTrue(len(cp._Plotter__df_descriptors) > 0)
        
    def test_target_sent_structural(self):
        """
        10. Test checks if target is sent from user
        """
        try:
            Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R", sim_type="structural")
        except Exception:
            self.fail("from_smiles(self.data_LOGS[\"smiles\"], target_type=\"R\", sim_type=\"structural\") raised Exception")
   
    def test_default_sym_type_assigned_tail(self):
        """
        11. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R")
        self.assertEqual(cp._Plotter__sim_type, "tailored")
  
    @patch('builtins.print')
    def test_INFO_sym_type_tail(self, mock_print):
        """
        12. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R")
        mock_print.assert_called_with('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because a target list has been provided \'tailored\' as been selected as sym_type.')
    
    def test_default_sym_type_assigned_struc(self):
        """
        13. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R")
        self.assertEqual(cp._Plotter__sim_type, "structural")
    
    @patch('builtins.print')
    def test_INFO_sym_type_struc(self, mock_print):
        """
        14. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R")
        mock_print.assert_called_with('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because no target list has been provided \'structural\' as been selected as sym_type.')
    
    def test_default_sym_type_assigned_with_anytext_tail(self):
        """
        15. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="anytext")
        self.assertEqual(cp._Plotter__sim_type, "tailored")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_INFO_sym_type_with_anytext_tail(self, mock_stdout):
        """
        16. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], target_type="R", sim_type="anytext")
        assert ('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because a target list has been provided \'tailored\' as been selected as sym_type.') in mock_stdout.getvalue()
    
    def test_default_sym_type_assigned_with_anytext_struc(self):
        """
        17. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R", sim_type="anytext")
        self.assertEqual(cp._Plotter__sim_type, "structural")
    
    @patch('builtins.print')
    def test_INFO_sym_type_with_anytext_struc(self, mock_print):
        """
        18. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_LOGS["smiles"], target_type="R", sim_type="anytext")
        mock_print.assert_called_with('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because no target list has been provided \'structural\' as been selected as sym_type.') 
    
    def test_default_target_type_assigned(self):
        """
        19. Test checks if default target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], sim_type="tailored")
        self.assertEqual(cp._Plotter__target_type, "R")
    
    @patch('builtins.print')
    def test_INFO_default_target_type_assigned(self, mock_print):
        """
        20. Test checks if user is informed about target_type
        """
        Plotter.from_smiles(self.data_LOGS["smiles"], target=self.data_LOGS["target"], sim_type="tailored")
        mock_print.assert_called_with('target_type indicates if the target is a continuous variable or a class label.\n'+
                          'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                          'From analysis of the target, R has been selected for target_type.') 
        

@pytest.mark.usefixtures("bbbp_data")
class TestFromSmilesC(unittest.TestCase):  
    
    def test_target_type_assigned_tailored(self):
        """
        21. Test checks if target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="tailored")
        self.assertEqual(cp._Plotter__target_type, "C")
        
    def test_sym_type_assigned_tailored(self):
        """
        22. Test checks if sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="tailored")
        self.assertEqual(cp._Plotter__sim_type, "tailored")

    def test_df_descriptors_created_tailored(self):
        """
        23. Test checks if df_descriptors is created
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="tailored")
        self.assertNotIsInstance(cp._Plotter__df_descriptors, type(None))
        
    def test_df_descriptors_non_empty_tailored(self):
        """
        24. Test checks if df_descriptors is non empty
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="tailored")
        self.assertTrue(len(cp._Plotter__df_descriptors) > 0)
        
    def test_target_sent_tailored(self):
        """
        25. Test checks if target is sent from user
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C", sim_type="tailored")
            
        self.assertTrue('Target values missing' in str(context.exception))
        
    def test_target_type_assigned_structural(self):
        """
        26. Test checks if target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="structural")
        self.assertEqual(cp._Plotter__target_type, "C")

    def test_sym_type_assigned_structural(self):
        """
        27. Test checks if sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="structural")
        self.assertEqual(cp._Plotter__sim_type, "structural")

    def test_df_descriptors_created_structural(self):
        """
        28. Test checks if df_descriptors is created
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="structural")
        self.assertNotIsInstance(cp._Plotter__df_descriptors, type(None))
        
    def test_df_descriptors_non_empty_structural(self):
        """
        29. Test checks if df_descriptors is non empty
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="structural")
        self.assertTrue(len(cp._Plotter__df_descriptors) > 0)
        
    def test_target_sent_structural(self):
        """
        30. Test checks if target is sent from user
        """
        try:
            Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C", sim_type="structural")
        except Exception:
            self.fail("from_smiles(self.data_LOGS[\"smiles\"], target_type=\"R\", sim_type=\"structural\") raised Exception")
   
    def test_default_sym_type_assigned_tail(self):
        """
        31. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C")
        self.assertEqual(cp._Plotter__sim_type, "tailored")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_INFO_sym_type_tail(self, mock_stdout):
        """
        32. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C")
        assert str('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because a target list has been provided \'tailored\' as been selected as sym_type.') in mock_stdout.getvalue()
    
    def test_default_sym_type_assigned_struc(self):
        """
        33. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C")
        self.assertEqual(cp._Plotter__sim_type, "structural")
    
    @patch('builtins.print')
    def test_INFO_sym_type_struc(self, mock_print):
        """
        34. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C")
        mock_print.assert_called_with('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because no target list has been provided \'structural\' as been selected as sym_type.')
    
    def test_default_sym_type_assigned_with_anytext_tail(self):
        """
        35. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="anytext")
        self.assertEqual(cp._Plotter__sim_type, "tailored")
      
    @patch('sys.stdout', new_callable=StringIO)
    def test_INFO_sym_type_with_anytext_tail(self, mock_stdout):
        """
        36. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="C", sim_type="anytext")
        assert str('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because a target list has been provided \'tailored\' as been selected as sym_type.') in mock_stdout.getvalue()
    
    def test_default_sym_type_assigned_with_anytext_struc(self):
        """
        37. Test checks if default sim_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C", sim_type="anytext")
        self.assertEqual(cp._Plotter__sim_type, "structural")
      
    @patch('builtins.print')
    def test_INFO_sym_type_with_anytext_struc(self, mock_print):
        """
        38. Test checks if user is informed about sim_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target_type="C", sim_type="anytext")
        mock_print.assert_called_with('sim_type indicates the similarity type by which the plots are constructed.\n' +
                         'The supported similarity types are structural and tailored.\n' +
                         'Because no target list has been provided \'structural\' as been selected as sym_type.') 
        
    @patch('builtins.print')
    def test_INFO_target_type_correct(self, mock_print):
        """
        39. Test checks if user is informed about target_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], target_type="R", sim_type="structural")
        mock_print.assert_called_with('Input received is \'R\' for target values that seem not continuous.')
      
    def test_default_target_type_assigned(self):
        """
        40. Test checks if default target_type is assigned
        """
        cp = Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], sim_type="tailored")
        self.assertEqual(cp._Plotter__target_type, "C")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_INFO_default_target_type_assigned(self, mock_stdout):
        """
        41. Test checks if user is informed about target_type
        """
        Plotter.from_smiles(self.data_BBBP["smiles"], target=self.data_BBBP["target"], sim_type="tailored")
        assert str('target_type indicates if the target is a continuous variable or a class label.\n'+
                          'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                          'From analysis of the target, C has been selected for target_type.') in mock_stdout.getvalue()


@pytest.mark.usefixtures("error")
class TestFromSmilesErroneusSMILES(unittest.TestCase):
    
    def test_BBBP_erroneous_data_removed_tailored(self):
        """
        42. Test if the erroneous data is removed from the calculated descriptors
        """
        cp = Plotter.from_smiles(self.data_BBBP_erroneous_smiles["smiles"], target=self.data_BBBP_erroneous_smiles["target"], target_type="C", sim_type="tailored")
        self.assertEqual(len(cp._Plotter__df_descriptors.index), len(self.data_BBBP_erroneous_smiles.index) - (len(self.list_BBBP_erroneous_smiles) + len(self.list_BBBP_erroneous_descriptors)))
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_BBBP_erroneous_data_INFO_tailored(self, mock_stdout):
        """
        43. Test if the user is informed about which is the erroneous data and that it will be removed from the dataset
        """
        Plotter.from_smiles(self.data_BBBP_erroneous_smiles["smiles"], target=self.data_BBBP_erroneous_smiles["target"], target_type="C", sim_type="tailored")
        assert str('The following erroneous SMILES have been found in the data:\nC12CCN(CC1)Cc1cccc(c1)OCCCNC(=O)CC12\nC(Cl)Cl1\nNc1nc(c(N@)n1)c2c=ccc(Cl)c2Cl\nnon_smile\n'+
                      'non_smile\nnon_smile\nnon_smile\nnon_smile\nCNc1CCCN1c2ccccc2CCc3ccccc13\nnon_smile\n[O-]][N+](=O)c1ccc2NC(=O)CN=C(c3ccccc3)c2c1\nnon_smile\nCC(Ccccccc1)NO\nnon_smile\nnon_smile\n'+
                      'non_smile\nC1=C2C=CC2=C1C3N(CC2)CCNC3\nC1=C(CC)SC2=C1C(=NCC(N2C)=O)C3=CC=CC=C3Cl12\nCC(O)C31(O)CCC4C2CCC1=CC(=O)C=CC1(C)C2C(O)CC34C\nC1=C-(OC)C(=CC2=C1C(=NN=C(C2)C)C3=CC=CC(=C3)Cl)OC\n'+
                      'CN(C)C[=O]COC2c1ccccc1CCc3ccccc23\nnon_smile\n[[C@]4([C@@]3([C@H]([C@H]2[C@]([C@@]1(C(=CC(=O)C=C1)CC2)C)(F)[C@H](C3)O)C[C@@H]4C)C)(OC(CC)=O)C(CCl)=O\nC1=CC=CC=C1CN2C(CC((C2)CN)=O\n'+
                      'C1=C(OC)C=CC3=C1N(C2=C(C=CC=C2)S3)CC(CN4CCC(O)CC4))C\n[[C@@H]1(C[C@H]3[C@H]2[C@@]1(O[C@H](O[C@H]2OC)[C@@H]3C)CN4CCCCC4)O\nnon_smile.\n' +
                      'The erroneous SMILES will be removed from the data.') in mock_stdout.getvalue()
        assert 'For the following SMILES not all descriptors can be computed:\n[N+](=[N-])=O.\nThese SMILES will be removed from the data.' in mock_stdout.getvalue()
        
    def test_CLINTOX_2_erroneous_data_removed_tailored(self):
        """
        44. Test if the erroneous data is removed from the calculated descriptors
        """
        cp = Plotter.from_smiles(self.data_CLINTOX_2_erroneous_smiles["smiles"], target=self.data_CLINTOX_2_erroneous_smiles["target"], target_type="C", sim_type="tailored")
        self.assertEqual(len(cp._Plotter__df_descriptors.index), len(self.data_CLINTOX_2_erroneous_smiles.index) - (len(self.list_CLINTOX_2_erroneous_smiles) + len(self.list_CLINTOX_2_erroneous_descriptors)))
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_CLINTOX_2_erroneous_data_INFO_tailored(self, mock_stdout):
        """
        45. Test if the user is informed about which is the erroneous data and that it will be removed from the dataset
        """
        Plotter.from_smiles(self.data_CLINTOX_2_erroneous_smiles["smiles"], target=self.data_CLINTOX_2_erroneous_smiles["target"], target_type="C", sim_type="tailored")
        assert str('The following erroneous SMILES have been found in the data:\n[NH4][Pt]([NH4])(Cl)Cl\nc1ccc(cc1)n2c(=O)c(c(=O)n2c3ccccc3)CCS(=O)c4ccccc4\nCc1cc2c(cc1C)N3C=N2[Co+]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)[O-])C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)O\n' + 
                   'Cc1cc2c(cc1C)N3C=N2[Co]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)O)C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)C#N\n'+
                   'CCCCc1c(=O)n(n(c1=O)c2ccc(cc2)O)c3ccccc3\nCCCCc1c(=O)n(n(c1=O)c2ccccc2)c3ccccc3.\n' +
                   'The erroneous SMILES will be removed from the data.') in mock_stdout.getvalue()
        assert str('For the following SMILES not all descriptors can be computed:\n*C(=O)[C@H](CCCCNC(=O)OCCOC)NC(=O)OCCOC\n[N+](=O)([O-])[O-]\n[N]=O\n[O-][99Tc](=O)(=O)=O\n[O-]P(=O)([O-])F\n[O-]S(=O)(=O)[O-]\n[O-]S(=O)(=S)[O-]\n[Se]\nC#N\nC(#N)[Fe-2](C#N)(C#N)(C#N)(C#N)N=O\n'+ 
                      'C1CC(C1)(C(=O)O)C(=O)O.N.N.[Pt]\nC1CC2(C1)C(=O)O[Pt]OC2=O\nCCP(=[Au]S[C@H]1[C@@H]([C@H]([C@@H]([C@H](O1)COC(=O)C)OC(=O)C)OC(=O)C)OC(=O)C)(CC)CC\nCl[201Tl]\nCl[Cr](Cl)Cl\nCl[Cu]Cl\nCl[Mn]Cl\nCl[Zn]Cl\nII\nN(=O)[O-]\nO1[As]2O[As]1O2\nO[32P](=O)([O-])[O-]\nO=[Al]O[Al]=O\nO[Si](=O)O\n'+ 
                      'O=[Ti]=O\nO=[Zn]\nOCl(=O)(=O)=O\nS=[Se]=S.\nThese SMILES will be removed from the data.') in mock_stdout.getvalue()
        
    def test_BBBP_erroneous_data_removed_structural(self):
        """
        46. Test if the erroneous data is removed from the calculated descriptors
        """
        cp = Plotter.from_smiles(self.data_BBBP_erroneous_smiles["smiles"], target=self.data_BBBP_erroneous_smiles["target"], target_type="C", sim_type="structural")
        self.assertEqual(len(cp._Plotter__df_descriptors.index), len(self.data_BBBP_erroneous_smiles.index) - len(self.list_BBBP_erroneous_smiles))
    
    @patch('builtins.print')   
    def test_BBBP_erroneous_data_INFO_structural(self, mock_print):
        """
        47. Test if the user is informed about which is the erroneous data and that it will be removed from the dataset
        """
        Plotter.from_smiles(self.data_BBBP_erroneous_smiles["smiles"], target=self.data_BBBP_erroneous_smiles["target"], target_type="C", sim_type="structural")
        mock_print.assert_called_once_with('The following erroneous SMILES have been found in the data:\nC12CCN(CC1)Cc1cccc(c1)OCCCNC(=O)CC12\nC(Cl)Cl1\nNc1nc(c(N@)n1)c2c=ccc(Cl)c2Cl\nnon_smile\n'+
                      'non_smile\nnon_smile\nnon_smile\nnon_smile\nCNc1CCCN1c2ccccc2CCc3ccccc13\nnon_smile\n[O-]][N+](=O)c1ccc2NC(=O)CN=C(c3ccccc3)c2c1\nnon_smile\nCC(Ccccccc1)NO\nnon_smile\nnon_smile\n'+
                      'non_smile\nC1=C2C=CC2=C1C3N(CC2)CCNC3\nC1=C(CC)SC2=C1C(=NCC(N2C)=O)C3=CC=CC=C3Cl12\nCC(O)C31(O)CCC4C2CCC1=CC(=O)C=CC1(C)C2C(O)CC34C\nC1=C-(OC)C(=CC2=C1C(=NN=C(C2)C)C3=CC=CC(=C3)Cl)OC\n'+
                      'CN(C)C[=O]COC2c1ccccc1CCc3ccccc23\nnon_smile\n[[C@]4([C@@]3([C@H]([C@H]2[C@]([C@@]1(C(=CC(=O)C=C1)CC2)C)(F)[C@H](C3)O)C[C@@H]4C)C)(OC(CC)=O)C(CCl)=O\nC1=CC=CC=C1CN2C(CC((C2)CN)=O\n'+
                      'C1=C(OC)C=CC3=C1N(C2=C(C=CC=C2)S3)CC(CN4CCC(O)CC4))C\n[[C@@H]1(C[C@H]3[C@H]2[C@@]1(O[C@H](O[C@H]2OC)[C@@H]3C)CN4CCCCC4)O\nnon_smile.\n' +
                      'The erroneous SMILES will be removed from the data.')        
        
    def test_CLINTOX_2_erroneous_data_removed_structural(self):
        """
        48. Test if the erroneous data is removed from the calculated descriptors
        """
        cp = Plotter.from_smiles(self.data_CLINTOX_2_erroneous_smiles["smiles"], target=self.data_CLINTOX_2_erroneous_smiles["target"], target_type="C", sim_type="structural")
        self.assertEqual(len(cp._Plotter__df_descriptors.index), len(self.data_CLINTOX_2_erroneous_smiles.index) - len(self.list_CLINTOX_2_erroneous_smiles))
        
    @patch('builtins.print')
    def test_CLINTOX_2_erroneous_data_INFO_structural(self, mock_print):
        """
        49. Test if the user is informed about which is the erroneous data and that it will be removed from the dataset
        """
        Plotter.from_smiles(self.data_CLINTOX_2_erroneous_smiles["smiles"], target=self.data_CLINTOX_2_erroneous_smiles["target"], target_type="C", sim_type="structural")
        mock_print.assert_called_once_with('The following erroneous SMILES have been found in the data:\n[NH4][Pt]([NH4])(Cl)Cl\nc1ccc(cc1)n2c(=O)c(c(=O)n2c3ccccc3)CCS(=O)c4ccccc4\nCc1cc2c(cc1C)N3C=N2[Co+]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)[O-])C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)O\n' + 
                      'Cc1cc2c(cc1C)N3C=N2[Co]456(N7=C8[C@H](C(C7=CC9=N4C(=C(C1=N5[C@@]([C@@H]2N6C(=C8C)[C@@]([C@H]2CC(=O)N)(CCC(=O)NC[C@H](OP(=O)(O[C@@H]2[C@H](O[C@H]3[C@@H]2O)CO)O)C)C)([C@@]([C@@H]1CCC(=O)N)(C)CC(=O)N)C)C)[C@@]([C@@H]9CCC(=O)N)(C)CC(=O)N)(C)C)CCC(=O)N)C#N\n'+
                      'CCCCc1c(=O)n(n(c1=O)c2ccc(cc2)O)c3ccccc3\nCCCCc1c(=O)n(n(c1=O)c2ccccc2)c3ccccc3.\n' +
                      'The erroneous SMILES will be removed from the data.') 
 
    def test_no_descriptors_computed(self):
        """
        50. Test if exception is raised when no descriptors can be computed
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CCCC'], sim_type="structural")
        self.assertTrue('Plotter object cannot be instantiated for given molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CCCCCC'], target=[1,0], sim_type="tailored")
        self.assertTrue('Plotter object cannot be instantiated for given molecules' in str(context.exception))
        
    def test_empty_smiles(self):
        """
        51. Test if exception is raised because no mols could be computed
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['aaaa', 'aaaa'], sim_type="structural")
        self.assertTrue('Plotter object cannot be instantiated for given molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['aaaa', 'aaaa'], target=[0, 0], sim_type="tailored")
        self.assertTrue('Descriptors could not be computed for given molecules' in str(context.exception))

    def test_target_diff_smiles(self):
        """
        52. Test if exception is raised target length is not equal to SMILES len
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CC'], target=[9])
        self.assertTrue('If target is provided its length must match the instances of molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CC'], target=[9,1,1])
        self.assertTrue('If target is provided its length must match the instances of molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CC'], target=[9], sim_type="structural")
        self.assertTrue('If target is provided its length must match the instances of molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC', 'CC'], target=[9,1,1], sim_type="structural")
        self.assertTrue('If target is provided its length must match the instances of molecules' in str(context.exception))
        
    @patch('builtins.print')
    def test_INFO_target_type_correct(self, mock_print):
        """
        53. Test checks if user gets notified when target type is non numeric but 'R' is selected
        """
        Plotter.from_smiles(['CCCC', 'CC'], target=[4, '5'], target_type='R', sim_type="structural")
        mock_print.assert_called_with('Input received is \'R\' for target values that seem not continuous.')
        with self.assertRaises(Exception):
            Plotter.from_smiles(['CCCC', 'CC'], target=[4, '5'], target_type='R', sim_type="tailored")
        mock_print.assert_called_with('Input received is \'R\' for target values that seem not continuous.')

    @patch('builtins.print')
    def test_select_target_type_correct(self, mock_print):
        """
        54. Test checks is for non numeric target types 'C' is selected
        """
        result = Plotter.from_smiles(['CCCC', 'CC'], target=[4, '5'], sim_type="structural")
        mock_print.assert_called_with('target_type indicates if the target is a continuous variable or a class label.\n'+
                  'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                  'From analysis of the target, C has been selected for target_type.')
        assert result._Plotter__target_type == 'C'
        result = Plotter.from_smiles(['CCCC', 'CC'], target=[4, '5'], sim_type="tailored")
        mock_print.assert_called_with('target_type indicates if the target is a continuous variable or a class label.\n'+
                  'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                  'From analysis of the target, C has been selected for target_type.')
        assert result._Plotter__target_type == 'C'
    
    def test_one_smiles(self):
        """
        55. Test if exception is raised because only one mol is computed
        """
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC'], sim_type="structural")
        self.assertTrue('Plotter object cannot be instantiated for given molecules' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Plotter.from_smiles(['CCCC'], target=[0], sim_type="tailored")
        self.assertTrue('Plotter object cannot be instantiated for given molecules' in str(context.exception))
    
    def test_no_feature_selected(self):
        """
        56. Test if no feature is selected the class does not crash
        """
        result = Plotter.from_smiles(['CCCC', 'CCCCCC'], target=[0,0])
        assert len(result._Plotter__df_descriptors.columns) == 202
        
    def test_C_unique_class(self):
        """
        57. Test if target is removed for 'C' target type when only one class is present
        """
        result = Plotter.from_smiles(['CCCC', 'OOOOOC'], target=[0,0], target_type="C")
        assert not result._Plotter__target
        result = Plotter.from_smiles(['CCCC', 'OOOOOC'], target=[0,0], target_type="C", sim_type="structural")
        assert not result._Plotter__target


if __name__ == '__main__':
    unittest.main()