# UI Adapters & Tree Builders

Tämä dokumentti kuvaa SHL-järjestelmän sensorisen ja motorisen kerroksen. Adapterit vastaavat siitä, että abstraktit komponentit muuttuvat fyysisiksi widgeteiksi, ja Tree Builderit lukevat näiden widgetien tilan takaisin järjestelmään.

## 1. UI Adapterit: Järjestelmän "Kädet"

UI Adapterin tehtävä on abstrahoida eri käyttöliittymäkirjastojen (Flet, PyQt6, Tkinter) väliset erot. Se tarjoaa yhtenäisen rajapinnan, jota `FormEngine` voi kutsua välittämättä siitä, mikä teknologia alla on.



### Adapterin vastuualueet:
- **Widgetin luonti:** Muuntaa `SHLComponent`-määritelmän framework-kohtaiseksi olioksi (esim. `ft.TextField` tai `QLineEdit`).
- **Ominaisuuksien mappaus:** Määrittää, miten teksti, placeholder tai tooltip asetetaan kussakin kirjastossa.
- **Kielen päivitys:** Päivittää widgetin tekstisisällön lennosta, kun kieli vaihtuu.

### Tuetut adapterit (V1):
| Framework | Luokka | Erityisominaisuudet |
| :--- | :--- | :--- |
| **Flet** | `FletAdapter` | Cross-platform (Flutter), tukee dynaamista Labelia ja Placeholdereita. |
| **PyQt6** | `PyQt6Adapter` | Natiivi työpöytäsovellus, rikas ominaisuusjoukko (tooltipit jne.). |
| **Tkinter** | `TkinterAdapter` | Kevyt ja universaali, rajalliset tyylittelyominaisuudet. |

---

## 2. UI Tree Builders: Järjestelmän "Silmät"

Tree Builder on adapterin vastinpari. Kun adapteri *luo* jotain, Tree Builder *lukee* mitä on jo olemassa. Tämä on elintärkeää itseparannukselle (Self-Healing).



### Tree Builderin toimintaperiaate:
1. **Skannaus:** Käy läpi sovelluksen aktiivisen käyttöliittymän (esim. Flet-sivun tai Playwright-selainikkunan).
2. **Normalisointi:** Muuttaa framework-kohtaiset widgetit yleisiksi `UINode`-olioiksi.
3. **Attribuuttien keruu:** Tallentaa jokaisesta nodesta tyypin, tekstin, selektorin ja sijainnin.

Tämä normalisoitu puu syötetään `HealerEngine`-moottorille, joka vertaa sitä alkuperäiseen skeemaan.

---

## 3. Playwright ja Web-automaatio

Web-ympäristössä adapteri ja builder toimivat Playwright-kirjaston päällä. 
- **Adapteri** käyttää Playwrightin `locator`-rajapintaa toimintojen suorittamiseen.
- **Tree Builder** käyttää JavaScript-pohjaista skannausta rakentaakseen DOM-puusta SHL-yhteensopivan näkymän.

Tämä mahdollistaa sen, että samat Healer-logiikat toimivat sekä työpöytäsovelluksissa että monimutkaisissa verkkosivuissa.

---

## 4. Tutkimuksellinen merkitys: Framework Agnosticism

Tämä kerros todistaa tutkimuksessa, että **sovelluksen liiketoimintalogiikka on siirrettävissä**. 

Koska adapteri-kerros erottaa UI-toteutuksen, voimme todentaa, että Healer-moottori kykenee korjaamaan virheitä riippumatta siitä, tapahtuuko virhe Windows-sovelluksessa vai selaimessa. Tämä poistaa perinteisen "testien ylläpitotaakan", jossa jokaiselle frameworkille on kirjoitettava omat säännöstöt.

---

**Seuraava dokumentti:** [Linguistics & Grammar Rules](./grammar_rules.md)
