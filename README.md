# CI

Detta projekt skapar ett python projekt som kontrollerar om ett namn finns i en lista.

## Funktioner
* Hämtar en lista med namn
* Kontrollerar om namn finns 
* Returnerar ett namnet finns eller inte

## Tester
* Unit test med marker 'Unit'
* Integrations tester med marker 'Integration'

### Kör lokalt
Installera beroenden:
```bash
pip install -r requrements.txt
```

## Projektet innehåller enligt uppgift
* Workflow mapp
* Konfigurationsfiler: requrements.txt, pytest.ini, setup.cfg
* src mappen innehåller funktion för att skapa lista
* Det finns två testfall för unittest och ett integrationstest. Det innehåller markers
* Vid push till man skapas lintas och testas (unit och inegration)