# FormEngine & MiddlemanManager

Tämä dokumentti kuvaa SHL-järjestelmän orkestraatiokerroksen. Se toimii "liimana", joka sitoo yhteen abstraktit komponentit, liiketoimintadatan ja konkreettiset käyttöliittymäkirjastot.

## 1. Miksi tämä kerros on olemassa? (The "Why")

Perinteisissä sovelluksissa käyttöliittymä (UI) on usein tiukasti kytketty datamalliin. Jos datamalli muuttuu tai UI-kirjasto vaihdetaan, koko koodi rikkoutuu. 

**SHL Engine ratkaisee tämän kolmella periaatteella:**
- **Framework-agnostisuus:** Sama logiikka ohjaa Flet-, PyQt6-, tai Tkinter-sovellusta.
- **Datan eristäminen (Decoupling):** Liiketoimintalogiikan ei tarvitse tietää, onko se näkyvissä tekstikentässä vai dropdown-valikossa.
- **Dynaaminen lokalisointi:** Käyttöliittymä voi vaihtaa kieltä ja taivutusmuotoja lennosta ilman, että syötetty data häviää.



---

## 2. Miten se toimii? (The "How")

### FormEngine: Orkestraattori
`FormEngine` on järjestelmän kapteeni. Se ei itse tiedä, miten nappi piirretään, vaan se ohjaa muita:
1. **Komponenttien luku:** Hakee `SHLComponent`-olion avulla tiedot JSON-skeemasta.
2. **UI-rakentaminen:** Käyttää `UIAdapteria` luomaan oikeat widgetit.
3. **Widget-hallinta:** Pitää kirjaa `widgets`-sanakirjassa siitä, mikä ID vastaa mitäkin UI-instanssia.

### MiddlemanManager: Tiedon kääntäjä
Middlemanit ovat "tulkin" roolissa datan ja UI:n välissä. 
- **Data → UI:** Muuntaa monimutkaisen Python-olion (esim. `User`) merkkijonoksi, jonka tekstikenttä ymmärtää.
- **UI → Data:** Muuntaa käyttäjän syötteen (esim. "Tuomas") takaisin oikeaksi tietotyypiksi tai attribuutiksi.



---

## 3. Keskeiset metodit ja datavirta

| Metodi | Tehtävä | Syyte | Tulos |
| :--- | :--- | :--- | :--- |
| `create_form` | Rakentaa UI-rakenteen | `list[SHLComponent]` | `dict[id, widget]` |
| `fill_form` | Vie datan käyttöliittymään | `data_object` | Päivitetty UI-tila |
| `extract_form_data` | Lukee käyttäjän syötteet | `list[SHLComponent]` | Validisoitu Python-data |
| `refresh_language` | Päivittää lokalisoinnin | `LanguageManager` | Käännetty käyttöliittymä |

---

## 4. Tutkimuksellinen merkitys (The "?? Factor")

Se suurin kysymysmerkki (??), jonka tämä kerros ratkaisee, on **luottamus tekniseen eheyteen**. 

Koska `FormEngine` käyttää `MiddlemanManageria`, voimme vaihtaa käyttöliittymän lennosta (esim. PyQt6 -> Flet) ja sovellus toimii yhä samalla datalla. Tutkimuksessa tämä todistaa, että **semanttinen yhteys** (tarkoitus) on tärkeämpi kuin **tekninen yhteys** (toteutus).

Tämä kerros mahdollistaa myös sen, että `HealerEngine` voi reitittää datan uudelleen, jos alkuperäinen komponentti rikkoutuu, koska `FormEngine` ylläpitää master-listaa komponenttien tarkoituksista.

---

**Seuraava dokumentti:** [Healer & Memory](./healer.md)
