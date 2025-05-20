import unittest
import sys
import os
import pandas as pd
import numpy as np
import pytest 

# Adjust the path to the src directory
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

    def test_negative(self):
        interesting_vars = ["Wind_direction"]
        df = metar_df(interesting_vars, self.data_m)
        assert 0 in df["Wind_direction"].values

    def test_invalid_interesting_variables_type(self):
        with pytest.raises(ValueError, match="interesting_variables må være en liste med strenger."):
            metar_df("not_a_list", {"metar": []})

    def test_invalid_interesting_variables_element_type(self):
        with pytest.raises(ValueError, match="interesting_variables må være en liste med strenger."):
            metar_df([123, "Date/time"], {"metar": []})

    def test_data_m_not_dict(self):
        with pytest.raises(ValueError, match="data_m må være en dictionary."):
            metar_df(["Airport"], ["not", "a", "dict"])

    def test_data_m_missing_metar_key(self):
        with pytest.raises(KeyError, match="data_m må inneholde nøkkelen 'metar'."):
            metar_df(["Airport"], {"not_metar": []})

    def test_metar_key_not_iterable(self):
        with pytest.raises(ValueError, match="data_m\\['metar'\\] må være en liste eller lignende itererbar."):
            metar_df(["Airport"], {"metar": "not_a_list"})

    def test_datapoint_not_iterable(self):
        # Skal ikke raise, men funksjonen skal ignorere ikke-liste datapunkt
        result = metar_df(["Airport"], {"metar": ["not a list inside"]})
        assert isinstance(result, pd.DataFrame)
        assert result.empty

    def test_parts_not_string(self):
        # Skal ikke raise, men ignorere ugyldige innslag
        result = metar_df(["Airport"], {"metar": [[12345]]})
        assert isinstance(result, pd.DataFrame)
        assert result.empty

   
if __name__ == '__main__':
    unittest.main()