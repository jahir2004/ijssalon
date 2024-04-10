# Creating the 'boekhouding.py' file with the specified dictionary
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# Importing functions and variables from 'presentatie.py'
from presentatie import presenteer

# Presenting the income data
presenteer(inkomsten, totaal_inkomsten)

import csv

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])
