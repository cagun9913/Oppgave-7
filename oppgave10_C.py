# Temperatursammenlikning: For hver værstasjon regn ut
# gjennomsnittstemperaturen hvert år det er nok data for det året. Det er nok data
# om det er data for minst 300 dager. Bruk disse gjennomsnittene til å plotte alle
# gjennomsnittstemperaturene for alle årene, separate kurver for hver værstasjon,
# årstall på x-aksen.

import csv
import matplotlib.pyplot as plt

fillister =('oslo_blindern_1954_2025_med_makstemperatur.csv',
        'roeros_1954_2025_med_makstemperatur.csv',
        'sinnes_2014_2025_med_makstemperatur.csv',
        'tromsoe_1954_2025_med_makstemperatur.csv',
        'vaernes_1954_2025_med_makstemperatur.csv',
        'venabu_1954_2025_med_makstemperatur.csv')

oslo_aardata = {}
roero_aardata = {}
sinnes_aardata = {}
tromsoe_aardata = {}
vaernes_aardata = {}
venabu_aardata = {}

with open(fillister[0], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in oslo_aardata:
                oslo_aardata[aardata] = []
                oslo_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            continue

    for aardata, gjennomsnittsdager in oslo_aardata. items():
        if len(gjennomsnittsdager) >= 300:
            gjennomsnittsdager = sum(gjennomsnittsdager) / len(gjennomsnittsdager)
    

with open(fillister[1], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in roero_aardata:
                roero_aardata[aardata] = []
                roero_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            pass

with open(fillister[2], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in sinnes_aardata:
                sinnes_aardata[aardata] = []
                sinnes_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            pass

with open(fillister[3], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in tromsoe_aardata:
                tromsoe_aardata[aardata] = []
                tromsoe_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            pass

with open(fillister[4], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in vaernes_aardata:
                vaernes_aardata[aardata] = []
                vaernes_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            pass

with open(fillister[5], 'r', encoding='utf-8') as fil:
    fil.readline()

    for linje in fil:
        data = linje.strip().split(';')
        if len(data[2]) < 4:
            continue
        aardata = int(data[2][-4:])
        
        if data[3] == '-' or data[4] == '-':
            continue
        try: 
            makstemp = float(data[3].replace(',', '.'))
            middeltemp = float(data[4].replace(',', '.'))

            gjennomsnittdag = (makstemp + middeltemp) / 2
            gjennomsnittdag = round(gjennomsnittdag, 1)

            if aardata not in venabu_aardata:
                venabu_aardata[aardata] = []
                venabu_aardata[aardata].append(gjennomsnittdag)

        except ValueError:
            pass


