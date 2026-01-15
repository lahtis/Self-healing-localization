# Adapter Roadmap — Future Extensions

Tämä osio kokoaa yhteen adapter‑kerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos adapter‑kerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. Adapter interface v2
- Yhtenäinen rajapinta kaikille adaptereille  
- Selkeämpi lifecycle (init → bind → render → update)  
- Parempi virheenkäsittely ja lokitus  
- Tuki adapterikohtaisille laajennuksille

## 2. Flet adapter v2
- Laajempi tuki Flet‑komponenteille  
- Parempi event‑binding  
- Tuki dynaamisille UI‑päivityksille  
- Yhteensopivuus tulevien Flet‑versioiden kanssa

## 3. PyQt adapter v2
- Laajempi widget‑tuki  
- Parempi layout‑hallinta  
- Tuki signaaleille ja sloteille  
- Yhtenäinen mappaus SHLComponent → QtWidget

## 4. Playwright adapter v2
- Parempi tuki web‑testaukseen  
- UI‑solmujen automaattinen tunnistus  
- Tuki dynaamisille elementeille ja odotuksille  
- Mahdollisuus snapshot‑testaukseen

## 5. Generic adapter template
- Mallipohja uusien adapterien luomiseen  
- Selkeä rakenne: mapping, events, rendering  
- Helpottaa yhteisön kontribuutioita

## 6. Adapter capability map
- Kuvaa, mitä ominaisuuksia kukin adapteri tukee  
- Auttaa healer‑ ja middleman‑kerroksia tekemään parempia päätöksiä  
- Mahdollistaa fallback‑strategiat

## 7. Adapter test suite
- Yhtenäiset testit kaikille adaptereille  
- Snapshot‑testit renderöidyille UI‑solmuille  
- Tuki mock‑ympäristöille (Qt, Flet, Playwright)

## 8. Adapter performance profiler
- Mittaa renderöinnin ja päivitysten keston  
- Tunnistaa hitaat komponentit  
- Auttaa optimoimaan suuria käyttöliittymiä
