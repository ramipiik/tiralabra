## Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
 * Sovellus käynnistetään ajamalla "Main" -hakemistossa ao. komento    
 ```
 poetry run invoke start
 ``` 
   * Jos et halua käyttää poetrya, voit käynnistää sovelluksen ajamalla "Main" -hakemistossa komennon    
```
python3 main.py
``` 

## Minkä muotoisia syötteitä ohjelma hyväksyy
* Syötteet annetaan tekstimuotoisena.
* Sovellus opastaa syötteiden antamisessa ja myös tarkastaa annetut syötteet

## Missä hakemistossa on ajamiseen tarvittavat testitiedostot.
* Yksikkötestit suoritetaan ajamalla "Main"-kansiossa komento
```
poetry run invoke test
``` 
* Itse testit löytyvät kansiosta Main/Tests/
* Testikattavuuden voi tarkistaa seuraavilla komennoilla:
```
poetry run invoke coverage
```