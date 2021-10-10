# Yksikkötestaus

## Kattavuusraportti
* Alla yksikkötestien kattavuus viikon 5 jälkeen:
![Screenshot from 2021-10-10 02-29-08](https://user-images.githubusercontent.com/62505549/136676245-b507095a-09d2-4b55-980d-f1c24d8592e8.png)

## Mitä on testattu, miten tämä tehtiin?
* Toteutin yksikkötestauksen Pythonin standardikirjastoon kuuluvalla unittest-kirjastolla: https://docs.python.org/3/library/unittest.html
* Testikattavuusraportti tulee coverage-työkalulla: https://coverage.readthedocs.io/en/coverage-5.5/

## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Yksikkötesteissä on pyritty testaamaan erilaisia käyttäjän antamia syötteitä - sekä oikeita että vääriä - ja varmistamaan, että ohjelma reagoi halutulla tavalla.
* Samoin yksikkötesteissä testataan erilaisia pelitilanteita ja varmistetaan, että algoritmi löytää oikean siirron.
* Yksikkötesteissä heuristiikkaa testataan varmistalla, että pelitilanteen arvostus ("heuristiikkapisteet") on sitä mitä pitääkin.

## Miten testit voidaan toistaa?
* Yksikkötestit suoritetaan ajamalla "Main"-kansiossa komento
```
poetry run invoke test
``` 
* Itse testit löytyvät kansiosta Main/Tests/
* Testikattavuuden voi tarkistaa seuraavilla komennoilla:
```
poetry run invoke coverage
```

# Suorituskykytestaus

## Laadullinen suorituskyky
Hyvä empiirinen suorituskykytesti on pelata algoritmia vastaan ja katsoa miten hyvin se pärjää:
 * Tässä testissä algoritmi pärjää erittäin hyvin. Vaikka olen itse koodannut algoritmin ja heuristiikan, ja tiedän miten se arvottaa tilanteita ja miten sen voi periaatteessa voittaa, en silti pysty yleensä sitä voittamaan. Päinvastoin suurin osa peleistä päätyy tekoälyn voittoon - osa näistä menee tosin käyttöliittymän piikkiin, koska tilanne on välillä hiukan vaikea hahmottaa tekstipohjaisesta käyttöliittymästä.
 * Joka tapauksessa lopputulos on, että minimax-algoritmin ja heuristiikan yhdistelmä toimii oikein hyvin.

## Ajallinen suorituskyky
* Jos tarkastellaan suorituskykyä algoritmin tehokkuuden näkökulmasta, niin nollahypoteesi on Tirakirjan taulukko 2.1, jonka mukaan aikavaatimus O(n!) pystyy käsittelemään tehokkaasti suuruusluokkaa 10 olevan syötteen. Eli siis käytännössä 3x3-kokoisen ristinollaruudukon. Intuitiivisesti tämä tuntuu yllättävän pieneltä.
 * Kun laitan tietokoneen pelaamaan itseään vastaan 3x3-ruudukolla ilman syvyysrajoitinta, on keskimääräinen siirron kesto vielä varsin nopea 70 ms 
 * Mutta jo 5x5-ruudukolla ilman syvyysrajoitinta siirron kesto on niin pitkä, että on jaksa odottaa edes ensimmäisen siirron valmistumista. Ero 3x3 ja 5x5 lautojen välillä on siis yllättävän iso. Tirakirjan taulukko oli oikeassa.
 * Yllättävän iso ero johtuu luonnollisesti siitä, että 
   * 3x3-laudalla permutaatioita on 9! eli 362880
   * 5x5-laudalla permutaatiota 25! eli 15511210043330985984000000
 * Tämän perusteella, jos rajoitan 5x5-laudalla minimax-algoritmin syvyyden neljään kierrokseen, pitäisi sen vielä toimia nopeasti, koska 25 * 24 * 23 * 22 = 303600.
   * Tämä piti paikkaansa. Keskimääräiseksi tietokoneen siirron kestoksi tuli 340 ms. Kesto on pidempi kuin 3x3-laudalla, koska algoritmin pitää ajaa jokaisen polun lopuksi heuristiikkametodit, ja koska pelin edetessä permutaatioiden määrä pienenee hitaammin kuin 3x3-ruudukolla.
 * Samalla logiikalla 7x7-laudalla syvyyttä saa olla maksimissaan 3, koska 49 * 48 * 47 = 110544.
   * Tämäkin piti paikkaansa. Kolmen syvyydellä ja 7x7 laudalla siirron kestoksi tuli 718 ms.
   * Kun taas neljän syvyydellä algoritmi oli jo erittäin hidas.
 * Isommilla laudoilla syvyys pitää rajoittaa kahteen, jotta pelikokemus on mukava, mikä tuntuu yllättävän vähältä, mutta on kuitenkin linjassa O(n!)-aikavaatimuksen ja Tirakirjan taulukon kanssa.
   * Käytännössä päädyin tekemään syvyysrajoittimesta liukuvan siten, että syvyys kasvaa sitä mukaa kun vapaiden ruutujen määrä pienenee. Eli vaikka peli olisi alkanut isolla laudella, voidaan syvyyttä kasvattaa kolmeen siinä vaiheessa, kun vapaita ruutuja on enää 50. Kun vapaita ruutuja on enää 25, voidaan syvyys nostaa neljään. 10 vapaalla ruudulla voidaan Tirakirjan mukaisesti laskea kaikki permutaatiot läpi, eli syvyysrajoitinta ei tarvita.
   * Liukuvan syvyysrajoittimen kanssa tietokoneen siirron keskimääräiseksi kestoksi tulee isoimmalla eli 20x20-laudalla noin 1s 
 * Käytännössä tämä tarkoittaa, että isoilla laudoilla melkein kaikki siirrot tehdään heuristiikan perusteella. Eli hyvä heuristiikka on siis avainroolissa siinä kuinka hyvin tekoäly pelaa.
