import csv
import matplotlib.pyplot as plt

filstier = (
    "sinnes_2014_2025_med_makstemperatur.csv",
    "oslo_blindern_1954_2025_med_makstemperatur.csv",
    "roeros_1954_2025_med_makstemperatur.csv",
    "tromsoe_1954_2025_med_makstemperatur.csv",
    "vaernes_1954_2025_med_makstemperatur.csv",
    "venabu_1954_2025_med_makstemperatur.csv"
)

resultater = {}

for filsti in filstier:

    try:
        with open(filsti, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = list(reader)

    except FileNotFoundError:
        print(f"Fant ikke fila {filsti}")
        continue

    alle_år = sorted({
        int(rad["Tid(norsk normaltid)"].split(".")[2])
        for rad in data
        if len(rad["Tid(norsk normaltid)"].split(".")) == 3
    })

    resultater[filsti] = {}

    for valgt_år in alle_år:
        antall_skifore = 0
        antall_målinger = 0

        for rad in data:
            dato = rad["Tid(norsk normaltid)"].strip()
            deler = dato.split(".")

            if len(deler) != 3:
                continue

            dag, måned, år = map(int, deler)
            if ((måned in (11, 12) and år == valgt_år - 1) or (måned in (1, 2, 3, 4, 5) and år == valgt_år)):

                sno = rad["Snødybde"].strip()
                if sno == "-" or sno == "":
                    continue
                antall_målinger += 1
                if int(sno) >= 20:
                    antall_skifore += 1

       
        if antall_målinger >= 100:
            resultater[filsti][valgt_år] = antall_skifore


    

fig, axs = plt.subplots(6, 1, figsize=(15, 15))

for ax, (stasjon, sesonger) in zip(axs, resultater.items()):

    år = list(sesonger.keys())
    dager = list(sesonger.values())

    ax.plot(år, dager)
    ax.set_title(stasjon)
    ax.set_ylabel("Skiføredager")
    ax.grid(True)

plt.tight_layout()
plt.show()

