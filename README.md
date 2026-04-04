# Halvlederdioden – AC-beregninger

Dette repositoriet inneholder støttefiler til laboratorieøvelsen **"Halvlederdioden; AC – beregninger"**.  
Målet er å gjøre beregningene og figurgrunnlaget mer etterprøvbart ved å samle:

- **GeoGebra-filer** for teoretiske kurver
- **Python-kode** for simulering av likeretter med kondensator

På denne måten kan andre teste egne verdier og se hvordan endringer i parametere påvirker resultatene.

---

## Innhold

### `geogebra/`
GeoGebra-filer brukt til teoretiske kurver og visualiseringer for flere av kretsene i rapporten:

- `Krets1.ggb`
- `krets2.ggb`
- `krets3.ggb`
- `krets4.ggb`
- `krets4_inv.ggb`
- `krets5.ggb`

### `python/`
Python-kode og avhengigheter for simulering:

- `Krets5u.py`
- `requirements.txt`

---

## Krav

For å kjøre Python-koden trenger du:

- **Python 3**
- et terminalvindu (PowerShell, CMD, Git Bash eller lignende)
- anbefalt: et virtuelt miljø (`.venv`)

---

## Slik kjører du Python-filen med `.venv`

### 1. Klon repoet
```bash
git clone <repo-url>
cd -halvlederdioden-ac-beregninger