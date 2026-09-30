import csv
import matplotlib.pyplot as plt

snødybde = []
nedbør = []
middeltemperatur = []
høyeste_middelvind = []

with open("sinnes_2014_2025.csv", "r", encoding="utf-8") as csvfil:
    leser = csv.reader(csvfil, delimiter=";")

    next(leser)
    if leser [3] == "Middeltemperatur":
        leser.append(middeltemperatur)
    else:
        next(leser)
print(middeltemperatur)