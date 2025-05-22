# Mappeinndeling og innhold av besvarelse

## data
Mappe for lagring av innsamlet data. 
Inneholder to undermapper:
- en for [csv-filer](/data/csv)
- en for [json-filer](/data/json)

[data/README.md](/data/README.md)

## docs
Inneholder tre undermapper:
- [besvarelse](/docs/besvarelse): refleksjonsnotatet - oppgave 7 som en .md fil
- [deklarasjon og kilder](/docs/deklarasjon_&_kilder): KI-deklarasjon som .pdf og kildeliste med brukte kilder i prosjektet.
- [tasks](/docs/tasks): oppgavene og vurderingskriteriene til prosjektet. Del 1, del 2 og generell del.

## notebooks
Innhold:
- alle delene av prosjektet fordelt i funksjonelle .ipynb filer.
- gjennomgående forklaringer og resultater av analysen om miljødata

- Les mer her: [notebooks/README.md](/notebooks/README.md)

## resources
 Innhold: 
 - Her ligger bilder/ e.l som vi har brukt i prosjektet. 

 - Les mer her:[resources/README.md](/resources/README.md)

## src
Innhold:
- større koder som benyttes i notebook filene
- alle funksjoner er laget i .py filer

- Les mer her: [src/README.md](/src/README.md)

## .env
Innhold:

- . env er lagringsplass av linker og koder.
- URL til API.met

- [.env](/.env)


## .requirements.txt
Innhold: 

- Lister opp hvilke Python-pakker som prosjektet trenger for å kjøre.
- brukes for å laste ned venv

- [.requirements.txt](/requirements.txt)

## .gitignore
Innhold: 
- Ignorerer spesifikke mapper ved committ til git hub. 

- [.gitignore](/.gitignore)



# Utgangspunktet for oppgave

Fly ønsker å ta av i motvind og lande i motvind. Det er tryggere, mer drivstoffbesparende og sliter mindre på bremser og dekk. Ergo tryggere, lavere kostnader og mer miljøvennlig.

I dette prosjektet ønsker vi å finne ut hva som er optimal retning på flystripen, basert på historisk data for vindretning? Både for Ørlandet hvor de har gjort oppgraderinger uten å flytte retningen på rullebanen og i Bodø hvor det er vedtatt at den skal flyttes.

Man ønsker også å forhindre sidevind, dersom sidevinden er for sterk kan fly bli nektet adgang og landing.

Hvorfor motvind er bra for landing og avgang kan du lese her:  
https://skybrary.aero/articles/headwind
https://simpleflying.com/why-aircraft-take-off-land-into-wind/

## Bodø flyplass
Ny flystripe for Bodø Lufthavn, hva er optimal retning? 

les mer her: https://www.nrk.no/nordland/forste-spadetak-pa-bodo-lufthavn-og-prosjektet-ny-by-ny-flyplass-1.16344890

## Ørland flyplass 
Vi ønsket å undersøke om flystripen på Ørland er optimal, da de nettopp har holdt hoverullebanen stengt grunnet arbeid og renovering i over 1 år? 

Du kan lese mer her: 
https://www.forsvarsbygg.no/no/nyheter/ny-hovedrullebane-pa-orland-flystasjon-er-operativ/

## Dagens rullebaneretninger

ENBO: RWY 07/25 /// 70 og 250 grader

ENOL: RWY 15/33 /// 150 og 330 grader