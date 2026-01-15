# Registry Roadmap — Future Extensions

Tämä osio kokoaa yhteen rekisterikerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos rekisterikerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. Patcher‑perheen laajennukset
- **patcher_full**  
  Sallii kaikki muutokset, myös komponenttien poistot.
- **patcher_strict**  
  Hyväksyy vain tarkasti määritellyt muutokset (esim. vain healerin tuottamat).

## 2. Blueprint diff ‑moduuli
- Rakenteellinen vertailu kahden blueprintin välillä  
- Rakenteellinen vertailu kahden UCR‑tiedoston välillä  
- Tuottaa selkeän diff‑raportin (kuten git diff, mutta SHL‑komponenteille)

## 3. Blueprint normalizer / formatter
- Järjestää kentät vakiojärjestykseen  
- Poistaa tyhjät tai turhat kentät  
- Yhdenmukaistaa blueprint‑rakenteen versionhallintaa varten

## 4. UCR schema migrator
- Päivittää vanhat UCR‑versiot uusiin skeemaversioihin  
- Mahdollistaa pitkän aikavälin yhteensopivuuden (v1 → v2 → v3…)

## 5. Blueprint linter
- Tarkistaa puuttuvat text_keys‑arvot  
- Varoittaa epäloogisista framework_map‑rakenteista  
- Tunnistaa käyttämättömät tai ristiriitaiset healer_key‑määritykset  
- Toimii kuin “eslint”, mutta SHL‑blueprinteille

## 6. Registry cache / memoization
- Välimuisti ladatuille UCR‑tiedostoille  
- Hash‑tarkistus ennen uudelleenlatausta  
- Nopeuttaa healing‑kerroksen toimintaa

## 7. Blueprint metadata ‑kerros
- Blueprintin versiohistoria  
- Viimeisin muokkaaja  
- Healing‑ ja patcher‑raporttien tallennus  
- Mahdollistaa “itseään selittävät” blueprintit
