# Middleman Roadmap — Future Extensions

Tämä osio kokoaa yhteen middleman‑kerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos middleman‑kerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. Middleman diff ‑moduuli
- Vertaa UI‑puuta ennen ja jälkeen healingin  
- Tuottaa rakenteellisen diff‑raportin middleman‑tasolla  
- Auttaa debuggaamaan healing‑päätöksiä ja UI‑muutoksia

## 2. Middleman normalizer / formatter
- Yhdenmukaistaa middleman‑tuottaman UI‑puun  
- Poistaa tyhjät tai turhat solmut  
- Järjestää komponentit vakiojärjestykseen  
- Parantaa UI‑puun luettavuutta ja versionhallintaa

## 3. Middleman linter
- Tarkistaa epäloogiset tai ristiriitaiset UI‑solmut  
- Varoittaa puuttuvista text_keys‑arvoista  
- Tunnistaa virheelliset healer_key‑määritykset  
- Toimii kuin “eslint”, mutta middleman‑tuotoksille

## 4. Middleman cache / memoization
- Välimuisti UI‑puun välituloksille  
- Hash‑tarkistus ennen uudelleenrakennusta  
- Nopeuttaa healing‑prosessia suurissa käyttöliittymissä

## 5. Middleman metadata ‑kerros
- Tallentaa UI‑puun rakennushistorian  
- Kirjaa healing‑päätökset ja patcher‑raportit  
- Mahdollistaa “itseään selittävät” UI‑puut

## 6. Middleman schema validator
- Varmistaa, että middleman‑tuottama UI‑puu noudattaa sisäistä skeemaa  
- Estää virheelliset solmut ennen UI‑kerrokseen siirtymistä  
- Toimii vastaparina registry‑kerroksen UCR‑validoinnille

## 7. Middleman → Blueprint reverse‑mapping (kokeellinen)
- Mahdollistaa UI‑puun palauttamisen blueprint‑muotoon  
- Auttaa debuggaamaan healing‑päätöksiä  
- Luo kaksisuuntaisen datavirran middleman‑ ja registry‑kerrosten välille
