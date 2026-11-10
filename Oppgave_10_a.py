import csv
import matplotlib.pyplot as plt
from datetime import datetime

Ønsket_årstall = input("Skriv inn ønsket årstall (2014-2025): ")

def plott_ønsket_data(indeks):
    plt.figure(figsize=(15,8))

    for navn, data in værstasjoner.items():

        tid = [rad[0] for rad in data]
        verdier = [rad[indeks] for rad in data]

        plt.plot(tid, verdier, label=navn)

    plt.legend()
    plt.grid(True)
    plt.show()

def gå_gjennom_data(filnavn):
    middeltemperatur = []
    nedbør = []
    høyeste_middelvind = []
    snødybde = []
    månedsdata = []
    måned = 1
    def sjekk_etter_gyldig_måling_middeltemperatur():
        try:
            middeltemperatur.append(float(rad[4]))
        except ValueError:
            return None

    def sjekk_etter_gyldig_måling_nedbør():
        try:
            nedbør.append(float(rad[5]))
        except ValueError:
            return None

    def sjekk_etter_gyldig_måling_høyeste_middelvind():
        try:
            høyeste_middelvind.append(float(rad[6]))
        except ValueError:
            return None

    def sjekk_etter_gyldig_måling_snødybde():
        try:
            snødybde.append(float(rad[7]))
        except ValueError:
            return None
    
    with open(filnavn, "r", encoding="utf-8") as csvfil:
        leser = csv.reader(csvfil, delimiter=";")

        next(leser)

        for rad in leser:
            rad = [verdi.replace(",", ".") for verdi in rad]

            try:
                dato = rad[2].split(".")
                if int(dato[2]) > int(Ønsket_årstall):
                    break
                try:
                    if 2014 <= int(Ønsket_årstall) <= 2025:
                        if dato[2] == Ønsket_årstall:
                            if int(dato[1]) == måned:
                                sjekk_etter_gyldig_måling_middeltemperatur()
                                sjekk_etter_gyldig_måling_nedbør()
                                sjekk_etter_gyldig_måling_høyeste_middelvind()
                                sjekk_etter_gyldig_måling_snødybde()
                            else:
                                # Beregner maks, min og sum for dataene og legger dem til i månedsdata-listen
                                if len(middeltemperatur) >= 2:
                                    maks_middeltemperatur = max(middeltemperatur)
                                    min_middeltemperatur = min(middeltemperatur)
                                else:
                                    maks_middeltemperatur = None
                                    min_middeltemperatur = None
                                if len(nedbør) >= 20:
                                    total_nedbør = sum(nedbør)
                                else:
                                    total_nedbør = None
                                if len(høyeste_middelvind) >= 2:
                                    maks_middelvind = max(høyeste_middelvind)
                                else:
                                    maks_middelvind = None
                                if len(snødybde) >= 2:
                                    maks_snødybde = max(snødybde)
                                else:
                                    maks_snødybde = None
                                månedsdata.append((datetime(int(Ønsket_årstall), måned, 1), maks_middeltemperatur, min_middeltemperatur, total_nedbør, maks_middelvind, maks_snødybde))
                                # Nullstiller listene for neste måned
                                for liste in [middeltemperatur, nedbør, høyeste_middelvind, snødybde]:
                                    liste.clear()
                                # Legger til dataene for første dag i neste måned
                                if måned < 12:
                                    måned += 1
                                sjekk_etter_gyldig_måling_middeltemperatur()
                                sjekk_etter_gyldig_måling_nedbør()
                                sjekk_etter_gyldig_måling_høyeste_middelvind()
                                sjekk_etter_gyldig_måling_snødybde()
                    else:
                        print(f"Advarsel: Det er ingen data for årstall {Ønsket_årstall}. Vennligst velg et årstall mellom 2014 og 2025.")
                        exit()
                except ValueError:
                    print(f"Advarsel: {Ønsket_årstall} er ikke et gyldig årstall. Vennligst velg et årstall mellom 2014 og 2025.")
                    exit()
            except IndexError:
                continue
        if len(middeltemperatur) >= 2:
            maks_middeltemperatur = max(middeltemperatur)
            min_middeltemperatur = min(middeltemperatur)
        else:
            maks_middeltemperatur = None
            min_middeltemperatur = None
        if len(nedbør) >= 20:
            total_nedbør = sum(nedbør)
        else:
            total_nedbør = None
        if len(høyeste_middelvind) >= 2:
            maks_middelvind = max(høyeste_middelvind)
        else:
            maks_middelvind = None
        if len(snødybde) >= 2:
            maks_snødybde = max(snødybde)
        else:
            maks_snødybde = None
        månedsdata.append((datetime(int(Ønsket_årstall), måned, 1), maks_middeltemperatur, min_middeltemperatur, total_nedbør, maks_middelvind, maks_snødybde))
        # Nullstiller listene for neste måned
        for liste in [middeltemperatur, nedbør, høyeste_middelvind, snødybde]:
            liste.clear()
    return månedsdata

print

månedsdata_sinnes = gå_gjennom_data("sinnes_2014_2025_med_makstemperatur.csv")
månedsdata_venabu = gå_gjennom_data("venabu_1954_2025_med_makstemperatur.csv")
månedsdata_vaernes = gå_gjennom_data("vaernes_1954_2025_med_makstemperatur.csv")
månedsdata_tromsoe = gå_gjennom_data("tromsoe_1954_2025_med_makstemperatur.csv")
månedsdata_roeros = gå_gjennom_data("roeros_1954_2025_med_makstemperatur.csv")
månedsdata_oslo_blindern = gå_gjennom_data("oslo_blindern_1954_2025_med_makstemperatur.csv")

værstasjoner = {"Sinnes": månedsdata_sinnes,"Venabu": månedsdata_venabu,"Værnes": månedsdata_vaernes,"Tromsø": månedsdata_tromsoe, "Røros": månedsdata_roeros,"Oslo Blindern": månedsdata_oslo_blindern}

print("Hva ønsker du å sammenligne?")

print("1. Maks Middeltemperatur")
print("2. Min Middeltemperatur")
print("3. Total Nedbør")
print("4. Maks Middelvind")
print("5. Maks Snødybde")

ønsker_å_sammenligne = input("Svar: ")

try:
    plott_ønsket_data(int(ønsker_å_sammenligne))
except ValueError:
    print("Ugyldig valg. Vennligst velg et tall mellom 1 og 5.")
