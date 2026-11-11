#gruppe opggave 10 
import csv
import matplotlib.pyplot as plt

sommer = {}
hoysommer = {}
trope = {}

with open("oslo_blindern_1954_2025_med_makstemperatur (1).csv", encoding="utf-8") as fil:
    leser = csv.reader(fil, delimiter=";")

    next(leser)

    for rad in leser:
        dato = rad[2]
        maks_temp = rad[3]

        if maks_temp == "" or maks_temp == "-":
            continue

        aar = int(dato[-4:])
        temp = float(maks_temp.replace(",", "."))

        if aar not in sommer:
            sommer[aar] = 0
            hoysommer[aar] = 0
            trope[aar] = 0

        if temp > 20:
            sommer[aar] += 1

        if temp > 25:
            hoysommer[aar] += 1

        if temp > 30:
            trope[aar] += 1

aarstall = sorted(sommer.keys())

plt.plot(aarstall, [sommer[a] for a in aarstall], label="Sommerdager")
plt.plot(aarstall, [hoysommer[a] for a in aarstall], label="Høysommerdager")
plt.plot(aarstall, [trope[a] for a in aarstall], label="Tropedager")

plt.xlabel("År")
plt.ylabel("Antall dager")
plt.title("Oslo Blindern")
plt.legend()
plt.grid()

plt.show()