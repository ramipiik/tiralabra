## Ohjelman yleisrakenne
* Kaikki lähdekoodi on "Main" -kansiossa
* Main-kansion juuressa on seuraavat tiedostot:
  * alphabeta.py: Minimax-algoritmi alpha-beta-karsinnalla
  * main.py: käynnistää ohjelman suorituksen
  * parameters.py: Oletukset ja magic numberit, joilla voi viilata algoritmin toimintaa
  * play.py: Käynnistää joko tietokoneen tai ihmispelaajan vuoron ja kutsuu tarvittavia metodeja
  * run_all_tests.sh: Script, joka ajaa kaikki yksikkötestit
  * tictactoe.py: Luokka, josta luodaan pelilautaoliot
* Heuristiikkatarkastukset ovat alikansiossa "Heuristics". Näitä käytetään pelitilanteen arviointiin, jos laudalla on paljon tilaa ja minimax-algoritmi haarautuu niin paljon, että sitä ei kannata suorittaa loppuun asti. 
* Kaikki yksikkötestit ovat kansiossa "Tests"
* Käynnistysvaiheen tekstikäyttöliittymämetodit löytyvät kansiosta "Start".

## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
Toteutetun algoritmin pseudokoodi on alla. Algoritmi käy läpi pelitilanteen kaikki mahdolliset permutaatiot. Se tarkoittaa, että aikavaatimus on O(n!), jossa n on pelilaudan koko. Sama pätee tilavaatimukseen - eli se on myös O(n!).

Valitettavasti aikavaatimuksen suuruusluokkaa ei ymmärtääkseni ole mahdollista parantaa. Siitä ei pääse yli eikä ympäri, että permutaatiot on vaan käytävä läpi, jotta löydetään paras siirto ja sitä seuraava paras siirto jne. Jos johonkin tilaan liittyvä optimaalinen siirto on jo löytynyt, niin tällöin alpha-beta-karsinta toki karsii turhat haarat pois, mikä toki nopeuttaa käytännön suoritusta. Mutta suuruusluokka on silti edelleen O(n!)

  ```
  play(node):
    if node.max_turn:
      value=-LARGE_NUMBER
      new_state=""
      for each child in node.children():
        v=alpha_beta_value(child)
        if v>value:
          value=v
          new_state=child
    if node.min_turn:
      # same as above, but minimize value instead of maximizing
    return new_state
  ```

  ```
  alpha_beta_value(node):
    if node.max_turn:
        value = max_value(node)
    else:
        value = min_value(node)
    return value
  ```
  
  ```
  max_value(node):   
    if end_state(node):
      return value(node
    if max_depth(node):
      return heuristics(node)  

    v = -LARGE_NUMBER  
    for each child in node.children():  
      v = max(v, min_value(child))  
    return v
  ```  

  ```
  min_value(node):
    if end_state(node):
      return value(node)
    if max_depth(node):
      return heuristics(node)  
    
    v = LARGE_NUMBER
    for each child in node.children():
      v = min(v, max_value(child))
    return v
  ```

## Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)
 * Ks. testausdokumentti.

## Työn mahdolliset puutteet ja parannusehdotukset
 * Mielestäni on edelleen intuitiivisesti erittäin outoa, että O(n!)-aikavaatimuksen vuoksi algoritmi ei pysty pelaamaan kahta siirtoa syvemmälle. Tämä oli itselleni isoin yllätys, vaikka onkin toki linjassa Tirakirjan taulukon kanssa. Onneksi heuristiikka toimii sen verran hyvin, että algoritmiä on silti erittäin vaikea voittaa.
 * Ohjaajan viikon 2 palautteella kokeilin jossain vaiheessa muutosta, jossa uusia siirtoja ei etsitä koko laudalta, vaan ainoastaan edellisen siirron läheltä. Idea on erittäin hyvä, mutta käytännössä se ei auttanut - tai sitten toteutuksessani oli jotain vikaa. Tämä siksi, että  tarkasteltavan ikkunan koon pitää olla neljä ruutua joka suuntaan eli 9x9=81 ruutua. Tämä on edelleen hyvin kaukana kymmenestä, jolla pystyy laskemaan kaikki permutaatiot läpi. Lisäksi siitä tuli ikäviä sivuoireita, sillä tässä versiossa pelin painopisteen pystyi vedättämään eri puolelle lautaa, jos joutui pulaan yhdellä rintamalla. Näin ollen päädyin poistamaan tämän main-branchista.
 * Uskon silti edelleen, että tähän löytyy joku ratkaisu - ristinolla on niin yksinkertainen peli, että on oltava mahdollista katsoa yli kahden siirron päähän.
 * Graafinen käyttöliittymä olisi iso parannus, mutta se on selkeästi laajuuden ulkopuolella. Ja olen pian käyttänyt kurssiin opintopisteiden mukaiset tunnit, joten se jää seuraavaan kertaan.

## Lähteet
* Johdatus tekoälyyn -kurssin materiaali: https://materiaalit.github.io/intro-to-ai/
* Tira-kirja eli tietorakenteet ja algoritmin -kurssin materiaali: https://github.com/hy-tira/tirakirja/