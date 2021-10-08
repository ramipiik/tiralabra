## Ohjelmointikieli
* Oman työni aion toteuttaa Pythonilla
* Voin antaa palautetta myös Javalla tai Javascriptillä/Nodella tehdyistä työstä

## Dokumentaation kieli
* Suomi

## Alustavat algoritmit ja tietorakenteet
_Suunnitelma on alustava. Itselleni käy usein niin, että ohjelmaa oikeasti koodatessa huomaa, että alkuperäinen ajatus ei ollutkaan niin hyvä. Lisäksi työmäärän arvioiminen on hieman haastavaa etukäteen. _
* Aion toteuttaa syvyysrajoitetun minimimax-algoritmin alpha-beta-karsinnalla ristinolla-peliin
* En ole aiemmin toteuttanut minimax-algoritmia, enkä ristinollaa, mutta näin suunnitteluvaiheessa uskoisin, että tietorakenteeksi käy hyvin kaksi sisäkkäistä Pythonin listaa eli siis matriisi. Jokaisen rekursiokutsun pitää kuljettaa mukaan ruudukon tilanne tuossa listassa sekä tieto siitä mikä on ko. tilan arvo (-1, 0, 1), jonka voi luonnollisesti tallentaa ihan normaaliin muuttujaan. Voi olla, että missaan jotakin, mutta tarkennan tätä kunhan saan jonkinlaisen koodirungon aikaiseksi ja ymmärrän paremmin mitä algoritmin toteuttaminen vaatii. 

## Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?
* Suunnitelma on tehdä ristinollapeli jota voi pelata a) ihminen vs. ihminen, b) ihminen vs. tekoäly c) tekoäly vs. tekoäly
* Peliä voi pelata erikokoisilla ruudukoilla (alustavasti esim. 3x3, 5x5, 7x7, 10x10, 15x15 ja 20x20). Mielenkiintoista nähdä miten tekoäly selviää isommista ruudukoista. 
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
* Mielestäni aikavaativuuden suuruusluokaksi tulee O(n!), missä n on ruutujen määrä, koska algoritmin pitää käydä läpi kaikki mahdolliset kombinaatiot ja valita niistä paras. Eli esim. 3x3-ruudukossa aikavaatimus olisi O(3!)=O(9). Tätä voi nopeuttaa alpha-beta-karsinnalla. Ja tarvittaessa katkaista syvyysrajoituksella.
* Tira-kirjan taulukon 2.1 perusteella O(n!)-aikavaatimuksen algoritmi selviää nopeasti suuruusluokkaa 10 olevista syötteistä. Eli 3x3-ruudukon pitäisi mennä sujuvasti, mutta 5x5 ruudukko ei enää menisi nopeasti. Itse uskoisin, että alpha-beta-karsinta nopeuttaa algoritmia sen verran, että 5x5 ruudukko menee vielä sujuvasti. Mielenkiintoista nähdä miten se menee, ja mihin kohtaan syvyysrajoitin pitää asettaa.
* Samoin tilavaativuuden suuruusluokaksi tulee O(n!). Logiikka on sama kuin edellä, eli jokaiseen kombinaatioon liittyy tila (tai rekursiokutsu), joka täytyy pitää muistissa.
* Käytännössä algoritmin käyttämä muisti tuskin tulee muodostumaan ongelmaksi. Uskoisin, että pullonkaula tulee olemaan aikavaatimus eli tekoälyn miettimisaika. Alustava tavoite on, että laskenta saa kestää maksimissaan yhden sekunnin. Jos se kestää kauemmin, pitää käyttää syvyysrajoitinta. 

## Lähteet
* Johdatus tekoälyyn -kurssin materiaali: https://materiaalit.github.io/intro-to-ai/
* Tira-kirja eli tietorakenteet ja algoritmin -kurssin materiaali: https://github.com/hy-tira/tirakirja/

## Opinto-ohjelma
* Tietojenkäsittelytieteen kandidaatti (TKT)
