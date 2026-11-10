import csv
import matplotlib.pyplot as plt
from datetime import datetime

dagsdata = []

Ønsket_årstall = input("Skriv inn ønsket årstall (2014-2025): ")

def sjekk_etter_gyldig_måling_middeltemperatur():
    try:
        return float(rad[3])
    except ValueError:
        return None

def sjekk_etter_gyldig_måling_nedbør():
    try:
        return float(rad[4])
    except ValueError:
        return None

def sjekk_etter_gyldig_måling_høyeste_middelvind():
    try:
        return float(rad[5])
    except ValueError:
        return None

def sjekk_etter_gyldig_måling_snødybde():
    try:
        return float(rad[6])
    except ValueError:
        return None
    
def hent_ut_dato_fra_liste(x):
    return x[0]

with open("sinnes_2014_2025.csv", "r", encoding="utf-8") as csvfil:
    leser = csv.reader(csvfil, delimiter=";")

    next(leser)

    for rad in leser:
        rad = [verdi.replace(",", ".") for verdi in rad]

        try:
            dato = rad[2].split(".")
            try:
                if 2014 <= int(Ønsket_årstall) <= 2025:
                    if dato[2] == Ønsket_årstall:
                        middeltemperatur = sjekk_etter_gyldig_måling_middeltemperatur()
                        nedbør = sjekk_etter_gyldig_måling_nedbør()
                        høyeste_middelvind = sjekk_etter_gyldig_måling_høyeste_middelvind()
                        snødybde = sjekk_etter_gyldig_måling_snødybde()
                        dagsdata.append((datetime.strptime(rad[2], "%d.%m.%Y"), middeltemperatur, nedbør, høyeste_middelvind, snødybde))
                else:
                    print(f"Advarsel: Det er ingen data for årstall {Ønsket_årstall}. Vennligst velg et årstall mellom 2014 og 2025.")
                    exit()
            except ValueError:
                print(f"Advarsel: {Ønsket_årstall} er ikke et gyldig årstall. Vennligst velg et årstall mellom 2014 og 2025.")
                exit()
        except IndexError:
            continue

dagsdata.sort(key=hent_ut_dato_fra_liste)

# Del opp i egne lister
Tid = [dato for dato, _, _, _, _ in dagsdata]
middeltemperatur = [middeltemperatur for _, middeltemperatur, _, _, _ in dagsdata]
nedbør = [nedbør for _, _, nedbør, _, _ in dagsdata]
høyeste_middelvind = [høyeste_middelvind for _, _, _, høyeste_middelvind, _ in dagsdata]
snødybde = [snødybde for _, _, _, _, snødybde in dagsdata]

fig, axs = plt.subplots(4, 1, figsize=(15, 10))

axs[0].plot(Tid, middeltemperatur, color="red")
axs[0].set_title("Middeltemperatur")
axs[0].grid(True)

axs[1].plot(Tid, nedbør, color="blue")
axs[1].set_title("Nedbør")
axs[1].grid(True)

axs[2].plot(Tid, høyeste_middelvind, color="green")
axs[2].set_title("Høyeste middelvind")
axs[2].grid(True)

axs[3].plot(Tid, snødybde, color="black")
axs[3].set_title("Snødybde")
axs[3].grid(True)

import matplotlib.dates as mdates
for ax in axs:
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m.%Y"))
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

#Hvordan skal vi tolke "-" i snødybde? Er det null eller manglende data?