# Käyttöohje: MoNoA - Modular Notes App (0.5.0)

Sovelluksen viimeisin julkaistu [release](https://github.com/algoholik/modularnotes/releases)
lähdekoodeineen on "Ohjelmistotekniikka Viikko 7" (_Assets_ -> _Source code_).


## Sovelluksen suoritus

Asenna ennen ohjelman käynnistämistä tarvittavat riippuvuudet komennolla:
```
poetry install
```

Sekä tee alustustoimenpiteet komennolla:
```
poetry run invoke build
```

Sovelluksen voi nyt suorittaa komennolla:

```
poetry run invoke start
```

## Aloitusnäkymä

Sovellus käynnistyy suoraan ensisijaiseen käyttönäkymään, ja käyttäjää tervehditään vastikään
luodulla ensimmäisellä tyhjällä notella.

![Ensimmäinen käynnistys](./kuvat/monoa_first_run.png)

## Toiminnot

### Luominen ja muokkaus
- Uusia muistiinpanoja (notes) luodaan vasemman palstan yläreunan "Create Note" -painikkeella.
- Muistiinpanon muodostavia palasia (snips) voidaan luoda auki olevan muistiinpanon sisään
oikean yläkulman "Add Snip" -painikkeella.
- Muistiinpanon otsikkoa voi muokata klikkaamalla ylhäällä keskellä olevaa tekstialuetta.
- Käyttäjä voi etsiä muistiinpanoja syöttämällä vasemman yläkulman "Search notes..." -tekstikenttään
hakusanan jolla vasemman reunan lista muistiinpanoista päivittyy näyttämään hakutulokset. Hakutuloksista
palataan kaikki muistiinpanot näyttävään näkymään hakukentän oikean reunan X-painikkeesta.

![Sisältöä syötettynä](./kuvat/monoa_note_contents.png)

### Tallentaminen
- Kaikki käyttäjän luomat notet ja snipit sekä niihin tehdyt muutokset tallentuvat reaaliajassa automaattisesti.
- Käyttäjä voi exportata auki olevan noten sisällön tekstitiedostoksi painamalla käyttöliittymän oikean yläkulman "Export Note..." -nappia, josta aukeavalla tallennusdialogi-ikkunalla käyttäjä voi määrittää tiedostolle nimen ja sijainnin.

![Export-dialogi](./kuvat/monoa_export_dialog.png)
