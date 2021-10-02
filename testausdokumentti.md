# Yksikkötestaus

## Kattavuusraportti
* Alla status viikon 4 lopuksi
![Test coverage image]
(https://github.com/ramipiik/tiralabra/blob/main/Test%20coverage%202021-10-03.png)


## Mitä on testattu, miten tämä tehtiin?
* Toteutin yksikkötestauksen Pythonin standardikirjastoon kuuluvalla unittest-kirjastolla: https://docs.python.org/3/library/unittest.html
* Testikattavuusraportti tulee coverage-työkalulla: https://coverage.readthedocs.io/en/coverage-5.5/

## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Yksikkötesteissä on pyritty testaamaan erilaisia käyttäjän antamia syötteitä - sekä oikeita että vääriä - ja varmistamaan, että ohjelma reagoi halutulla tavalla.
* Samoin yksikkötesteissä testataan erilaisia pelitilanteita ja varmistetaan, että algoritmi löytää oikean siirron.
* Yksikkötesteissä heuristiikkaa testataan varmistalla, että pelitilanteen arvostus ("heuristiikkapisteet") on sitä mitä pitääkin.

## Miten testit voidaan toistaa?
* Yksikkötestit voidaan toistaa ajamalla seuraava script Main-kansiossa `<./run_all_tests.sh>`
* Yksikkötestien kattavuusraportin saa toteutettua ajamalla
1. Ensin ohjelman raportointityökalun läpi komennolla: "coverage run main.py"
2. Tämän jälkeen raportin saa tulostettua komennolla: "coverage report -m"


# Suorituskykytestaus
Ei vielä aloitettu...

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
*