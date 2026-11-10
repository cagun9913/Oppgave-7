import csv
 
filsti = r"sinnes_2014_2025.csv"

try:
    with open(filsti, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        data = list(reader)
except FileNotFoundError:
    print("Fant ikke fila. Sjekk at stien er riktig og at du kjører scriptet fra riktig mappe.")
    exit()

alle_år = sorted({
    rad["Tid(norsk normaltid)"].split(".")[2]
    for rad in data
    if len(rad["Tid(norsk normaltid)"].split(".")) == 3
})

print("Mulige år du kan skrive inn:")
for år in alle_år:
    print(" -", år)

valgt_år = int(input("Skriv inn et år: ").strip())

skisesong_dager = []
for rad in data:
    dato = rad["Tid(norsk normaltid)"].strip()
    deler = dato.split(".")
    if len(deler) != 3:
        continue

    dag, måned, år = map(int, deler)

    # Skisesong-regel
    if (måned in (11, 12) and år == valgt_år - 1) or (måned in (1, 2, 3, 4, 5) and år == valgt_år):
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


