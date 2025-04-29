import numpy as np
import pandas as pd
import re
 
# Eksempel på kolonnenavn
#column_names = ["Airport", "Date/time", "Wind_speed","Wind_direction","Gust_speed" ,"Variable wind", "Cloud 1", "Cloud 2", "Cloud 3", "Cloud 4", "Cloud 5", "Temperature", "Dewpoint", "QNH"]
 
 
def metar_df(interesting_variables,data_m):
    df = pd.DataFrame(columns= interesting_variables)
   
    for datapoint in data_m["metar"]:
       for parts in datapoint:
            partsList = parts.split()
            
            row_data = {}
           
            if len(parts)> 1 and "Airport" in interesting_variables:
                row_data["Airport"] = partsList[0]
 
            if len(parts)> 2 and "Date/time" in interesting_variables:
                row_data["Date/time"] = partsList[1]
 

            if len(parts)> 3 and "Wind_direction" in interesting_variables:
                wind_dir_str = partsList[2][:3]
                try:
                    row_data["Wind_direction"] = int(wind_dir_str)
                except ValueError:
                    row_data["Wind_direction"] = 0

            if len(parts)> 3 and "Wind_speed" in interesting_variables:
                wind_speed_str = partsList[2][3:5]
                try:
                    row_data["Wind_speed"] = int(wind_speed_str)
                except ValueError:
                    row_data["Wind_speed"] = 0  

            if len(parts)> 3 and "Gust_speed" in interesting_variables:
                wind_speed_str = partsList[2][6:8]
                try:
                    row_data["Gust_speed"] = int(wind_speed_str)
                except ValueError:
                    row_data["Gust_speed"] = np.nan
 
            if "Variable wind" in interesting_variables:
                for part in partsList:
                    if "V" in part and len(part)==7:
                        row_data["Variable wind"] = part
                        break
                    else: row_data["Variable wind"] = np.nan
               
 
            if "Cloud 1" in interesting_variables:
                for part in partsList:
                    if part == "CAVOK":
                        row_data["Cloud 1"] = part
                        break
                    else: row_data["Cloud 1"] =np.nan
               
 
            if "Cloud 2" in interesting_variables:
                for part in partsList:
                    if "FEW" in part and len(part) > 4:
                        row_data["Cloud 2"] = part
                        break
                    else: row_data["Cloud 2"] = np.nan
       
 
            if "Cloud 3" in interesting_variables:
                for part in partsList:
                    if "SCT" in part and len(part)> 4:
                        row_data["Cloud 3"] = part
                        break
                    else: row_data["Cloud 3"] =np.nan
           
 
            if "Cloud 4" in interesting_variables:
                for part in partsList:
                    if "BKN" in part and len(part)> 4:
                        row_data["Cloud 4"] = part
                        break
                    else: row_data["Cloud 4"] =np.nan            
 
            if "Cloud 5" in interesting_variables:
                for part in partsList:
                    if "OVC" in part:
                        row_data["Cloud 5"] = part
                        break
                    else: row_data["Cloud 5"] =np.nan
               
            if "Temperature" in interesting_variables or "Dewpoint" in interesting_variables:
                temp_dewpoint_value = np.nan  
                temp_dewpoint_pattern = re.compile(r'^(M?\d{1,2})/(M?\d{1,2})$')

                for part in partsList:
                    if temp_dewpoint_pattern.match(part):
                        temp_dewpoint_value = part
                        break

                if isinstance(temp_dewpoint_value, str):
                    temp_str, dew_str = temp_dewpoint_value.split('/')

                    if "Temperature" in interesting_variables:
                        row_data["Temperature"] = int(temp_str.replace('M', '-'))
                    if "Dewpoint" in interesting_variables:
                        row_data["Dewpoint"] = int(dew_str.replace('M', '-'))
                else:
                    if "Temperature" in interesting_variables:
                        row_data["Temperature"] = np.nan
                    if "Dewpoint" in interesting_variables:
                        row_data["Dewpoint"] = np.nan

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