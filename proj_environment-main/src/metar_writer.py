import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_metar(icao_code, date):
    base_url = os.getenv("base_url")
    
    metar_url = f"{base_url}?icao={icao_code}&content_type=text/plain&content=metar&date={date}"
    
    metar_response = requests.get(metar_url)
    
    metar_data = metar_response.text
    
    return metar_data
