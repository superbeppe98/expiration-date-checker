from tabulate import tabulate
import pandas as pd
pd.options.mode.chained_assignment = None

# Funzione per allineare a sinistra le stringhe


def align_left(s):
    if pd.isna(s):
        return ""
    else:
        return f'{s:<30}'


# Carica il file Excel
df = pd.read_excel("prodotti.xlsx")

# Rinomina la colonna "Part Name" in "Nome Articolo" e spostala alla posizione 0 spostando il testo a sinistra
df = df.rename(columns={"Part Name": "Nome Articolo"})
nome_articolo = df.pop("Nome Articolo")
df.insert(0, "Nome Articolo", nome_articolo)


# Rinomina la colonna "Quantity" in "Quantità"
df = df.rename(columns={"Quantity": "Quantità"})

# Rinomina la colonna "Purchase Price" in "Prezzo di acquisto"
df = df.rename(columns={"purchase_price": "Prezzo di acquisto"})

# Converte la colonna "Confezionamento" in un oggetto datetime
df["Confezionamento"] = pd.to_datetime(df["Confezionamento"], format="%m/%y")

# Trova i prodotti con data di scadenza fino alla fine dell'anno 2023
mask = (df["Confezionamento"] <= pd.Timestamp(2023, 12, 31))
prodotti_scadenza = df.loc[mask]

prodotti_scadenza["Confezionamento"] = prodotti_scadenza["Confezionamento"].dt.strftime(
    '%d-%m-%Y')

# Stampa i prodotti trovati senza il numero di riga
print(tabulate(prodotti_scadenza, showindex=False, headers=df.columns))
