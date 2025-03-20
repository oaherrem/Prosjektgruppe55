import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Funksjoner

def get_taf(icao_code, date):
    base_url = os.getenv("base_url")
    
    taf_url = f"{base_url}?icao={icao_code}&content_type=text/plain&content=taf&date={date}"
    
    taf_response = requests.get(taf_url)
    
    taf_data = taf_response.text
    
    return taf_data