
# Notebooks:
Denne mappen innholder .ipynb filer som henter data og funksjoner fra andre mapper, printer og visualiserer analysen vår. Hver undermappe tar for seg ulike funksjonaliteter av analysen, og er delt inn i to overordnede deler: Del 1 - datainnsamling og forberedelser og Del 2 - dataanlyse og visualisering.

 ## DEL 1 Datainnsamling og forberedelse

 ### Oppgave 1: [Sett opp utviklingsmiljø](./01_utviklingsmiljø.ipynb)

Her setter vi opp utviklingsmiljøet vårt og printer setningen; Utviklingsmiljøet er klart! for å teste at utviklingsmiljøet fungerer. 

### Oppgave 2: [Datainnsamling](./02_datainnsamling.ipynb) 

- samler vi inn nødvendig data ved bruk av en API
- bruker funksjonen [metar_writer](../src/metar_writer.py) som itererer og lagrer dataen
- Datasettet blir lagret som en [json-fil](../data/json/ENOL_metar_data.) under mappen 'data'.
 

### Oppgave 3: [Databehandling](./03_databehandling.ipynb)

- Datasette fra [json-fil](../data/json) blir renset og sortert i funksjonelle kategorier 
- Benytter funksjonen  [dataframe_metar](../src/dataFrame_metar.py) 
- andre teknikker som blir brukt et list comprehensions og Pandas SQL. 

Resultatet vi får etter databehanldingen blir lagret som en dataframe i [csv mappa](../data/csv).

## DEL 2 Dataanalyse og visualisering 
I denne delen bruker vi den rensede dataframen som ble lagret i en csv-fil fra del 1, i visualiseringer og videre analyse/prediksjon.
- Renset [dataframe](../data/csv/ENOL_data.csv) i csv-fil

### Oppgave 4: [Dataanalyse](./04_dataanalyse.ipynb)
- Bergener statistiske mål som gjennomsnitt, median og standardavvik, hvor vi bruker Numpy og Pandas biblioteker.
- groupby() - pandas funksjonalitet
- [Crosswind](../src/crosswind.py) funksjonen brukes for å analysere vindretning som ligger innenfor et kritisk område med tanke på sidevind på en rullebane.
- først brukes funksjonen til å finne antall tilfeller av nåværende rullebane posisjon ved hjelp av .append
- deretter brukes funksjonen til å finne optimal rullebane posisjon og printer antall tilfeller. 

### Oppgave 5: [Visualiseringer](./05_visualisering.ipynb)

- [Kart](../resources/images/ENOL_kart.png) som er brukt i en vindrose visualiseringen. 
- [Kilde](../docs/deklarasjon_&_kilder/kilder.md) vindrose funksjon 

### Oppgave 6: [Prediktiv analyse](./06_prediktiv_analyse.ipynb)
 - [kilde](../docs/deklarasjon_&_kilder/kilder.md) lineær regresjon 


 ##
 VI har brukt Jupyter-boka gjennom hele prosjektet og som inspirasjon under analysen vår. 