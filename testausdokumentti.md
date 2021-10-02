# Yksikkötestaus

## Kattavuusraportti
* Alla status viikon 4 lopuksi

Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
Heuristics/basic_check.py          112     22    80%   8-13, 16-32, 70, 72
Heuristics/boundaries_check.py      13      0   100%
Heuristics/closeness_check.py       41      5    88%   17-24
Heuristics/mustwin_check.py         73     11    85%   11-12, 15-16, 23, 25, 40, 52, 82, 101, 123
Heuristics/prevent_mustwins.py      78      9    88%   11-16, 29, 86, 105
Heuristics/run_heuristics.py        50      8    84%   21, 36-38, 51, 56, 74-75
Heuristics/sanity_check.py          91     21    77%   8-15, 18-28, 47, 49, 64, 90, 106, 125, 147
Start/board.py                      52     24    54%   21-22, 25-28, 30-33, 35-38, 40-43, 45-48, 55-56
Start/confirm.py                    14      4    71%   14-19
Start/first_move.py                 28      8    71%   19-21, 27-31
Start/level.py                      26      5    81%   28-32
Start/players.py                    23      5    78%   17-18, 23-25
Start/recap.py                      16      2    88%   8, 13
Start/start.py                      25      0   100%
alphabeta.py                        40     21    48%   11, 18-34, 48-54
main.py                             16      1    94%   16
parameters.py                       23      5    78%   13, 15, 17, 24, 32
play.py                             97     17    82%   21-23, 26, 37-40, 47, 60-64, 79, 107, 111
tictactoe.py                       108      9    92%   49, 57, 78, 93, 110, 139, 155-157
--------------------------------------------------------------
TOTAL                              926    177    81%


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