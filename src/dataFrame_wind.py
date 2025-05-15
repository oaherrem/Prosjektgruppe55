
import pandas as pd
import numpy as np

def metar_df(interesting_variables,data_m):
    df = pd.DataFrame(columns=interesting_variables)
    
    for datapoint in data_m["metar"]:
        if isinstance(datapoint, list):
            datapoint = datapoint[0]
        partsList = datapoint.split()
        row_data = {}
        
        if len(partsList)> 1 and "Airport" in interesting_variables:
            row_data["Airport"] = partsList[0]

        if len(partsList)> 2 and "Date/time" in interesting_variables:
            row_data["Date/time"] = partsList[1]

        if len(partsList)> 3 and "Wind_direction" in interesting_variables:
            wind_dir_str = partsList[2][:3]
            try:
                row_data["Wind_direction"] = int(wind_dir_str)
            except ValueError:
                row_data["Wind_direction"] = 0

        if len(partsList)> 3 and "Wind_speed" in interesting_variables:
            wind_speed_str = partsList[2][3:5]
            try:
                row_data["Wind_speed"] = int(wind_speed_str)
            except ValueError:
                row_data["Wind_speed"] = 0  

        if len(partsList)> 3 and "Gust_speed" in interesting_variables:
            wind_speed_str = partsList[2][6:8]
            try:
                row_data["Gust_speed"] = int(wind_speed_str)
            except ValueError:
                row_data["Gust_speed"] = np.nan
        
        if "QNH" in interesting_variables:
            for part in partsList:
                if "Q" in part and len(part)> 3:
                    row_data["QNH"] = part[1:5]
                    break
                else: row_data["QNH"] = np.nan

        # Konverter row_data til en DataFrame og legg den til df ved hjelp av pd.concat
        row_df = pd.DataFrame([row_data])
        df = pd.concat([df, row_df], ignore_index=True)
    return df
