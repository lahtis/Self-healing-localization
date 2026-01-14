# Osa 2 – Arkkitehtuurin synty (TestPyPI, modulaarisuus, healing‑sykli)

Ensimmäisten Python‑kokeilujen jälkeen projekti alkoi kasvaa nopeasti.  
Pienistä apuskripteistä syntyi tarve rakentaa jotakin suurempaa:  
järjestelmä, joka ei vain lukenut kielitiedostoja, vaan ymmärsi UI:n semanttisen rakenteen.

Tämä vaihe oli SHL frameworkin todellinen synty.

## Localizerista modulaariseksi paketiksi

Kun `Localizer` oli osoittautunut hyödylliseksi Digital Guestbookissa ja Jeevesissä, syntyi ajatus:

**tämä pitäisi irrottaa omaksi paketiksi.**

Tämä johti ensimmäiseen TestPyPI‑julkaisuun:

- **0.0.1** – ensimmäinen raakaversio, joka ei toiminut  
- **0.0.2** – korjattu versio, joka toimi ja todisti, että pakettimalli oli oikea suunta  

TestPyPI‑julkaisut pakottivat miettimään:

- tiedostorakennetta  
- modulaarisuutta  
- riippuvuuksia  
- julkaisuprosessia  
- versionhallintaa  

Tämä oli ensimmäinen hetki, jolloin projekti alkoi muistuttaa oikeaa kirjastoa.

## Modulaarisuuden synty

Kun Localizer irrotettiin omaksi paketiksi, syntyi tarve selkeälle rakenteelle:

- kielikerros  
- konfiguraatiokerros  
- tiedostokerros  
- UI‑adapterit  
- semanttinen logiikka  

Tämä johti ajatukseen, että UI:n ja lokalisoinnin ei pitäisi olla sidottuja toisiinsa.  
Sen sijaan niiden pitäisi kommunikoida **semanttisen välikerroksen** kautta.

Tämä oli SHL:n ensimmäinen arkkitehtoninen periaate.

## Healing‑syklin alku

Kun Localizer alkoi automaattisesti:

- luoda puuttuvia avaimia  
- täydentää oletusarvoja  
- päivittää JSON‑tiedostoja  

syntyi ajatus:

**entä jos koko UI voisi parantua samalla tavalla?**

Tästä syntyi healing‑syklin ensimmäinen versio:

1. **Havaitaan puuttuva tieto**  
2. **Luodaan oletus**  
3. **Tallennetaan se**  
4. **Käytetään sitä heti**  

Tämä oli aluksi vain lokalisointia varten, mutta pian kävi selväksi, että sama logiikka voisi toimia:

- UI‑komponenteille  
- semanttisille avaimille  
- rakenteille  
- adaptereille  
- jopa kokonaisille näkymille  

Healing‑syklistä tuli SHL:n ydinajatus.

## Jeevesin vaikutus arkkitehtuuriin

Kun Localizeria yritettiin liittää Jeevesiin, tuli esiin uusia tarpeita:

- modulaarisuus  
- tietokantakerros  
- turvallinen AI‑integraatio  
- kolmitasoinen validointi  
- erillinen semanttinen rekisteri  

Jeevesin uusi versio toimi käytännön testialustana, jossa SHL:n ideat joko toimivat tai kaatuivat.  
Moni SHL:n arkkitehtuurinen ratkaisu syntyi juuri näistä kokeiluista.

Tässä vaiheessa projekti ei ollut enää skripti eikä kirjasto.  
Se oli:

- modulaarinen  
- semanttinen  
- itseparantuva  
- framework‑agnostinen  
