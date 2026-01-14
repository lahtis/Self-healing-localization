# Osa 9 – Kerrosmallin selitys esimerkin kautta

Kerrosmalli on helpointa ymmärtää konkreettisen esimerkin kautta.  
Tässä kuvataan, mitä tapahtuu, kun sovellus haluaa näyttää yksinkertaisen tekstikentän:

**“Kirjoita viesti…”**

Tämä esimerkki kulkee läpi koko SHL frameworkin arkkitehtuurin ylhäältä alas.

---

## 1. UI-kerros – Kehittäjä pyytää tekstikenttää

Kehittäjä kirjoittaa:

```python
TextField(label=loc.L("input_label", "Kirjoita viesti..."))
```
UI ei tiedä mitään semantiikasta.
Se vain pyytää: “Tarvitsen tekstikentän, jonka `label` on tämä.”

UI ei tee muuta.

---

## 2. Adapteri-kerros – Muuntaa pyynnön semantiikaksi
Adapteri ottaa UI:n pyynnön ja muuntaa sen semanttiseksi rakenteeksi:

```json
{
  "type": "text_input",
  "semantic_key": "input_label",
  "default": "Kirjoita viesti..."
}
```
Adapteri ei päätä, mitä teksti tarkoittaa.
Se vain muuntaa UI:n pyynnön SHL:n sisäiseen muotoon.

---

## 3. Semanttinen rekisteri – Mitä tämä elementti tarkoittaa?
Semanttinen rekisteri tarkistaa:
* onko input_label jo määritelty
* mikä on sen tarkoitus
* mihin kontekstiin se kuuluu
* onko sillä erityisiä sääntöjä
Jos rekisterissä ei ole merkintää, se luo uuden:

```python
input_label:
  type: text
  context: message_input
  description: "Label for the main message input field"
```
Tämä on ensimmäinen hetki, jolloin järjestelmä ymmärtää merkityksen.

---

## 4. Healing-kerros – Puuttuvien tietojen täydentäminen
Healing-kerros tarkistaa:
* löytyykö käännös JSON-tiedostosta
* löytyykö semanttinen kuvaus
* löytyykö oletusarvo
* löytyykö rakenne UI:lle
Jos jotain puuttuu, healing täydentää sen automaattisesti:
* lisää puuttuvan avaimen JSONiin
* luo oletusarvon
* tallentaa semanttisen kuvauksen
* varmistaa, että UI saa toimivan rakenteen
Healing ei pysähdy virheeseen — se parantaa tilanteen.

---

## 5. Data / Persistence – Tallennus
Healingin jälkeen järjestelmä tallentaa:
* uuden avaimen JSON-kielitiedostoon
* semanttisen rekisterin päivityksen
* mahdolliset uudet oletusarvot
* muutokset tietokantaan (jos käytössä)

Esimerkiksi JSON-tiedostoon syntyy:

```json
{
  "input_label": "Kirjoita viesti..."
}
```

---

## 6. Ydinlogiikka – Sovellus käyttää semantiikkaa
Ydinlogiikka ei näe UI:ta eikä JSON-tiedostoja.
Se näkee vain:

```python
semantic_key = "input_label"
value = "Kirjoita viesti..."
```

Ydinlogiikka voi käyttää tätä:
* validointiin
* lokitukseen
* analytiikkaan
* AI‑rajapintaan
* tai muihin toimintoihin
Ilman että se tietää mitään käyttöliittymästä.

---

## 7. Paluu UI:hin – Lopullinen komponentti
Kun kaikki kerrokset ovat tehneet työnsä, UI saa takaisin valmiin komponentin:

```python
TextField(label="Kirjoita viesti...")
```

UI näyttää sen käyttäjälle.
Kaikki muu tapahtui taustalla.

# Yhteenveto esimerkin kulusta
```text
| Kerros                | Mitä tapahtuu?                     |
|-----------------------|------------------------------------|
| UI                    | Pyytää tekstikenttää               |
| Adapteri              | Muuntaa pyynnön semantiikaksi      |
| Semanttinen rekisteri | Määrittelee merkityksen            |
| Healing               | Täydentää puuttuvat tiedot         |
| Data                  | Tallentaa muutokset                |
| Ydinlogiikka          | Käyttää semanttista arvoa          |
| UI (lopuksi)          | Näyttää valmiin komponentin        |
```

---

# Miksi tämä esimerkki on tärkeä?
Koska se näyttää, että SHL framework ei ole vain tekninen rakenne.
Se on ajattelutapa, jossa:

UI ei kanna vastuuta semantiikasta
* semantiikka ei ole sidottu UI:hin
* healing korjaa puutteet automaattisesti
* data pysyy eheänä
* ydinlogiikka pysyy puhtaana
* ja koko järjestelmä toimii kerroksittain, ei sekavana kokonaisuutena
Tämä esimerkki on SHL:n filosofia käytännössä.


---
