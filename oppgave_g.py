import csv
filsti = r"sinnes_2014_2025.csv"

# Navn; ID, dato, middeltemp, nedbør, middelvind, snødybde

max_length = 0
max_start = None
max_end = None

current_length = 0
current_start = None
current_end = None

try:            ## Prøver en try i tilfelle den ikke finner fila.
    with open(filsti, encoding="utf-8") as file:    ##Åpner fila
        reader = csv.reader(file, delimiter=";")    ##Bruker csv reader for å lage et objekt som har contentet av fila.

        for row in reader:      ##Leser innhold linje for linje
            if not row or len(row) < 5:     ##SJekker om linja har riktig antall datapunkter. Hvis ikke hopper den over
                continue

            dato = row[2].strip()       ##Setter midl. objekt dato = datapunkt nr [2] (3)
            nedbor_str = row[4].strip() ##Samma med nedbørsmengden.

            try:                #Forsøker å sette nedbøret til et flyt-tall.
                nedbor = float(nedbor_str.replace("," , "."))   ##Innebygd replacement av , med .
            except ValueError:  #Hvis det ikke er et tall, vil den starte ny "tørkeperiode"
                current_length = 0
                current_start = None
                current_end = None
                continue

            if nedbor == 0:     #Sjekker om nedbør er lik null
                if current_length == 0: #Sjekker om vi er på en ny tørkeperiode eller ikke
                    current_start = dato    #Hvis ja: Setter startdatoen til denne radens dato
                current_length += 1         #Legger så til en på lengden på tørkeperioden
                current_end = dato          #Setter sluttdato. Vil fortsette å gjøre dette for hver rad

                if current_length > max_length: #Sjekker om denne perioden er lengre enn max-perioden.. Hvis ja:
                    max_length = current_length #Hvis ja setter den maxlengde og datoer lik denne perioden
                    max_start = current_start
                    max_end = current_end
            else:
                current_length = 0      #Hvis nedbør IKKE er null
                current_start = None    #Så resetter den datoer og lengden.
                current_end = None      #Mens max-perioden er fortsatt lagret i "max_xxx"

except FileNotFoundError:
    print("Fant ikke fila. Sjekk at stien er riktig og at du kjører scriptet fra riktig mappe.")
    exit()


print("Lengste sammenhengende periode uten nedbør:")
print(f"Lengde: {max_length} dager")
print(f"Startdato: {max_start}")
print(f"Sluttdato: {max_end}")