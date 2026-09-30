import csv
import matplotlib.pyplot as plt

Tid = []
Middeltemperatur = []
Nedbør = []
Høyeste_middelvind = []
Snødybde = []
Ferdig_lest_fil = False

try:
    with open("sinnes_2014_2025.csv", "r", encoding="utf-8") as csvfil:
        leser = csv.reader(csvfil, delimiter=";")

        next(leser)
        try:
            for rad in leser:
                if rad[3]:
                    Tid.append(rad[3])
                
                elif rad[4]:
                    Middeltemperatur.append(float(rad[4]))

                elif rad[5]:
                    Nedbør.append(float(rad[5]))

                elif rad[6]:
                    Høyeste_middelvind.append(float(rad[6]))

                elif rad[7]:
                    Snødybde.append(float(rad[7]))
            Ferdig_lest_fil = True

        except ValueError:
            print("Advarsel: ufullstendig data!")
except FileNotFoundError:
    print("Filen ble ikke funnet. Vennligst sjekk filbanen og prøv igjen.")

if Ferdig_lest_fil == True:
    plt.figure(figsize=(10, 5))

    try:
        plt.plot(Tid, Middeltemperatur, label="Middeltemperatur", marker="o")
    except ValueError:
        print("Advarsel: ufullstendig Middeltemperatur-data")

    try:
        plt.plot(Tid, Nedbør, label="Nedbør", marker="o")
    except ValueError:
        print("Advarsel: ufullstendig Nedbør-data")

    try:
        plt.plot(Tid, Høyeste_middelvind, label="Høyeste middelvind", marker="o")
    except ValueError:
        print("Advarsel: ufullstendig Høyeste middelvind-data")

    try:
        plt.plot(Tid, Snødybde, label="Snødybde", marker="o")
    except ValueError:
        print("Advarsel: ufullstendig Snødybde-data")

    plt.title(f"Sinnes {Tid[0]} til {Tid[-1]}")
    plt.xlabel("Time")
    plt.ylabel("middeltemperatur, nedbør, høyeste middelvind og snødybde")
    plt.legend()
    plt.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()