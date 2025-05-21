# Tests mappe

I denne mappen ligger det enhetstester for de viktigste funksjonene våre. Hovedprinsippet som er brukt i alle enhetstestene er Arrange - Act - Assert. 

## Enhetstest: [crosswind](test_crosswind.py)

- funksjon som blir testet: [crosswind](../src/crosswind.py)
- tester verdier ved å bruke assertTrue/False av forskjellige vindretninger. 

## Enhetstest: [dataFrame_metar](test_dataFrame_metar.py)

- funksjon som blir testet: [dataFrame_metar](../src/dataFrame_metar.py)
- positive enhetstester: tester dataframen som helhet, manglende verdier og ulike interesting_varibles
- negative tester som formatet til dataen, ugyldige interesting variables og nøkkelordet 'metar'

## Enhetstest: [metar_writer](test_metar_writer.py)
- funksjon som blir testet: [metar_writer](../src/metar_writer.py)
- tester formatet av datasettet, at den henter riktig antall linjer og at flyplassen i datasettet stemmer med flyplassen som blir hentet. 