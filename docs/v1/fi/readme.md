# SHL (Semantic Healer Layer) - Arkkitehtuurisynteesi 2026

SHL on **semanttinen välikerros**, joka erottaa sovelluksen tarkoituksen (Intent) sen teknisestä toteutuksesta (Implementation). Se mahdollistaa käyttöliittymien automaattisen korjautumisen (Self-Healing) ja täydellisen framework-agnostisuuden.

## 🏗️ 1. Kerrosarkkitehtuuri

Järjestelmä jakautuu neljään pääasialliseen vastuualueeseen:

| Kerros | Komponentit | Tehtävä |
| :--- | :--- | :--- |
| **Semanttinen Rekisteri** | `ui_schema.json`, `SHLComponent` | Määrittää komponenttien "DNA:n": tyypit, kieliavaimet ja tekniset vastineet. |
| **Orkestraatio (Engine)** | `FormEngine`, `MiddlemanManager` | Ohjaa tiedonkulkua datamallien ja käyttöliittymän välillä. |
| **Adapterit & Havainnointi** | `UIAdapters`, `UITreeBuilders` | Renderöi widgetit (Flet, PyQt6, Tkinter) ja lukee ruudun tilan (Playwright). |
| **Itseparannus (Healer)** | `HealerEngine`, `Memory`, `Logger` | Havaitsee tekniset rikkoutumiset ja korjaa ne heuristiikan avulla. |

---

## 🔄 2. Keskeiset datavirrat

### A. Renderöintisykli (The Render Flow)
1. **Määrittely:** `FormEngine` hakee komponentin tiedot `SHLComponent`-luokan kautta JSON-skeemasta.
2. **Luonti:** `UIAdapter` muuntaa abstraktin määrittelyn framework-kohtaiseksi widgetiksi (esim. `QLineEdit` tai `TextField`).
3. **Sidonta:** `MiddlemanManager` muuntaa raakadatan (esim. `User`-objekti) UI-komponentille sopivaan muotoon.
4. **Lokalisointi:** `LanguageManager` hakee termit huomioiden kielelliset säännöt (vokaalisointu).



### B. Itseparannussykli (The Healing Cycle)
Prosessi noudattaa kaavaa: **Lookup → Diff → Heal Attempt → Resolution → Patch**.
1. **Lookup:** `UITreeBuilder` rakentaa reaaliaikaisen `UINode`-puun käyttöliittymästä.
2. **Diff:** Järjestelmä havaitsee, ettei komponenttia löydy rekisteröidyn ID:n tai selektorin perusteella.
3. **Heal Attempt:** `HealerEngine` suorittaa ML-avusteisen haun käyttäen kolmea heuristiikkaa:
    * **Text:** Täsmääkö ruudun teksti kielitiedoston käännökseen (huomioiden taivutukset)?
    * **Type:** Onko widgetin tekninen tyyppi oikea?
    * **Context:** Täsmääkö komponentin data-binding (esim. `user.email`).
4. **Learning:** `HealerMemory` päivittää metodien luottamusarvot (Confidence) onnistumisten perusteella.
5. **Resolution:** `HealerLogger` dokumentoi muutoksen auditointia ja automaattista korjausta (Patch) varten.



---

## 🧠 3. Kielellinen äly (Grammatical Engine)

`LanguageManager` ei ole pelkkä JSON-pohjainen käännöstyökalu, vaan se sisältää suomen kielelle kriittistä logiikkaa:
* **Vowel Harmony & Gradation:** Mahdollistaa sen, että Healer tunnistaa sanan "Pankissa" vastaavan avainta "pankki", vaikka muoto on muuttunut.
* **User Keys:** Järjestelmä priorisoi käyttäjän itse luomaa "avainkieltä" (esim. osoitteiden nimeäminen) tunnistuksen tueksi.

---

## 🛠️ 4. Tekniikkapino

* **Kieli:** Python 3.10+
* **UI-Frameworkit:** Flet (Flutter), PyQt6, Tkinter, Streamlit
* **Testaus/Web-luku:** Playwright
* **Tallennus:** JSON (Skeemat, lokit, muisti)

---

## 📈 5. Analytiikka ja Oppiminen

`HealerStats`-komponentti tarjoaa näkyvyyden järjestelmän suorituskykyyn:
- **Accuracy:** Onnistumisprosentti per heuristiikka.
- **Selector Evolution:** Historia siitä, miten komponenttien selektorit ovat muuttuneet ja kehittyneet sovelluksen elinkaaren aikana.

---

# 6. SHL Documentation Tree (V1)

```text
docs/
└── v1/
    └── fi/
        ├── README.md                 # Projektin visio ja johdanto
        ├── SUMMARY.md                # Navigointi ja sisällysluettelo
        ├── vocabulary.md             # Keskeinen sanasto
        │
        ├── architecture/             # Järjestelmän tekninen rakenne
        │   ├── engine.md             # FormEngine & MiddlemanManager
        │   ├── healer.md             # HealerEngine & Memory
        │   ├── adapters.md           # UI Adapters & Tree Builders
        │   ├── grammar_rules.md      # Kielioppisäännöt (Teoria)
        │   ├── morphology_engine.md  # Normalisointi (Tekniikka)
        │   └── middleman_logic.md    # Semanttinen datan käsittely
        │
        ├── data/                     # Skeemat ja tallennusmuodot
        │   ├── ui_schema.md          # JSON-komponenttien määrittely
        │   ├── localization.md       # JSON & .PO -logiikka
        │   └── healer_data.md        # Lokien ja muistin arkistointi
        │
        └── research/                 # Tutkimus- ja testiskenaariot
            ├── test_scenarios.md     # Käytännön testitapaukset
            └── stats_analysis.md     # Suorituskykymittarit
```
