# UI-Skeema (V1) – Komponenttien määrittely

SHL-järjestelmä on tietomalli-ohjattu (Data-driven). Tämä tarkoittaa, että käyttöliittymää ei kovakoodata, vaan se määritellään JSON-pohjaisessa skeematiedostossa. Tämä dokumentti selittää skeeman rakenteen ja sen eri kenttien tarkoituksen.

## 1. Skeeman perusrakenne

Skeematiedosto sijaitsee yleensä polussa `shl/ui/schema/v1/ui_schema.json`. Sen ylin taso sisältää versiotiedot ja listan komponenteista.

```json
{
  "$schema": "[https://shl.dev/schema/ui/v1](https://shl.dev/schema/ui/v1)",
  "version": "1.0.0",
  "components": [ ... ]
}
