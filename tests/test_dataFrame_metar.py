import unittest
import sys
import os
import pandas as pd
import numpy as np

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
                ["ENOL 030020Z ////KT 9999 DRSN NSC M04/M12 Q1010"]

            ]
        }
   

    def test_metar_columns(self):
        interesting_variables = ["Airport", "Date/time", "Wind_direction", "Wind_speed", "Gust_speed","QNH"]
        df = metar_df(interesting_variables, self.data_m)

        self.assertEqual(len(df),5)
        self.assertTrue(all(col in df.columns for col in interesting_variables))
        self.assertEqual(df.loc[0,"Airport"],"ENOL")
        self.assertEqual(df.loc[1,"Wind_direction"],120)
        self.assertEqual(df.loc[2,"Wind_speed"],28)
        self.assertEqual(df.loc[3,"QNH"],"1009")

    def test_missing_data(self):
        interesting_variables = ["Wind_direction", "Wind_speed", "Gust_speed"]
        df = metar_df(interesting_variables,self.data_m)

        self.assertEqual(df.loc[4, "Wind_direction"],0)
        self.assertEqual(df.loc[4, "Wind_speed"],0)
        self.assertTrue(np.isnan(df.loc[2,"Gust_speed"]))

    def test_dataframe(self):
        interesting_variables = ["Airport", "Date/time", "Wind_direction", "Wind_speed", "Gust_speed","QNH"]
        df = metar_df(interesting_variables,self.data_m)

        self.assertIsInstance(df,pd.DataFrame)
        self.assertListEqual(list(df.columns), interesting_variables)
        self.assertFalse(df["Airport"].isna().any(), "Airport-kolonnen inneholder NaN!")
        self.assertTrue(df["Gust_speed"].isna().any(), "Det finnes gust_speed")
       

if __name__ == '__main__':
    unittest.main()