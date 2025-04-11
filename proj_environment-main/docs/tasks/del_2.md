# Mappe del 2
Forklaring mappe del 2: 

## Oppgave 4

1. Vi har brukt Pandas innebygde koder for å regne ut gjennomsnitt, median og standardavvik for dataen vi har valgt å fokusere på. Da vi har valgt å fokusere på vind-retning og hastighet er disse verdiene viktig statistiske mål fordi det forteller oss om variasjonene i målingene. 

2. Ved å bruke gjennomsnittlig måling av vind og vindkast, får vi et mer realistisk bilde på hvordan været faktisk er. Da vi er interessert i hvor ofte vinden er over 35 8kt, kan vi bruke den innebygde funksjonalitet max() til å si noe om hvor mye vinden begrenser aktivtet ved en flyplass. Den andre variabelen vi skal se på er trykk og hvordan den endrer seg i fht vinden. 

3. ved eventuelle skjevheter eller der vi vet vi ikke nødvendigvis får data hver gang, jobber vi kritisk med resultatene vi får. Da vi kjenner til denne måten dataen fungerer, har vi også en tanke på hvilke resultater vi forventer. 

4. Vi planlegger å bruke visualiseringsverktøyer windrose som en del av analysen av vindretning og hastighet, i tillegg til vindkast ved en flyplass. 

- søylediagram 



## Oppgave 5 


3. Vi valgte å lage en grafisk modell av vindkast opp mot trykk, hvor vi første hadde verdi 0 som representerte manglende data. I grafen så vi at alle null verdiene ble inkuldert, og ga oss en graf som ikke ble riktig representert. Vi gikk derfor tilbake i funksjonen vår "dataFrame_wind" for å bytte null med NaN. Etter denne endringen fikk vi en graf som representerte 


## Oppgave 6 

3. Ser fra oppgave 4 og 5, at vi forventet manglende data i vindkast. Ved å benytte "missingno" bibliotek klarer vi å visualiserer manglende data i vår data frame. Denne viser tydelig mangler under kolonnen "Gust_speed". 
Brukte også .isnull for å telle hvor mange tilfeller det mangler gust_speed data. Resultat ga oss at mindre enn 4% av all dataen inneholder gust-data. 
På bakgrunn av dette, vil potensielt gi misvisende resultater på den totale analysen. 

