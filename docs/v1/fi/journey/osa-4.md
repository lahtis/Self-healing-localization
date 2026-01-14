# Osa 4 – Jeevesin uusi aikakausi, turvallisuuskerrokset ja SHL:n lopullinen muoto

Kun Localizer oli muuttunut paketiksi ja healing‑sykli oli saanut ensimmäisen muotonsa, projekti tarvitsi todellisen testialustan.  
Tähän rooliin nousi Jeeves – alun perin yksinkertainen RSS‑daemon, mutta nyt täysin uuden kehitysvaiheen keskipiste.

## Jeevesin uudelleensyntymä – modulaarinen ja tietokantapohjainen

Uusi Jeeves rakennettiin alusta asti modulaariseksi:

- erilliset moduulit logiikalle  
- tietokantakerros pysyvyyttä varten  
- selkeä rajapinta UI:lle  
- mahdollisuus laajentaa toimintoja ilman, että koko järjestelmä hajoaa  

Tämä versio oli paljon kunnianhimoisempi kuin alkuperäinen.  
Se ei ollut enää “daemon”, vaan alustaprojekti, jonka päälle voisi rakentaa useita UI‑kerroksia ja palveluita.

## AI‑integraation ongelmat – ja tarve turvallisuudelle

Kun Jeevesiin yritettiin liittää AI‑työkaluja, syntyi nopeasti ongelmia:

- AI yritti tehdä liikaa  
- rajapinnat olivat liian avoimia  
- syötteitä ei validoitu riittävästi  
- järjestelmä saattoi mennä epävakaaksi  

Tämä johti tärkeään oivallukseen:

**AI ei saa olla suoraan kiinni järjestelmän ytimessä.  
Sen täytyy kulkea turvallisen välikerroksen kautta.**

Tämän seurauksena Jeevesiin rakennettiin lähes “NASAn veroinen” kolmikerroksinen turvakerros:

1. **Syötekerros**  
   – validoi kaiken, mitä AI tai UI lähettää  
2. **Semanttinen kerros**  
   – tulkitsee tarkoituksen, ei vain tekstiä  
3. **Toimintakerros**  
   – suorittaa vain sallitut ja turvalliset operaatiot  

Tämä oli ensimmäinen kerta, kun healing‑sykli ja semanttinen rekisteri alkoivat toimia yhdessä.

## Healing‑syklin kypsyminen

Jeevesin kautta healing‑sykli kehittyi merkittävästi.  
Alkuperäinen ajatus “lisää puuttuva avain JSON‑tiedostoon” laajeni:

- puuttuvat UI‑elementit voidaan generoida  
- puuttuvat semanttiset avaimet voidaan luoda  
- puuttuvat rakenteet voidaan täydentää  
- järjestelmä voi korjata itseään ilman, että kehittäjä koskee koodiin  

Healing‑syklistä tuli:

- **reaktiivinen** (havaitsi muutokset)  
- **oppiva** (täytti puuttuvat kohdat)  
- **pysyvä** (tallensi muutokset)  
- **framework‑agnostinen** (toimi missä tahansa ympäristössä)  

Tämä oli hetki, jolloin SHL framework alkoi saada lopullisen muotonsa.

## Semanttinen rekisteri ja adapterit

Jeevesin kehityksen aikana syntyi tarve erottaa:

- mitä UI haluaa esittää  
- miten se esitetään  
- missä ympäristössä se esitetään  

Tästä syntyivät:

### Semanttinen rekisteri  
Yhteinen “sanakirja”, joka kuvaa:

- tarkoitukset  
- toiminnot  
- UI‑elementtien merkitykset  

### Adapterit  
Kerros, joka muuntaa semanttisen rakenteen:

- Flet‑komponenteiksi  
- CLI‑komponenteiksi  
- tulevaisuudessa muihin UI‑frameworkeihin  

Tämä teki SHL:stä ensimmäistä kertaa **framework‑agnostisen**.

Tässä vaiheessa SHL ei ollut enää:

- skripti  
- kirjasto  
- tai yksittäinen työkalu  

Se oli:

- arkkitehtuuri  
- semanttinen välikerros  
- itseparantuva järjestelmä  
- turvallinen AI‑rajapinta  
- ja pohja tuleville UI‑frameworkeille
