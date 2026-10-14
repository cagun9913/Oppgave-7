# Tell antall sommerdager, høysommerdager og tropedager i det aktuelle året
# og skriv ut dette. En sommerdag er en dag med maksimaltemperatur over 20 grader. En
# høysommerdag har maksimaltemperatur over 25 grader og en tropedag har
# maksimaltemperatur over 30 grader.

filnavn = r'øvingsoppgave 7\Oppgave-7\sinnes_2014_2025_med_makstemperatur.csv'
dato = input('skriv inn et valgfritt år fra 2014-2025: ')

sommerdager = 0
høysommerdager = 0
tropedager = 0
kalde_dager = 0
with open(filnavn, 'r', encoding='utf-8') as fila:
    fila.readline()

    for linje in fila:
        data = linje.strip().split(';')
        if data[2].endswith(dato):
            if data[3] =='-':
                continue
            dagstemp = data[3]
            dagstemp = dagstemp.replace(',', '.')
            dagstemp = float(dagstemp)
            if 20 <= dagstemp < 25:
                sommerdager += 1
            elif 25 <= dagstemp < 30:
                høysommerdager += 1
            elif dagstemp >= 30:
                tropedager += 1
            else:
                kalde_dager += 1

print(f'antall sommerdager: {sommerdager} \nantall høysommerdager: {høysommerdager}')
print(f'antall tropedager: {tropedager} \nantall kalde dager: {kalde_dager}')