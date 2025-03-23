Describes the notebooks directory

Oppgave 1

Vi begynte med å sette opp repository på GitHub for Prosjektgruppe55. Deretter lastet vi opp oppgavemalen og den har vi brukt som utgangspunkt i besvarelsen av mappeinnleveringen. Deretter clonet vi repoen slik at gruppen hadde samme fil. Dermed var utviklingsmiljøet vårt klart.
Printer ut "Utviklingsmiljøet er klart!"

---

Oppgave 2

Programmet henter funksjoner fra mappen src og setter parameterene for data fra en åpen API-kilde og lagrer dataen som en JSON-fil under mappen data.

Vi har valgt en sentral og relevant åpen datakilde for miljødata. api.met.no. Tjenesten leveres av Meterologisk institutt, og er offisiell og pålitelig kilde for meterologisk data i Norge. 

Vi har valgt å spesifisere oppgaven inn på Aviation Weather, mer spesifikt Meteorological Aerodrome Report (METAR) og Terminal Aerodrome Forecast (TAF). METAR blir publisert hver halvtime og er en vær observasjon og TAF blir publisert hver 3 time og er en værmelding for de neste 24 timene. METAR og TAF er internasjonal standardiserte format brukt i luftfart. Dataen er tilgjengelig og krever ingen API-nøkkel som gjør data-innsamlingen enkel. Parameterene for API-en er tid, lokasjon og formatvalg, som vi ser som en fordel for vår analyse.

Det står mer info om dataen som er benyttet og grunnlag for valg av lagringsmetode av data i README-filen under mappen data.

---

Oppgave 3

