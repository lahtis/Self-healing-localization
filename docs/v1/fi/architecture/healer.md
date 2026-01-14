# HealerEngine, Memory & Stats

Tämä dokumentti kuvaa SHL-järjestelmän "älykerroksen". Healer-kokonaisuus vastaa virhetilanteiden tunnistamisesta, automaattisesta korjaamisesta ja kokemuspohjaisesta oppimisesta.

## 1. Mikä on Healerin tehtävä?

Käyttöliittymätestit ja dynaamiset lomakkeet rikkoutuvat yleensä siksi, että tekninen selektori (kuten ID tai XPath) muuttuu. Healer-kerros korvaa teknisen haun **semanttisella haulla**. Se ei etsi tiettyä ID:tä, vaan se etsii komponenttia, joka "näyttää ja tuntuu" oikealta.



---

## 2. Itseparannussykli (The Healing Process)

Healer toimii viidessä vaiheessa:

1. **Detection (Diff):** `FormEngine` tai testiilmoittaa, ettei komponenttia löydy.
2. **Analysis:** `HealerEngine` skannaa `UITreeBuilderin` avulla sovelluksen nykyisen UI-puun.
3. **Heal Attempt:** Järjestelmä käyttää kolmea painotettua heuristiikkaa:
    * **Text Match:** Etsitään tekstiä, joka vastaa `LanguageManagerin` käännöstä (huomioiden suomen kielen taivutukset).
    * **Type Match:** Varmistetaan, että ehdokas on oikeaa tyyppiä (esim. `TextField`).
    * **Context Match:** Tarkistetaan, onko ehdokas kytketty oikeaan datamalliin (Middleman-yhteys).
4. **Resolution:** Jos 100 % vastaavuus löytyy, järjestelmä luo uuden selektorin.
5. **Learning:** Onnistuminen tallennetaan muistiin, mikä vahvistaa käytetyn metodin luotettavuutta.

---

## 3. Komponentit

### HealerEngine
Päämoottori, joka suorittaa hakuheuristiikat. Se ei tee kovia päätöksiä sokkona, vaan kysyy neuvoa muistilta.

### HealerMemory
Järjestelmän "kokemusperäinen aivo". Se tallentaa:
- **Confidence-arvot:** Kuinka usein kukin metodit (teksti, tyyppi, konteksti) on onnistunut.
- **Historian:** Mitä muutoksia on tehty aiemmin.
- **Arkistoinnin:** Tallentaa vanhat muistiversiot aikaleimalla, jotta oppimista voidaan tutkia.

### HealerLogger & Stats
Dokumentointikerros, joka muuttaa raakadatan analytiikaksi:
- **Audit Log:** Jokainen korjaus kirjataan (Old Key -> New Key).
- **Accuracy %:** Tilastollinen näyttö siitä, kuinka luotettava itseparannus on.



---

## 4. Tutkimuksellinen näkökulma: "Semantic Stability"

Healer-kerros todistaa tutkimuksessasi, että käyttöliittymän ei tarvitse olla staattinen ollakseen luotettava. 

Käyttämällä **vokaalisointua** ja **vokaaligradationia** osana `Text Match` -prosessia, Healer pystyy tunnistamaan komponentteja, vaikka ne olisivat kieliopillisesti eri muodoissa (esim. "Nimi" vs. "Nimesi"). Tämä tekee SHL-järjestelmästä ainutlaatuisen verrattuna perinteisiin itseparannusmekanismeihin.

---

## 5. Keskeiset mittarit (HealerStats)

| Mittari | Kuvaus |
| :--- | :--- |
| **Text Accuracy** | Kuinka hyvin kielellinen tunnistus toimii. |
| **Type Integrity** | Estää vääriä korjauksia (esim. napin korvaaminen kentällä). |
| **Recovery Rate** | Kuinka monta % rikkoutuneista komponenteista saatiin palautettua ilman ihmistä. |

---

**Seuraava dokumentti:** [UI Adapters & Tree Builders](./adapters.md)
