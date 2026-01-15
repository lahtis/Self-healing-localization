# SHL Utils

Tämä hakemisto on varattu SHL‑järjestelmän yhteisille apumoduuleille.  
Utils‑kansio sisältää pieniä, uudelleenkäytettäviä työkaluja, jotka eivät kuulu suoraan mihinkään yksittäiseen kerrokseen (core, registry, middleman, healer, adapters, ui_tree, diff).

## Tarkoitus

Utils‑kansion tavoitteena on:

- tarjota yhteisiä apufunktioita ja luokkia
- välttää koodin toistoa eri kerrosten välillä
- pitää kerroskohtaiset moduulit puhtaina ja keskittyneinä
- tarjota paikka pienille “liimafunktioille”, jotka eivät tarvitse omaa kerrosta

## Mitä utils EI ole

Utils ei ole:

- kaatopaikka satunnaisille funktioille  
- paikka kerroslogiikalle  
- paikka, jonne siirretään koodia vain siksi, ettei tiedetä mihin se kuuluu  

Utils on tarkoitettu vain **pienille, yleishyödyllisille apureille**, jotka palvelevat useita kerroksia.

## Mahdollisia tulevia moduuleja

Tänne voidaan lisätä esimerkiksi:

- **string_utils.py**  
  – tekstin normalisointi, siistiminen, vertailu

- **path_utils.py**  
  – polkujen käsittely, tiedostojen etsiminen

- **validation_utils.py**  
  – pienet validointiapurit, joita core ja registry voivat käyttää

- **debug_utils.py**  
  – lokitus, aikaleimat, debug‑tulostus

- **conversion_utils.py**  
  – datarakenteiden muunnokset (dict → object, object → dict)

- **timing_utils.py**  
  – suoritusajan mittaus ja profilointi

## Tulevaisuuden laajennukset

- yhteinen logging‑kerros  
- konfiguraation lataus ja välimuisti  
- pienet DSL‑työkalut skeeman käsittelyyn  
- apurit diff‑kerroksen raportointiin  
- snapshot‑tallennus UI‑puulle tai healer‑datalle

Utils‑kansio kasvaa SHL‑järjestelmän mukana, mutta pysyy kevyenä ja tarkoituksenmukaisena.
