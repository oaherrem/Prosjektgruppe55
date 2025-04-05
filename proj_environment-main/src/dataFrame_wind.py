
import pandas as pd

def metar_df(interesting_variables,data_m):
    df = pd.DataFrame(columns=interesting_variables)
    
    for datapoint in data_m["metar"]:
       for parts in datapoint:
            partsList = parts.split()
            row_data = {}
            
            if len(parts)> 1 and "Airport" in interesting_variables:
                row_data["Airport"] = partsList[0]

            if len(parts)> 2 and "Date/time" in interesting_variables:
                row_data["Date/time"] = partsList[1]

            if len(parts)> 3 and "Wind_direction" in interesting_variables:
                #row_data["Wind_direction"] = int(partsList[2][:3])
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

            # Konverter row_data til en DataFrame og legg den til df ved hjelp av pd.concat
            row_df = pd.DataFrame([row_data])
            df = pd.concat([df, row_df], ignore_index=True)
    return df
