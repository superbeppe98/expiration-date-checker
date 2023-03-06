# Expiration Date Checker
A simple Python program for a Expiration date checker

## Installation
The following two dependencies are needed:
 - pandas
 - tabulate
You can install this using
```shell
pip install -r requirements.txt
```

## Usage
You need to provide a file .xlsx named "products"
```shell
$ python3 controllo.py
Inserisci la data di scadenza del confezionamento (formato: 01-01-2023):01-01-2025
Nome Articolo      Quantità  Confezionamento    Prezzo di acquisto
---------------  ----------  -----------------  --------------------
1111 | Test               9  01-01-2023         0,50 €
2222 | Test               1  01-01-2024         20,00 €
3333 | Test               1  01-01-2024         34,50 €
4444 | Test               2  01-01-2025         23,00 €
```
This is an example output for the given sample.
