# Mappeinndeling og innhold av besvarelse

## Data
Mappe for lagring av innsamlet data. Inneholder to undermapper, en for csv filer og en for json filer. 

[Data](/proj_environment-main/data/README.md)

## Docs
Innholder dokumentasjon og utfyllende besvarelser. 
- Oppgavebeskrivelsene av del 1 + 2 samt generell del
- Utfyllende svar på oppgavene og vurderingskriteriene 

[Docs\tasks](/proj_environment-main/docs/tasks/del_1.md)

## Notebooks

Her ligger kodene for hver oppgave. Vi importerer lagrede data filer i tillegg til våre hovedfunksjoner. 

[Notebooks](/proj_environment-main/notebooks/README.md)
## Resources
 
 - Her ligger bilder/ e.l som vi har brukt i prosjektet. 

[Resources](/proj_environment-main/resources/README.md)

## Src

I denne mappen ligger koder som kan benyttes flere ganger. Dette gjør kodene mer brukervennlige å hente opp flere ganger uten å måtte kopiere koden direkte inn i hver fil. 

[Src](/proj_environment-main/src/README.md)

## .env
. env er lagringsplass av linker, API-nøkler og koder.

[.env](/proj_environment-main/.env)




## .requirements.txt

Lister opp hvilke Python-pakker som prosjektet trenger for å kjøre.
[.requirements.txt](/requirements.txt)

## .gitignore

Ignorerer deler i forbindelse emg git hub. 

[.gitignore](/.gitignore)


# Utgangspunktet for oppgave

Forklaring**
## Bodø flyplass
Ny flystripe for Bodø Lufthavn
https://www.nrk.no/nordland/forste-spadetak-pa-bodo-lufthavn-og-prosjektet-ny-by-ny-flyplass-1.16344890

## Ørland flyplass 
Vi ønsket å undersøke om flystripen på Ørland er optimal, da de nettopp har holdt hoverullebanen stengt grunnet arbeid og renovering i over 1 år? 

Du kan lese mer her: 
https://www.forsvarsbygg.no/no/nyheter/ny-hovedrullebane-pa-orland-flystasjon-er-operativ/

## Dagens rullebaneretninger

ENBO: RWY 07/25 /// 70 og 250 grader

ENOL: RWY 15/33 /// 150 og 330 grader


## Prosjektets premisser

Fly ønsker å ta av i motvind og lande i motvind. Det er tryggere, mer drivstoffbesparende og sliter mindre på bremser og dekk. Ergo tryggere, lavere kostnader og mer miljøvennlig.

I dette prosjektet ønsker vi å finne ut hva som er optimal retning på flystripen, basert på historisk data for vindretning? Både for Ørlandet hvor de har gjort oppgraderinger uten å flytte retningen på rullebanen og i Bodø hvor det er vedtatt at den skal flyttes.


Hvorfor motvind er bra for landing og avgang kan du lese her:  
https://skybrary.aero/articles/headwind
https://simpleflying.com/why-aircraft-take-off-land-into-wind/
