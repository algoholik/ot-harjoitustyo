# Vaatimusmäärittely

## Sovelluksen tarkoitus

**MoNoA** -sovelluksen avulla käyttäjä voi koostaa isompia muistiinpanoja _notes_, pienemmistä osatekijöistä _snips_. 
Nämä pienemmät *snipit* voivat olla joko ns. globaaleja (kun päivität yhtä snippiä yhdessä muistiinpanossa
päivittyvät kaikki sen instanssit kaikissa muissakin muistiinpanoissa joissa sitä esiintyy), tai paikallisia
(snipin muokkaus ei vaikuta muualle). 

MoNoA on tehty ajatustyöhön, jossa käytetään toistuvasti samoja pienempiä elementtejä, ja siksi se soveltuu hyvin esimerkiksi tehtävä- ja ostoslistojen tekemiseen, tai vaikkapa koodinpätkien hallinnointiin.


## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_. Myöhemmin sovellukseen saatetaan lisätä joko mahdollisuus suojata yksittäisiä muistiinpanoja salasanalla, tai kokonaan usean käyttäjän mahdollistava _käyttäjätilien hallinta_.


## Käyttöliittymäluonnos

Sovellus koostuu kahdesta eri päänäkymästä:

1. Muokkausnäkymä:
   - noten luominen (TEHTY)
   - noten valinta (TEHTY)
   - noten muokkaus (TEHTY)
     - snipin lisäys muistiinpanoon (TEHTY)
     - snippien järjestyksen muuttaminen (OSIN TEHTY)
     - snipin poisto muistiinpanosta
   - lista noteista (TEHTY)
   - lista snipeistä
   - notes-listan hakutoiminto (TEHTY)
   - snips-listan hakutoiminto

2. Hahmotusnäkymä:
   - lista noteista
   - lista snipeistä
   - mahdollisuus hakea ja lajitella noteja ja snipejä niiden sisällön mukaan


## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi luoda noteseja (TEHTY)
- Käyttäjä voi muuttaa osan noten sisällöstä snipiksi
- Käyttäjä voi lisätä luotuja snippejä osaksi noteja (TEHTY)
- Käyttäjä voi määritellä onko snippetti globaali vai paikallinen


## Jatkokehitysideoita

Perusversion jälkeen MoNoAa voisi jatkokehittää ominaisuuksilla kuten:

- Useita erilaisia snippettejä:
  - Teksti
  - Todo-listaus
  - Laskukaava
  - Dynaaminen linkki (esim. kalenterimerkintään)
- Käyttäjä voisi löytää helposti muita samankaltaisia muistiinpanoja:
  - Muistiinpanot joissa esiintyy eniten samoja snippettejä
  - Muistiinpanot joissa esiintyy eniten samoja sanoja
- Muistiinpanojen exporttaus haluttuun formaattiin: 
  - markdown
  - html
  - pdf
- Salasanasuojatut muistiinpanot
- Mahdollisuus jakaa muistiinpanoja muille käyttäjille
- Jaetut muistiinpanot usean käyttäjän kesken