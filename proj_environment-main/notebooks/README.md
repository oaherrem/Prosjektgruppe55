Describes the notebooks directory

Oppgave 1

Vi begynte med å sette opp repository på GitHub for Prosjektgruppe55. Deretter lastet vi opp oppgavemalen og den har vi brukt som utgangspunkt i besvarelsen av mappeinnleveringen. Deretter clonet vi repoen slik at gruppen hadde samme fil. Dermed var utviklingsmiljøet vårt klart.
Printer ut "Utviklingsmiljøet er klart!"

---

Oppgave 2

Programmet henter funksjoner fra mappen src og setter parameterene for data fra en åpen API-kilde og lagrer dataen som en JSON-fil under mappen data.

Vi har valgt en sentral og relevant åpen datakilde for miljødata. api.met.no. Tjenesten leveres av Meterologisk institutt, og er offisiell og pålitelig kilde for meterologisk data i Norge. 

Vi har valgt å spesifisere oppgaven inn på Aviation Weather, mer spesifikt Meteorological Aerodrome Report (METAR) og Terminal Aerodrome Forecast (TAF). METAR blir publisert hver halvtime og er en vær observasjon og TAF blir publisert hver 3 time og er en værmelding for de neste 24 timene. METAR og TAF er internasjonal standardiserte format brukt i luftfart. Dataen er tilgjengelig og krever ingen API-nøkkel som gjør data-innsamlingen enkelt. Parameterene for API-en er tid, lokasjon og formatvalg, som vi ser som en fordel for vår analyse.

Det står mer info om dataen som er benyttet og grunnlag for valg av lagringsmetode av data i README-filen under mappen data.

---

Oppgave 3

Vi har benyttet oss av Pandas-bibliotekets innebygde funksjon for identifisering av missing data. I vår DataFrame i oppgave 3 blir Not a number (NaN) fylt inn for hver manglende data.

List comprehensions er benyttet for å kunne sortere datastrengene. Eksempelvis klarer vi å plassere vind-styrke/retning i en egen kolonne da det er den eneste delen av koden som inneholder KT (knots). Ergo, dersom den inneholder KT plasser den i denne kolonnen.

Pandas SQL gjør det mulig å sortere data i en tabell, altså i kolonner og rader. Dette gjør det mulig å hente ut riktig data til senere analyse. For vår del tar den informasjon lagret i en JSON fil og sorterer informasjonen i tilhørende kolonne, samtidig som den separerer hver publiserte METAR i riktig rad. Dette gjør at vi enklere får overblikk over tendenser og kan analysere dataen i mappe del 2. 

Av den dataen vi henter fra dette datasettet er den største uregelmessigheten lengden på dataen. I det minste laget kan den inneholde 6 koder med informajon og i andre tilfeller kan den være over 18 koder lang. For å håndtere denne uregelmessigheten løser vi ved å bruke list comprehensions, noe av dataen har vi valgt å ekskludere da vi ser på de som irrelevant da de er for uregelmessig, og ikke hjelper å svare på oppgaven vår. Dersom vi skulle ha inkludert nedbørstyper hadde vi hatt 9 ulike nedbørstyper som kan kombineres og bli publisert som lett, moderat og kraftig. Dette hadde vært alt for mye jobb å sortere i en kode for å deretter ikke få bruk for det.