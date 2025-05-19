
# Notebooks:
Denne mappen innholder .ipynb filer som henter data og funksjoner fra andre mapper og deretter printer og visulaiserer analysen. Hver undermappe tar for seg ulike funksjonaliteter av analysen, som er delt inn i to overordnede deler: Del 1 - datainnsamling og forberedelser og Del 2 - dataanlyse og visualisering.

 ## DEL 1 Datainnsamling og forberedelse

 ### Oppgave 1: [Sett opp utviklingsmiljø](./01_utviklingsmiljø.ipynb)

Her setter vi opp utviklingsmiljøet vårt og printer setningen; Utviklingsmiljøet er klart! for å teste at utviklingsmiljøet fungerer. 

### Oppgave 2: [Datainnsamling](./02_datainnsamling.ipynb) 

Her samler vi inn nødvendig data ved bruk av en API og funksjonen [metar_writer](../src/metar_writer.py) som itererer og lagrer dataen som en [json](../data/json/ENOL_metar_data.) fil.
 

### Oppgave 3: [Databehandling](./03_databehandling.ipynb)

Denne delen renser og  sorter innsamlet [data](../data/json) i funksjonelle kategorier ved bruk av funksjonen  [dataframe_metar](../src/dataFrame_metar.py) og teknikker som list comprehensions og Pandas SQL. 

Resultatet vi får etter databehnaldingen blir lagret som en dataframe i [csv mappa](../data/csv).

## DEL 2 Dataanalyse og visualisering 
I denne delen benytter vi den rensede dataframen som ble lagret i en csv-fil fra del 1 til videre analyse og visualiseringer.
- Renset [dataframe](../data/csv/ENOL_wind_data.csv)

### Oppgave 4: [Dataanalyse](./04_dataanalyse.ipynb)


### Oppgave 5: Visualsiering 

[Visulaisering](./05_visualisering.ipynb)

[Link til kode i bilde - kartbakgrunn av ENOL](../resources/images/ENOL_kart.png)

### Oppgave 6: Prediktiv analyse

[Link til kode i notebook mappe del 2](./)