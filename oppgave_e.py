import csv
import matplotlib.pyplot as plt   

# Filsti til CSV-fila
filsti = r"C:\Users\prowo\OneDrive - Universitetet i Stavanger\UiS\UiS\semester_1\DAT120\koding\inlerveringer\inlevering 7\sinnes_2014_2025.csv"

def safe_int(x):
    try:
        return int(x)
    except:
        return 0

data = []
print("Prøver å åpne:", filsti)

try:
    with open(filsti, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        data = list(reader)
except FileNotFoundError:
    print("Fant ikke fila. Sjekk at stien er riktig og at du kjører scriptet fra riktig mappe.")
    exit()

# Finn alle mulige år
alle_år = set()

for rad in data:
    dato = rad.get("Tid(norsk normaltid)", "").strip()
    if not dato:
        continue

    deler = dato.split(".")
    if len(deler) != 3:
        continue

    år = deler[2]
    alle_år.add(år)

alle_år = sorted(alle_år)

print("Mulige år du kan skrive inn:")
for år in alle_år:
    print(" -", år)

valgt_år = input("Skriv inn et år: ").strip()

skisesong_dager = []

for rad in data:
    dato = rad["Tid(norsk normaltid)"].strip()
    deler = dato.split(".")

    if len(deler) != 3:
        continue  

    dag = int(deler[0])
    måned = int(deler[1])
    år = int(deler[2])

    if måned in (11, 12) and år == int(valgt_år) - 1:
        skisesong_dager.append(rad)
    elif måned in (1, 2, 3, 4, 5) and år == int(valgt_år):
        skisesong_dager.append(rad)
antall_skifore = 0

for rad in skisesong_dager:
    sno = rad["Snødybde"].strip()
    if sno == "-" or sno == "":
        continue
    try:
        sno_cm = int(sno)
    except:
        continue
    if sno_cm >= 20:
        antall_skifore += 1
print(f"Antall dager med skiføre i skisesongen {valgt_år}: {antall_skifore}")


dgfdsfs
