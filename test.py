import datetime
import pandas as pd


def test_align_left():
    assert align_left('hello') == 'hello                          '
    assert align_left('') == ''
    assert align_left(123) == '123                           '
    assert align_left(None) == ''


def test_expiring_products():
    # Create a dummy dataframe with products that have different expiration dates
    data = {'Product Name': ['Product A', 'Product B', 'Product C'],
            'Packaging': ['01/23', '05/24', '06/25']}
    df = pd.DataFrame(data)

    # Convert the "Packaging" column to a datetime object
    df["Packaging"] = pd.to_datetime(df["Packaging"], format="%m/%y")

    # Set the expiration date for testing purposes
    data_scadenza_str = '31-12-2024'
    data_scadenza = datetime.datetime.strptime(data_scadenza_str, '%d-%m-%Y')

    # Find products with an expiration date up to the end of 2023
    mask = (df["Packaging"] <= pd.Timestamp(data_scadenza))
    expiring_products = df.loc[mask]

    # Check that the correct products are returned
    assert expiring_products.shape[0] == 2
    assert 'Product A' in expiring_products['Product Name'].values
    assert 'Product B' in expiring_products['Product Name'].values
    assert 'Product C' not in expiring_products['Product Name'].values
