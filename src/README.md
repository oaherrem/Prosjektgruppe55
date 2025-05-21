
# Src mappe

I mappen src ligger koder som kan benyttes flere ganger for besvarelse for oppgavene.

## [__init__.py](__init__.py)

Funksjonalitet
- gjør det mulig å finne/importere pyhon koder i 'src' mappe, i andre overordnede mapper, ved å gjøre om mappa til en python-pakke

## [avg_widget.py](avg_widget.py)

Funksjonalitet: 
- denne funksjonen brukes [her](../notebooks/05_visualisering.ipynb)

## [crosswind.py](crosswind.py)
Funksjonalitet:
- finner antall tilfeller av sidevind, basert på historiske datapunkter

- denne funksjonen brukes [her](../notebooks/04_dataanalyse.ipynb)

## [dataFrame_metar.py](dataFrame_metar.py)
Funksjonalitet:
- plasserer og sorterer kategorisk data ved bruk av list comprehensions
- for-loop med flere if-setninger for å plassere rett type data i rett kolonne
- formålet - lage en pandas.DataFrame
- denne funksjonen brukes [her](../notebooks/03_databehandling.ipynb)

## [Metar_writer](metar_writer.py) 

Funksjonalitet:
- skriver METAR-data basert på parameter gitt av bruker
- identifiserer bruker til eier av API, grunnet krav fra eier, i dette tilfelle Meterologisk Institutt
- importer også URL gjennom [.env](../.env)
 