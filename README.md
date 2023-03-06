# Expiration Date Checker
A simple Python program for a Expiration date checker

## Installation
To install Expiration Date Checker, you need to have Python 3 installed on your system. The program also requires two dependencies, pandas and tabulate, to be installed. You can install these dependencies by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
To use Expiration Date Checker, you need to provide an Excel file named "products.xlsx" that contains information about your products, including the expiration date, quantity, packaging, and purchase price.

Once you have the Excel file ready, you can run the program by navigating to the directory where the program is stored and running the following command:
```shell
$ python3 controllo.py
```
This will prompt you to enter the expiration date of the packaging in the format "dd-mm-yyyy". After entering the date, the program will display a table with the name, quantity, packaging, and purchase price of the products whose expiration date is later than the date you entered.

Here's an example output for the given sample:

```shell
Enter the expiration date of the packaging (format: dd-mm-yyyy): 01-01-2025
+----------------+------------+-----------------+----------------------+
| Nome Articolo  | Quantità   | Confezionamento | Prezzo di acquisto |
+================+============+=================+======================+
| 1111 | Test    | 9          | 01-01-2023      | 0.50                 |
+----------------+------------+-----------------+----------------------+
| 2222 | Test    | 1          | 01-01-2024      | 20.00                |
+----------------+------------+-----------------+----------------------+
| 3333 | Test    | 1          | 01-01-2024      | 34.50                |
+----------------+------------+-----------------+----------------------+
| 4444 | Test    | 2          | 01-01-2025      | 23.00                |
+----------------+------------+-----------------+----------------------+
```
This output shows the name, quantity, packaging, and purchase price of all the products whose expiration date is later than January 1, 2025.
