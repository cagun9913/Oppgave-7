# Finn og skriv ut lengde, startdato og sluttdato for den lengste
# sammenhengende perioden uten nedbør, hvor døgnnedbør er 0.

filnavn = r'øvingsoppgave 7\Oppgave-7\sinnes_2014_2025_med_makstemperatur.csv'

lengst_periode = 0
start_periode = ''
slutt_periode = ''

nå_lengde = 0
nå_start = ''

with open(filnavn, 'r', encoding='utf-8') as fila:
    fila.readline()

    for linje in fila:
        data = linje.strip().split(';')
        
        if data[5].strip() == '-' or data[5].strip() == '':
            continue

        nedbør = data[5]
        nedbør = nedbør.replace(',', '.')
        nedbør = float(nedbør)
        
        if nedbør == 0.0:
            if nå_lengde == 0:
                nå_start = data[2]

            nå_lengde += 1

            if nå_lengde > lengst_periode:
                lengst_periode =  nå_lengde
                start_periode = nå_start
                slutt_periode = data[2]
        else:
            nå_lengde = 0
            
print(f'lengste periode uten nedbør: {lengst_periode}.\ni perioden fra {start_periode} til {slutt_periode}')

                
                

                 
            

