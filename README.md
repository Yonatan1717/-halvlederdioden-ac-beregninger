# Halvlederdioden – AC-beregninger

Dette repositoriet inneholder GeoGebra-filer og Python-kode brukt som støtte til laboratorieøvelsen **"Halvlederdioden; AC – beregninger"**.

Målet er å gjøre beregningene og figurgrunnlaget mer etterprøvbart, slik at andre kan teste egne verdier og utforske hvordan ulike parametere påvirker resultatene.

## Innhold

### `geogebra/`
GeoGebra-filer for teoretiske kurver:
- `Krets1.ggb`
- `krets2.ggb`
- `krets3.ggb`
- `krets4.ggb`
- `krets4_inv.ggb`
- `krets5.ggb`

### `python/`
Python-kode og avhengigheter:
- `Krets5u.py`
- `requirements.txt`

## Krav

For å kjøre Python-koden trenger du:
- Python 3
- terminal (PowerShell, CMD, Git Bash eller lignende)
- anbefalt: virtuelt miljø (`.venv`)

## Slik kloner du repoet

```bash
git clone https://github.com/Yonatan1717/-halvlederdioden-ac-beregninger.git
cd -halvlederdioden-ac-beregninger
```

## Slik kjører du Python-filen med `.venv`

### 1. Opprett virtuelt miljø

#### Windows

```bash
py -3 -m venv .venv
```

Hvis `py` ikke fungerer:

```bash
python -m venv .venv
```

#### macOS / Linux

```bash
python3 -m venv .venv
```

### 2. Aktiver miljøet

#### Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

Dersom PowerShell blokkerer aktivering, kan du midlertidig tillate det med:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Kjør deretter:

```bash
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```bash
.venv\Scripts\activate.bat
```

#### Git Bash

```bash
source .venv/Scripts/activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

Når miljøet er aktivert, vil du vanligvis se `(.venv)` først i terminalen.

### 3. Installer nødvendige pakker

```bash
pip install -r python/requirements.txt
```

### 4. Kjør Python-filen

```bash
python python/Krets5u.py
```

På Windows kan du også bruke:

```bash
py python/Krets5u.py
```

### 5. Avslutt miljøet

Når du er ferdig, kan du skrive:

```bash
deactivate
```

## GeoGebra-filer

GeoGebra-filene kan åpnes i **GeoGebra Classic** eller i nettversjonen av GeoGebra.

Disse filene kan brukes til å:
- vise teoretiske kurver
- teste andre parameterverdier
- sammenligne hvordan endringer i diodefall, zenerspenning, frekvens, motstand og kondensator påvirker resultatene
