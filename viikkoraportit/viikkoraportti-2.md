## Mitä olen tehnyt tällä viikolla?
* tietomallien luontia. Minimax-algoritmin luonnostelua.
* käyttöliittymä
* alpha-beta-karsinta
* eri kokoiset ruudukot
* 0, 1 ja 2 pelaajan versiot
* eri tasoiset tekoälyt
* syvyysrajoitin (dummy-heuristiikalla)

## Miten ohjelma on edistynyt?
* Ihan ok. Aikaa on tosin mennyt enemmän kuin mitä oletin

## Mitä opin tällä viikolla / tänään?
* Minimax-algoritmin toteuttaminen
* Alpha-beta-karsinnnan toteuttaminen

## Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.
* Käytin tosi paljon aikaa siihen, että saisin algoritmin tekemään "fiksun näköisiä" päätöksiä.
 * Minimax-algoritmi valitsee nimittäin ensimmäisen parhaan vaihtoehdon, jonka onnistuu löytämään. Tämä vaikuttaa ihmiselle hieman erikoiselta, koska usein voitto voisi olla 1 tai 2 siirron päässä, mutta algoritmi lähtee hakemaan 4 siirron "mattia", koska  se tulee syvyyshaun polulla ensin vastaan. Onnistuinkin tässä siten, että jos kahden vaihtoehdon arvo on sama, valitsee algoritmi näistä lyhyemmän polun, jos se on voittamassa. Tai pidemmän polun jos se on häviämässä.   
 * Yo. lisäys toimii ihan hyvin ilman alpha-beta-karsintaa, mutta monen tunnin ihmettelyn jälkeen tajusin, että alpha-beta-karsinnalla se ei toimi, koska se jättää joka tapauksessa osan poluista käymättä eikä siksi välttämättä löydä ihmiselle ilmiselviä ratkaisuita
 * Leveyshaku olisi sikäli parempi, että se löytäisi ensin lyhyemmät polut. Mutta toisaalta sillä menisi erittäin kauan käydä kaikki vaihtoehdot läpi. 
 * Heuristiikka on on vielä kokonaan toteuttamatta. Katsotaan, jos sieltä aukenisi joku ratkaisu "tyhmän näköisiin" siirtoihin. Sinänsä algoritmi kyllä toimii nytkin, koska se ajaa kohta löytämäänsä parasta ratkaisua. Ratkaisut eivät vaan näytä aina kovin intuitiivilta
* Algoritmi on tällä hetkellä yllättävän hidas yli 3x3-ruudukoilla vaikka siinä on alpha-beta-karsinta implementoitu. Oikea heuristiikka tulee varmaan auttamaan tässä.

## Mitä teen seuraavaksi?
* Heuristiikka
* Nopeuden optimointia
* Koodin siistimistä (tällä hetkellä se on aivan jäätävää sekasotkua - ei kannata katsoa)
* Testaus ja linttaus on vielä ihan auki. En ole edes ehtinyt vielä tutustua Pythonin kirjastoihin.
