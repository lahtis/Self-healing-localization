# Middleman-logiikka – Semanttinen datan käsittely

Middleman-logiikka on SHL-järjestelmän "diplomaatti". Sen tehtävänä on varmistaa, että sovelluksen liiketoimintadata (Business Logic) ja käyttöliittymän esitysmuoto (UI Representation) pysyvät synkronoituna, vaikka ne puhuvat eri kieliä.

## 1. Mikä on Middleman?

Middleman on puskuri, joka eristää datamallin käyttöliittymästä. Se estää sen, että käyttöliittymän muutokset (esim. nimen vaihtuminen "Etunimeksi") rikkoisivat taustajärjestelmän datan.



## 2. Semanttinen muunnosprosessi

Kun data kulkee järjestelmän läpi, Middleman suorittaa sille semanttisen analyysin:

### A. ToComponent (Data -> UI)
- **Tehtävä:** Muuntaa raakadata (kuten `datetime`-objekti tai `User`-luokka) merkkijonoksi tai valinnaksi.
- **Esimerkki:** Jos järjestelmässä on osoite-objekti, Middleman voi koota siitä tekstikenttään sopivan merkkijonon: *"Katuosoite 1, 00100 Helsinki"*.

### B. FromComponent (UI -> Data)
- **Tehtävä:** Tulkitsee käyttäjän syötteen ja palauttaa sen oikeassa muodossa takaisin järjestelmään.
- **Esimerkki:** Jos käyttäjä kirjoittaa päivämääräkenttään "14. tammikuuta", Middleman muuntaa sen ISO-standardin mukaiseksi `2026-01-14` muodoksi.



---

## 3. Integraatio Healerin kanssa

Middleman-logiikka on kriittinen osa itseparannusta. Kun Healer yrittää tunnistaa komponenttia, se tarkistaa:
1. **Löytyykö Middleman-yhteys?** Jos komponentti `user_email` on kytketty `UserMiddleman`-luokkaan, Healer tietää etsiä kenttää, johon syötetään sähköpostiosoitteita.
2. **Data-validointi:** Healer voi testata ehdokaskenttää syöttämällä siihen dataa Middlemanin kautta. Jos Middleman hyväksyy syötteen, on todennäköistä, että oikea komponentti on löytynyt.

---

## 4. Käyttäjän oma avainkieli (User's Key Language)

Tutkimuksen kannalta tärkein ominaisuus on kyky tallentaa käyttäjän luomaa semanttista kieltä.
- Kun käyttäjä luo uuden kohteen (esim. "Kesämökki"), Middleman rekisteröi tämän nimen ja kytkee sen taustalla olevaan ID-tunnukseen.
- Jos käyttöliittymä rikkoutuu, Healer käyttää tätä tallennettua "avainkieltä" löytääkseen juuri sen kentän, jonka käyttäjä itse nimesi.

---

## 5. Kehitysnäkymät

Tulevaisuudessa Middleman-logiikkaa laajennetaan tukemaan:
- **Automaattista tyyppitunnistusta:** Middleman osaa itse päätellä datan perusteella, pitäisikö se näyttää kalenterina vai tekstikenttänä.
- **Älykästä täyttöä:** Jos käyttäjä on täyttänyt "Koti-osoitteen", Middleman voi ehdottaa postinumeroa automaattisesti kielellisen kontekstin perusteella.
