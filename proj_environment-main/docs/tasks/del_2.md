# Mappe del 2
Forklaring overordnet* mappe del 2: 

## Oppgave 4
I oppgave 4 starter vi med å definere en variabel "airport" som vi skal bruke for å analysere data for den valgte flyplassen. På denne måten trenger vi kun å bytte ut f.eks. ENOL med ENBO for å hente ut verdier fra en annen flyplass. 

1. Vi har brukt Numpy og Pandas innebygde koder for å regne ut gjennomsnitt, median og standardavvik for data som vi henter du fra datasettet vårt. Da vi har valgt å fokusere på vind-retning og hastighet er disse verdiene viktig statistiske mål i denne analysen, fordi dette forteller oss senere hvor mye målingene varierer. 

2. 
Vi har valgt å gjennomføre en enkel statistisk analyse ved å ta gjennomsnittet av vind retning mot tre andre variabler: vindhastighet, vindkast og trykk. Vi gjør dette ved den innebygde pandas-funksjonen groupby().
Vi har dessuten valgt å gjennomføre tilsvarende analyse med variabelen trykk, mot tre andre variabler: vindretning, vindhastighet og vindkast. Dette er noe vi ser nærmere på i vår analyse i oppgave 5 og 6. 

En annen analyse vi er interessert i er hvor mange tilfeller av sidevind som oppstår på en flyplass over en periode. Grunnen til dette er fordi det påvirker flyplassen sin operasjonelle status. Vi har valgt å lage en dynamisk funskjon "is_crosswind", som sjekker alle vindretningene som ligger innenfor vårt definerte kritiske området, samt vindhastighet over 35 knop. 


3. Ved eventuelle skjevheter eller der vi vet vi ikke nødvendigvis får data hver gang, jobber vi kritisk med resultatene vi får. Da vi kjenner til måten dataen fungerer på, har vi også en tanke på hvilke resultater vi forventer. Ved hjelp av bibliotekte missingno og dens innbygde funksjonen msno.matrix kan vi enkelt visualisere manglende verdier i datasettet vårt. Vi vet at metar-data alltid gir verdier som vindretning, vindhastighet og trykk. Det som kan variere er vindkast, som vi planlegger å sjekke. For å sjekke at programmet vårt klarer å håndtere manglende verdier fra flere variabler, vil vi med vilje slette noen datapunkter. 

4. I vår analyse planlegger vi å bruke ulike visualiseringsverktøyer for å underbygge analysen vår av ulike variabler. 
Forskjellige visualiseringer som vi planlegger å lage er scatterplott i 2D, vindrose, linjediagram og korrelasjon av ulike variabler. 
Bibliotek vi bruker:
- matplotlib.pyplt for å lage scatter plot og vindrose som skal sammenlikne vindretning opp mot vindhastighet og vindkast. Dessuten bruker vi dette til å vise grafene og diagrammene. 
- seaborn bruker vi for å lage linjediagram av vindretning
- Widgets planlegger vi å bruke for å gjøre*




## Oppgave 5 


3. Vi valgte å lage en grafisk modell av vindkast opp mot trykk, hvor vi første hadde verdi 0 som representerte manglende data. I grafen så vi at alle null verdiene ble inkuldert, og ga oss en graf som ikke ble riktig representert. Vi gikk derfor tilbake i funksjonen vår "dataFrame_wind" for å bytte null med NaN. Etter denne endringen fikk vi en graf som representerte 


## Oppgave 6 

3. Ser fra oppgave 4 og 5, at vi forventet manglende data i vindkast. Ved å benytte "missingno" bibliotek klarer vi å visualiserer manglende data i vår data frame. Denne viser tydelig mangler under kolonnen "Gust_speed". 
Brukte også .isnull for å telle hvor mange tilfeller det mangler gust_speed data. Resultat ga oss at mindre enn 4% av all dataen inneholder gust-data. 
På bakgrunn av dette, vil potensielt gi misvisende resultater på den totale analysen. 

