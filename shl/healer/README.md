# Healer Roadmap — Future Extensions

Tämä osio kokoaa yhteen healer‑kerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos healer‑kerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. Healer rule engine v2
- Selkeämpi sääntökieli healing‑päätöksille  
- Mahdollisuus prioriteetteihin ja sääntöjen painotuksiin  
- Tuki monimutkaisille ehdollisille korjauksille

## 2. Healer explainability layer
- Selittää, miksi tietty healing‑päätös tehtiin  
- Tuottaa “decision trace” ‑raportin  
- Auttaa debuggaamaan ja kouluttamaan uusia sääntöjä

## 3. Healer simulation mode
- Ajaa healingin ilman, että muutoksia sovelletaan  
- Tuottaa raportin mahdollisista korjauksista  
- Hyödyllinen testaukseen ja CI‑putkiin

## 4. Healer rollback / undo
- Mahdollistaa healing‑muutosten peruuttamisen  
- Tallentaa healing‑session historian  
- Toimii yhdessä patcher‑raporttien kanssa

## 5. Healer performance profiler
- Mittaa healing‑prosessin keston  
- Tunnistaa hitaat säännöt ja pullonkaulat  
- Tuottaa tilastotietoa optimointia varten

## 6. Healer memory v3
- Parempi pitkäaikainen muistikerros  
- Tuki useille eri muistityypeille (session, project, global)  
- Mahdollisuus oppia käyttäjän korjaustavoista

## 7. Healer test suite generator
- Luo automaattisia testitapauksia healing‑säännöille  
- Varmistaa regressioiden eston  
- Tuottaa snapshot‑testejä UI‑puusta

## 8. Healer → Blueprint feedback loop
- Kirjoittaa healing‑päätökset takaisin blueprintiin  
- Mahdollistaa blueprintin automaattisen parantamisen  
- Luo kaksisuuntaisen datavirran healerin ja registry‑kerroksen välille
