import requests
print(requests.__version__)


def get_metar_taf(icao_code):
    base_url = "https://api.met.no/weatherapi/tafmetar/1.0/"
    
    metar_url = f"{base_url}?icao={icao_code}&content_type=text/plain&content=metar"
    taf_url = f"{base_url}?icao={icao_code}&content_type=text/plain&content=taf"
    
    metar_response = requests.get(metar_url)
    taf_response = requests.get(taf_url)
    
    metar_data = metar_response.text
    taf_data = taf_response.text
    
    return metar_data, taf_data

icao_code = "ENOL"
metar, taf = get_metar_taf(icao_code)
print("METAR:\n", metar)
print("TAF:\n", taf)


#Fra oppgave 2
# Lagrer dataene i en CSV-fil
#all_data.append(data)
#df = pd.DataFrame(all_data)
#df.to_csv(f'../data/data{icao_code}.csv')