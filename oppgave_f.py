# f) Forenklet plantevekst: En forenklet modell av hvordan en plante vokser basert på
# temperatur er som følger: Planten trenger et minimum av 5 plussgrader for å vokse. Dere
# kan regne at planten sin vekst en gitt dag er lik temperatur minus
# minimumstemperaturen. Beregn total plantevekst et gitt år.

filnavn = r'C:\Users\Krist\DAT120\øvingsoppgave 7\Oppgave-7\sinnes_2014_2025_med_makstemperatur.csv'
dato = input('skriv inn et valgfritt år fra 2014-2025: ')
#dato = dato.replace(',', '.')
aarlig_vekst = []
dager_uten_vekst = 0
with open(filnavn, 'r', encoding='utf-8') as fila:
    fila.readline()

    for linje in fila:
        data = linje.strip().split(';')
        if data[2].endswith(dato):
            maxtemp = data[3]
            maxtemp = maxtemp.replace(',', '.')
            maxtemp = float(maxtemp)
            mintemp = 5.0
            plante_vekst = maxtemp - mintemp
            if plante_vekst <= 0:
                dager_uten_vekst += 1
            else:
                aarlig_vekst.append(plante_vekst)


sum_vekst = sum(aarlig_vekst)
print(f'den totale planteveksten i {dato}, er {sum_vekst}mm')
print(f'dager i {dato} uten vekst: {dager_uten_vekst}')