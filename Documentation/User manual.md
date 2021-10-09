## Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
 * Sovellus käynnistetään ajamalla komento `python3 main.py` "Main" -hakemistossa

## Minkä muotoisia syötteitä ohjelma hyväksyy
* Syötteet annetaan tekstimuotoisena.
* Sovellus opastaa syötteiden antamisessa ja myös tarkastaa annetut syötteet

## Missä hakemistossa on ajamiseen tarvittavat testitiedostot.
* Yksikkötestit ajetaan suorittamalla seuraava script Main-kansiossa `./run_all_tests.sh`
* Itse testit löytyvät kansiosta Main/Tests/
* Testikattavuuden voi tarkistaa seuraavilla komennoilla:
```
 pip install coverage
 ```
 ```
 coverage run main.py
 ```  
 ```
 coverage report -m
 ```