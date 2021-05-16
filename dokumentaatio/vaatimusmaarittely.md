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

Sovellus koostuu yhdestä päänäkymästä sekä yhdestä dialogi-näkymästä:

Päänäkymä:
- noten luominen (VALMIS)
- noten valinta (VALMIS)
- noten muokkaus (VALMIS)
  - snipin lisäys muistiinpanoon (VALMIS)
  - snippien järjestyksen muuttaminen (OSITTAIN VALMIS)
  - snipin poisto muistiinpanosta (PUUTTUU)
- lista noteista (VALMIS)
- lista snipeistä (PUUTTUU)
- notes-listan hakutoiminto (VALMIS)
- snips-listan hakutoiminto (PUUTTUU)

Dialogi-näkymä:
- käyttäjä voi valita kohdepolun mihin note exportataan


## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi luoda noteseja (VALMIS)
- Käyttäjä voi määrittää notelle otsikon (VALMIS)
- Käyttäjä voi luoda noten sisälle snippejä (VALMIS)
- Käyttäjä voi etsiä noteja
- Käyttäjä voi exporttaa noten sisältöineen (snipit) tekstitiedostoksi
- Käyttäjä voi määritellä onko snippetti globaali vai paikallinen (PUUTTUU)


## Jatkokehitysideoita

Perusversion jälkeen MoNoAa tullaan jatkokehittämään mm. näillä ominaisuuksilla:

- Käyttäjä voi lisätä jo luotuja snippejä noten sisään
- Snippejä voi vaihtaa "lennosta" noten sisältä toiseksi snipiksi
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
- Käyttäjänhallinta
- Salasanasuojatut muistiinpanot
- Mahdollisuus jakaa muistiinpanoja muille käyttäjille
- Jaetut muistiinpanot usean käyttäjän kesken
