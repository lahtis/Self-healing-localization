# SHL UI Components

Tämä hakemisto sisältää SHL‑järjestelmän käyttöliittymäkomponentit.  
Komponentit ovat järjestelmän pienin visuaalinen yksikkö, ja ne toimivat sillanrakentajina:

- UI‑skeeman  
- adapterien  
- middleman‑kerroksen  
- healer‑kerroksen  
- ja lopulta käyttöliittymän renderöinnin välillä.

Jokainen komponentti määritellään `ui_schema.json` ‑tiedostossa ja ladataan ohjelmallisesti `SHLComponent`‑luokan kautta.

## Komponenttien rooli

UI‑komponentit:

- määrittelevät, millaisia elementtejä käyttöliittymässä voi olla  
- sisältävät tekstikentät (`text_keys`)  
- kuvaavat framework‑kohtaiset toteutukset (`implementations`)  
- kantavat metatietoa, jota healer ja middleman hyödyntävät  
- toimivat adapterien renderöinnin lähtökohtana  

Ne ovat siis SHL:n “UI‑sanakirja”.

## Rakenne

Tässä hakemistossa voi olla:

- komponenttikohtaisia lisätiedostoja  
- komponenttien laajennuksia  
- komponenttien testejä  
- tulevia komponenttikohtaisia konfiguraatioita  

Varsinainen komponenttimäärittely sijaitsee kuitenkin aina skeemassa (`ui_schema.json`).

## Tulevat laajennukset

Tulevaisuudessa tänne voidaan lisätä:

- komponenttikohtaisia dokumentaatioita  
- komponenttikohtaisia testejä  
- komponenttikohtaisia laajennusmoduuleja  
- automaattisesti generoituja komponenttilistoja  

Tämä hakemisto toimii perustana kaikelle UI‑rakentamiselle SHL‑järjestelmässä.
