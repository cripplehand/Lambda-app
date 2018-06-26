# Mensen die deelnemen zijn weergegeven in een ander bestand. Zie teams.csv.
# De drie imports zijn nodig om de functies om gegevens uit het teams.csv document te halen en aan te passen.
# En om het script tijdelijke te pauzeren zodat niet alles direct wordt geprint.
import csv
import operator
import time
deelnemers = []
# Eerst wordt het bestand teams.csv geopen (readen).
try:
    bestand = open("teams.csv", "r")
# Maar als het bestand nog niet bestaat. Wordt deze aangemaakt en ook geopend.
except:
    bestand = open("teams.csv", "w")
    bestand = open("teams.csv", "r")


# Daadwerkelijk begin van het script.
print("""
+-----------------+
| Ingeladen teams |
|                 |
+-----------------+
""")
time.sleep(2.0)
for regel in bestand:
# Het '\n' commando zorgt ervoor dat het stukje informatie op een ander regel staat in het temas.csv document.    
    regel = regel.replace('\n', '')
# Daarna printen we de gedefinieerde waarden om aan te tonen dat ze zijn ingeladen.
    print(regel)
    velden = regel.split(",")
    for i in range(len(velden)):
        if velden[i].isdigit(): velden[i] = int(velden[i])
    deelnemers.append(velden)
# We sluiten het bestand direct omdat we niet constant gebruik maken van het document.
bestand.close()
deelnmrInd = -1
print("""
+-----------------+
""")
input("Druk op enter om naar het menu te gaan.")


# Daarna krijgt de gebruiker een menu waaruit kan worden gekozen.
doorgaan = True
while doorgaan:
    print ("""
            +----------------------------------------------+
            |                                              |
            | Welkom in het Centrale Rankinglist programma |
            | Dit programma is ontworpen voor de casus:    |
            |          LAN-Party Zuyd Hogeschool           |
            |           ~///Ontwikkelaars\\\\\\~              |
            | Eline Habets   Eline Martin   Wesley de Vree |
            |                                              |
            +----------------------------------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 0      |    |      Keuze 1      |    |      Keuze 2      |
|   Stop programma  |    | Invoeren teamnaam |    |  Teamnaam opslaan |
|                   |    |                   |    |                   |
+-------------------+    +-------------------+    +-------------------+

+-------------------+    +-------------------+
|      Keuze 3      |    |      Keuze 4      |
|    Team zoeken    |    |  Scores weergeven |
|                   |    |                   |
+-------------------+    +-------------------+



Typ bij:"Geef keuze" 0,1,2,3 of 4
+---------------------------------------------------------------------+

""")
# Afhankelijk van de keuze die is gemaakt, kiest het programma de juiste code en keert terug naar het begin.
    keuze = input("==> Geef keuze: ")
    if keuze.isdigit():
        keuze = int(keuze)


# Voor keuze 1, wordt eerst naar de team naam gevraagd, geprint wat nu in het geheugen hebben, en als laatste de score.
# Indien de gebruiker met: Ja/ja antwoord, wordt de loop herhaald.
        if keuze == 1:
            meerdeelnemers = True
            while meerdeelnemers:
                naam = input ("Naam Team: ")
                time.sleep(1.0)
                print(deelnemers)
                score = int(input("Geef Score: "))
                print("Indien de score dient te worden gewijzigt,\npas deze na het opslaan aan in het team.csv bestand")
                rij = [naam, score]
                deelnemers.append(rij)
                antw = input ("Nog een team invoeren? (Ja/Nee)")
                meerdeelnemers = antw in "jaJa"
            print("Vergeet niet de ingevoerde teams op te slaan met: '2'.")
            input("Druk op enter om naar het menu te gaan.")
            for d in deelnemers:
# Uiteindelijk printen we de volledige lijst van teams die met hun score zijn ingevoerd, om aan te tonen dat het in het geheugen staat.
                print(d)


# Voor keuze 2, wordt de nieuwe data opgeslagen in het .csv document. Met het print statement wordt de gebruiker geinformeerd dat het is opgeslagen.
        elif keuze == 2:
            bestand = open ("teams.csv", "w")
            for d in deelnemers:
                for i in range(0, len(d)-1):
                    bestand.write(str(d[i])+",")
                bestand.write(str(d[len(d) - 1]))
                bestand.write("\n")
            print("Gegevens successvol opgeslagen in team.csv bestand!")
            input("Druk op enter om naar het menu te gaan.")
# Zodra de data is opgeslagen sluiten we het bestand direct.
            bestand.close()


# Voor keuze 3, kan de gebruiker zoeken op een team en zijn score als resultaat krijgen. Voor resultaten die niet in de lijst staan wordt een melding gegeven.
        elif keuze == 3:
            deelnmrInd = -1
            naam = input("Geef de naam van het team(Let op: Hoofdlettergevoelig!): ")
            gevonden = False
            i = 0
# Door te zoeken of het resultaat er in staat, wordt de value verhoogd en uit de loop gesprongen.
            while not gevonden and i < len(deelnemers):
                if deelnemers[i][0] == naam:
                    gevonden = True
                else:
                    i = i + 1
            if gevonden:
                deelnmrInd = i
# Om de naam te printen.
            if deelnmrInd != -1:
                for i in range(0, len(deelnemers[deelnmrInd])):
                    print(deelnemers[deelnmrInd][i], end = "       ")
                print()
            else:
                 print("Team niet gevonden, controleer je spelling.") 
            input("Druk op enter om naar het menu te gaan.")


# En als laatste en belangrijkste, de keuze om de rankinglijst te weergeven volgorde van hoogste score naar laagste.
        elif keuze == 4:
            bestand = open('teams.csv','r')
            csv1 = csv.reader(bestand,delimiter=',')
            sort = sorted(csv1,reverse=True,key=lambda x:int(x[1]))
            for eachline in sort:
                print (eachline)
                bestand.close()
            input("Druk op enter om naar het menu te gaan.")


# Om het programma te sluiten wordt 0 gebruikt.
        elif keuze == 0:
            doorgaan = False
# Als er een foutieve keuze wordt ingetypt dan krijgt men deze foutmelding.
        else:
            print("Kies uit: 0,1,2,3 of 4.")


# Afsluiting programma.            
print ("Programma is afgesloten")
