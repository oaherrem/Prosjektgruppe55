import unittest
import sys
import os
import pandas as pd
import numpy as np
import pytest 

#Justerer filbanen til 'src'-mappa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dataFrame_metar import metar_df

class TestMetarDataFrame(unittest.TestCase):

    def setUp(self):
        self.data_m =  {
            "metar": [
                ["ENOL 010020Z 12031KT 9999 DRSN NSC M03/M09 Q1007="],
                ["ENOL 010050Z 12031KT 9999 DRSN NSC M03/M09 Q1006="],
                ["ENOL 020020Z 12028KT 9999 DRSN NSC M03/M10 Q1009="],
                ["ENOL 020050Z 12024KT 9999 DRSN NSC M04/M11 Q1009="],
                ["ENOL 030020Z ////KT 9999 DRSN NSC M04/M12 Q1010="],
                ["ENOL 030050Z 1A725KT 9999 DRSN NSC M06/M11 Q1011="]

            ]
        }
# POSITIVE TESTER:
    def test_metar_columns(self): # tester verdien i internt i en kolonne
        interesting_variables = ["Airport", "Date/time", "Wind_direction", "Wind_speed", "Gust_speed","QNH"]
        df = metar_df(interesting_variables, self.data_m)
    
        self.assertEqual(len(df),6)
        self.assertTrue(all(col in df.columns for col in interesting_variables))
        self.assertEqual(df.loc[0,"Airport"],"ENOL")
        self.assertEqual(df.loc[1,"Wind_direction"],120)
        self.assertEqual(df.loc[2,"Wind_speed"],28)
        self.assertEqual(df.loc[3,"QNH"],"1009")
    
    def test_missing_data(self): # tester manglende data
        interesting_variables = ["Wind_direction", "Wind_speed", "Gust_speed"]
        df = metar_df(interesting_variables,self.data_m)

        self.assertEqual(df.loc[4, "Wind_direction"],0)
        self.assertEqual(df.loc[4, "Wind_speed"],0)
        self.assertTrue(np.isnan(df.loc[2,"Gust_speed"]))

    def test_dataframe(self): #tester hele DataFramen og enkelte variabler
        interesting_variables = ["Airport", "Date/time", "Wind_direction", "Wind_speed", "Gust_speed","QNH","Temperature"]
        df = metar_df(interesting_variables,self.data_m)

        self.assertIsInstance(df,pd.DataFrame)
        self.assertListEqual(list(df.columns), interesting_variables)
        self.assertFalse(df["Airport"].isna().any(), "Airport-kolonnen inneholder NaN!")
        self.assertTrue(df["Gust_speed"].isna().any(), "Det finnes gust_speed")
        self.assertFalse(df["Temperature"].isna().any(),"Temparature-kolonnen inneholder NaN!")

# NEGATIVE TESTER:

    def test_interesting_variables_not_list(self):
        with self.assertRaises(ValueError) as context:
            metar_df("Airport", self.data_m)
        self.assertIn("interesting_variables må være en liste med strenger.", str(context.exception))

    def test_interesting_variables_contains_non_strings(self):
        with self.assertRaises(ValueError) as context:
            metar_df(["Airport", 123], self.data_m)
        self.assertIn("interesting_variables må være en liste med strenger.", str(context.exception))

    def test_missing_metar_key(self):
        data_m_missing_metar = {"no_metar": self.data_m["metar"]}
        with self.assertRaises(KeyError) as context:
            metar_df(["Airport"], data_m_missing_metar)
        self.assertEqual(context.exception.args[0], "data_m må inneholde nøkkelen 'metar'.")

    def test_invalid_interesting_variables_type(self):
        with pytest.raises(ValueError, match="interesting_variables må være en liste med strenger."):
            metar_df("not_a_list", {"metar": []})

    def test_invalid_interesting_variables_element_type(self):
        with pytest.raises(ValueError, match="interesting_variables må være en liste med strenger."):
            metar_df([123, "Date/time"], {"metar": []})

    def test_negative(self):
        interesting_variable = ["Wind_direction"]
        df = metar_df(interesting_variable, self.data_m)
        assert 0 in df["Wind_direction"].values    


    def test_parts_not_string(self):
        # Skal ikke raise, men ignorere ugyldige innslag
        result = metar_df(["Airport"], {"metar": [[12345]]})
        assert isinstance(result, pd.DataFrame)
        assert result.empty

   
if __name__ == '__main__':
    unittest.main()