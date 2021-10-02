# Yksikkötestaus

## Kattavuusraportti
* Alla yksikkötestien kattavuus viikon 4 jälkeen:
![Test coverage 2021-10-03](https://user-images.githubusercontent.com/62505549/135732255-d2082cbb-6181-4a42-856e-3941a2f6a16a.png)

## Mitä on testattu, miten tämä tehtiin?
* Toteutin yksikkötestauksen Pythonin standardikirjastoon kuuluvalla unittest-kirjastolla: https://docs.python.org/3/library/unittest.html
* Testikattavuusraportti tulee coverage-työkalulla: https://coverage.readthedocs.io/en/coverage-5.5/

## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Yksikkötesteissä on pyritty testaamaan erilaisia käyttäjän antamia syötteitä - sekä oikeita että vääriä - ja varmistamaan, että ohjelma reagoi halutulla tavalla.
* Samoin yksikkötesteissä testataan erilaisia pelitilanteita ja varmistetaan, että algoritmi löytää oikean siirron.
* Yksikkötesteissä heuristiikkaa testataan varmistalla, että pelitilanteen arvostus ("heuristiikkapisteet") on sitä mitä pitääkin.

## Miten testit voidaan toistaa?
* Yksikkötestit voidaan toistaa ajamalla seuraava script Main-kansiossa `./run_all_tests.sh`
* Yksikkötestien kattavuusraportin saa toteutettua ajamalla
  1. Ensin ohjelman raportointityökalun läpi komennolla: `coverage run main.py`
  1. Tämän jälkeen raportin saa tulostettua komennolla: `coverage report -m`


# Suorituskykytestaus

## Ajallinen suorituskyky
* To be done: Kellota tietokone vs. tietokone pelien kestoja eri kokoisilla laudoilla.

## Laadullinen suorituskyky
* To be done: Pelaa 5 pelin turnaus tietokonetta vastaan jokaisella laudalla ja dokumentoi tulokset