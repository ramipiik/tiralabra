## Ohjelmointikieli
* Oman työni aion toteuttaa Pythonilla
* Voin antaa palautetta myös Javalla tai Javascriptillä/Nodella tehdyistä työstä

## Dokumentaation kieli
* Suomi

## Alustavat algoritmit ja tietorakenteet
_Suunnitelma on alustava. Itselleni käy usein niin, että ohjelmaa oikeasti koodatessa huomaa, että alkuperäinen ajatus ei ollutkaan niin hyvä. Lisäksi työmäärän arvioiminen on hieman haastavaa etukäteen. _
* Aion toteuttaa syvyysrajoitetun minimimax-algoritmin alpha-beta-karsinnalla ristinolla-peliin
* En ole aiemmin toteuttanut minimax-algoritmia. Tietorakenteiden puolesta tarvitaan ainakin listoja. Tarkennan tätä kunhan saan jonkinlaisen koodirungon aikaiseksi ja ymmärrän paremmin mitä pelitilanteen ylläpitäminen algoritmin toteuttaminen vaatii. 

## Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?
* Suunnitelma on tehdä ristinollapeli jota voi pelata a) ihminen vs. ihminen, b) ihminen vs. tekoäly c) tekoäly vs. tekoäly
* Peliä voi pelata erikokoisilla ruudukoilla (alustavasti esim. 3x3, 5x5, 7x7, 10x10, 15x15 ja 20x20)
* 3x3-ruudukolla voittoon vaaditaan kolme peräkkäistä merkkiä. Isommilla ruudukoilla voittoon vaaditaan neljä peräkkäistä merkkiä.
* Koska tällä kurssilla pääfokus on algoritmin luomisessa teen ensin tekstipohjaisen käyttöliittymän. Tavoite on kuitenkin tehdä myös graafinen web-pohjainen käyttöliittymä (joko tämän projektin puitteissa tai myöhemmin)
* Ratkaistava ongelma on optimaalisen siirron valitseminen tekoälyn näkökulmasta
* Valitisin minimax-algoritmin, koska se soveltuu hyvin täydellisen informaation kahden pelaajan peleihin.
* Alpha-beta-karsinta taas on helppo tapa tehostaa minimax-algoritmin toimintaa 
* Syvyysrajoituksen valitsin, koska sen ansiosta peliä voidaan pelata myös mielivaltaisen isoilla laudoilla. Pieniin lautoihin sitä ei tarvita. En osaa sanoa, minkä kokoisessa laudassa syvyyrajoitusta käytännössä tarvitsee, mutta se selvitää kokeilemalla
* Olisi hauskaa toteuttaa myös eri tasoisia tekoälyjä esim. siten, että taso 0 katsoo vain yhden siirron eteenpäin, taso 1 katsoo kaksi siirtoa eteenpäin, taso 2 katsoo kolme siirtoa eteenpäin jne. Taso 5 laskee koko ruudukon läpi tarvittaessa syvyysrajoitinta käyttäen 


## Mitä syötteitä ohjelma saa ja miten näitä käytetään?
Syötteet ennen pelin alkua:
* Pelitapa: a) ihminen vs. ihminen, b) ihminen vs. tekoäly c) tekoäly vs. tekoäly
* Ruudukon koko: 3x3, 5x5, 7x7, 10x10, 15x15 ja 20x20
* Tekoälyn taso: 0-5

Syötteet pelin aikana: 
* Ihmispelaajan siirrot

## Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)
* 

## Lähteet
* Johdatus tekoälyyn -kurssin materiaali: https://materiaalit.github.io/intro-to-ai/
* Tietorakenteet ja algoritmin -kurssin materiaali: https://github.com/hy-tira/tirakirja/

## Opinto-ohjelma
* Tietojenkäsittelytieteen kandidaatti (TKT)
