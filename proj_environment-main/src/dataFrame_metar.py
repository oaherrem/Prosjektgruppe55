import numpy as np
import pandas as pd
 
 
# Eksempel på kolonnenavn
#column_names = ["Airport", "Date/time", "Wind/direction", "Variable wind", "Cloud 1", "Cloud 2", "Cloud 3", "Cloud 4", "Cloud 5", "Temp/dewpoint", "QNH/pressure"]
 
 
def metar_df(interesting_variables,data_m):
    df = pd.DataFrame(columns= interesting_variables)
   
    for datapoint in data_m["metar"]:
       for parts in datapoint:
            partsList = parts.split()
            #print(partsList)
            row_data = {}
           
            if len(parts)> 1 and "Airport" in interesting_variables:
                row_data["Airport"] = partsList[0]
 
            if len(parts)> 2 and "Date/time" in interesting_variables:
                row_data["Date/time"] = partsList[1]
 
            if len(parts)> 3 and "Wind/direction" in interesting_variables:
                row_data["Wind/direction"] = partsList[2]
 
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
               
            if "Temp/dewpoint" in interesting_variables:
                for part in partsList:
                    if "/" in part and len(part)> 3:
                        row_data["Temp/dewpoint"] = part
                        break
                    else: row_data["Temp/dewpoint"] = np.nan
           
            if "QNH/pressure" in interesting_variables:
                for part in partsList:
                    if "Q" in part and len(part)> 3:
                        row_data["QNH/pressure"] = part
                        break
                    else: row_data["QNH/pressure"] = np.nan
           
        # Konverter row_data til en DataFrame og legg den til df ved hjelp av pd.concat
            row_df = pd.DataFrame([row_data])
            df = pd.concat([df, row_df], ignore_index=True)
    return df