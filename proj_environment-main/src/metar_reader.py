import json

def read_metar(metar_file):
    try:
        with open(metar_file, 'r') as file:
            taf = json.load(file)
            return taf
    except FileNotFoundError:
        print(f"Error: filen {metar_file} er ikke funnet")
    return None