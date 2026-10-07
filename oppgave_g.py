import csv
filsti = r"sinnes_2014_2025.csv"

# Navn; ID, dato, middeltemp, nedbør, middelvind, snødybde

max_length = 0
max_start = None
max_end = None

current_length = 0
current_start = None
current_end = None

try:
    with open(filsti, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row or len(row) < 5:
                continue

            dato = row[2].strip()
            nedbor_str = row[4].strip()

            try:
                nedbor = float(nedbor_str.replace("," , "."))
            except ValueError:
                current_length = 0
                current_start = None
                current_end = None
                continue

            if nedbor == 0:
                if current_length == 0:
                    current_start = dato
                current_length += 1
                current_end = dato

                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
                    max_end = current_end
            else:
                current_length = 0
                current_start = None
                current_end = None

except FileNotFoundError:
    print("Fant ikke fila. Sjekk at stien er riktig og at du kjører scriptet fra riktig mappe.")
    exit()


print("Lengste sammenhengende periode uten nedbør:")
print(f"Lengde: {max_length} dager")
print(f"Startdato: {max_start}")
print(f"Sluttdato: {max_end}")