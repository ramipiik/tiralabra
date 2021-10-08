## Ohjelman yleisrakenne
* Kaikki lähdekoodi on "Main" -kansiossa
* Main-kansion juuressa on seuraavat tiedostot:
  * alphabeta.py: Minimmax-algoritmi alpha-beta-karsinnalla
  * main.py: käynnistää ohjelman suorituksen
  * parameters.py: Oletukset ja magic numberit, joilla voi viilata algoritmin toimintaa
  * play.py: Käynnistää joko tietokoneen tai ihmispelaajan vuoron ja kutsuu tarvittavia metodeja
  * run_all_tests.sh: Script, joka ajaa kaikki yksikkötestit
  * tictactoe.py: Luokka, josta luodaan pelilautaoliot
* Heuristiikkatarkastukset ovat alikansiossa "Heuristics". Näitä käytetään pelitilanteen arviointiin, jos laudalla on paljon tilaa ja minimax-algoritmi haarautuu niin paljon, että sitä ei kannata suorittaa loppuun asti. 
* Kaikki yksikkötestit ovat kansiossa "Tests"
* Käynnistysvaiheen tekstikäyttöliittymämetodit löytyvät kansiosta "Start".


## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
 * To be done

## Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)
 * To be done

## Työn mahdolliset puutteet ja parannusehdotukset
 * To be done

## Lähteet
* Johdatus tekoälyyn -kurssin materiaali: https://materiaalit.github.io/intro-to-ai/
* Tira-kirja eli tietorakenteet ja algoritmin -kurssin materiaali: https://github.com/hy-tira/tirakirja/