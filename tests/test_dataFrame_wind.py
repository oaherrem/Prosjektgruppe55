import unittest
import sys
import os
import pandas as pd

# Adjust the path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dataFrame_wind import metar_df

class TestMetarDataFrame(unittest.TestCase):
    def test_metar_df(self):
        # Eksempeldata for testing
        data_m = {
            "metar": [
                "ENOL 010020Z 12031KT 9999 DRSN NSC M03/M09 Q1007=",
                "ENOL 010050Z 12031KT 9999 DRSN NSC M03/M09 Q1006=",
                "ENOL 020020Z 12028KT 9999 DRSN NSC M03/M10 Q1009=",
                "ENOL 020050Z 12024KT 9999 DRSN NSC M04/M11 Q1009=",
            ]
        }
        interesting_variables = ["Airport", "Date/time", "Wind_direction", "Wind_speed", "Gust_speed","QNH"]

        # Kjør funksjonen
        dataframe = metar_df(interesting_variables, data_m)

        # Sjekk at resultatet er en DataFrame
        self.assertIsInstance(dataframe, pd.DataFrame)

        # Sjekk at DataFrame har de riktige kolonnene
        self.assertListEqual(list(dataframe.columns), interesting_variables)

        self.assertFalse(dataframe["Airport"].isna().any(), "Airport-kolonnen inneholder NaN!")

        # Sjekk at DataFrame har riktig antall rader
        self.assertEqual(len(data_m["metar"]), len(dataframe),4)

        # Sjekk at verdiene i DataFrame er riktige
        self.assertEqual(dataframe["Airport"].iloc[0],"ENOL") # kjører fra første linje i datasettet. 
        self.assertEqual(dataframe["Date/time"].iloc[1],"010050Z") # kjører fra andre linje i datasettet. 
        self.assertEqual(dataframe["Wind_direction"].iloc[2],120) # tredje linje i datasettet. 
        self.assertEqual(dataframe["QNH"].iloc[3],"1009") # fjerde linje i datasettet.

if __name__ == '__main__':
    unittest.main()