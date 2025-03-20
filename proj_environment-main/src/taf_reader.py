import json

def read_taf(taf_file):
    try:
        with open(taf_file, 'r') as file:
            taf = json.load(file)
            return taf
    except FileNotFoundError:
        print(f"Error: filen {taf_file} er ikke funnet")
    return None
    