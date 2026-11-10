
import matplotlib.pyplot as plt
import csv

filnavn = 'sinnes_2014_2025.csv'

month_dict = {}

with open(filnavn, mode='r', encoding='UTF-8') as fil:
    leser = csv.DictReader(fil, delimiter=';')

    for rad in leser:
        if not rad or 'Tid(norsk normaltid)' not in rad:
            continue

        dato_str = rad.get('Tid(norsk normaltid)', '')
        vind_str = rad.get('Høyeste middelvind (døgn)', '')

        if dato_str and vind_str and vind_str != '-':
            try:
                deler = dato_str.split('.')
                day, month, year = deler[0], deler[1], deler[2]

                nøkkel = f"{year}-{month}"

                if nøkkel not in month_dict:
                    month_dict[nøkkel] = []

                vind = float(vind_str.replace('"', '').replace(',', '.'))
                month_dict[nøkkel].append(vind)

            except (ValueError, IndexError):
                continue

resultat = []

sortedkeys = sorted(month_dict.keys())

for nøkkel in sortedkeys:
    verdier = month_dict[nøkkel]

    if len(verdier) > 0:
        verdier.sort()
        antall = len(verdier)

        min_vind = verdier[0]
        maks_vind = verdier[-1]

        if antall % 2 == 1:
            median_vind = verdier[antall // 2]
        else:
            midten1 = verdier[(antall // 2) -1]
            midten2 = verdier[antall // 2]
            median_vind = (midten1 + midten2) / 2

        resultat.append({
            'tid': nøkkel,
            'min': min_vind,
            'median': median_vind,
            'maks': maks_vind
        })



if not resultat:
    print("Fant ingen data")

tider = []
minverdier = []
medianverdier = []
maksverdier = []

for r in resultat:
    tider.append(r['tid'])
    minverdier.append(r['min'])
    medianverdier.append(r['median'])
    maksverdier.append(r['maks'])

plt.figure(figsize=(12, 6))

plt.plot(tider, minverdier, label='Minimum Vind', color='blue')
plt.plot(tider, medianverdier, label='Median Vind', color='green')
plt.plot(tider, maksverdier, label='Maksimum Vindstyrke', color='red')

plt.xlabel('Måned')
plt.ylabel('Vindstyrke')
plt.title('Vindstatistikk per måned gjennom perioden')
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()

