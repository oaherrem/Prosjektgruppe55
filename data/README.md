# Data
Innholdet i denne mappen består av nedlastet data gjennom en API fra meterologisk institutt. VI har valgt å dele mappen inn i to delmapper: en for json-filer og en for csv-filer. På denne måten holder vi denne mappen ryddig, i tillegg til at det er enkelt å jobbe med data-filene underveis. 

## [json](/data/json)

Innhold: 

- rådata fra API met, med metar data fra et år
- I oppgave 2 blir data for to flyplasser, i vårt tilfelle Ørland og Bodø, fra API.met lagret som json filer i denne mappa. 
- Vi benytter [base_url](../.env) og funksjonen [metar_writer](../src/metar_writer.py) for å hente metar dataen. 

## [csv](/data/csv)

Innhold:

- renset data fra json-filene
- dataen i disse filene blir lagret gjennom filen som heter ['databehandling'](../notebooks/03_databehandling.ipynb). 
- Vi har laget en funskjon [dataframe_metar](../src/dataFrame_metar.py) som iterer over alle datapunktene i datasettet og deretter lagrer det som en dataframe. 
- Dataframen består av utvalgte variabler vi benytter videre i analysen vår. 

## Generell info om innsamlet data - METAR:

METAR inneholder informasjon som vindhastighet, vindkast (gust), vindretning, temperatur, duggpunkt, sikt, skydekke, nedbør og trykk over havnivå (QNH) oppført i hektopascal (hPa).

International Civil Aviation Organization-koder (ICAO-koder) er en internasjonal standard og navngivning av flyplasser og landingsplasser likt den mer kjente standarden IATA-koder som OSL for Oslo Lufthavn og TRD for Trondheim Lufthavn. Det som gjør ICAO-koder til en mer presis navngivning av flyplasser og landingsplasser er at den er unik og kan ikke forveksles med andre flyplasser eller landingsplasser, i motsetning til IATA-koder som ikke er unike og kan brukes for flere plasser.

Ordet METAR vil bli brukt gjennomgående i navngivning av funksjoner og tester, da dette er en spesifikk vær-datatype.