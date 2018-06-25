#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/

# Imports
import sqlite3
from lambda_app_UI import * # Importeren menu's (UI)


# Program 

# Groet gebruiker tot de applicatie.
welcome()
input()
# Login scherm
login()
# Valideren
## Indien SLB = toon slb functies
## Indien STUDENT = toon student functies

# Toon menu op basis van functies

def aanmaken_db():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gebruiker(
    userID INTEGER PRIMARY KEY, 
    gebruikersnaam VARCHAR(20) NOT NULL,
    voornaam VARCHAR(20) NOT NULL,
    achternaam VARCHAR(20) NOT NULL,
    wachtwoord VARCHAR(20) NOT NULL);
    ''')
    
    cursor.execute('''
    INSERT INTO gebruiker(gebruikersnaam,voornaam,achternaam,wachtwoord)
    VALUES ('test_gebruiker','Bob','Snith','vogel')
    ''')

    db.commit()

    cursor.execute('SELECT * FROM gebruiker')
    print(cursor.fetchall())

def login():
    while True:
        gebruikersnaam = input('Vul u gebruikersnaam in: ')
        wachtwoord = input('Vul u wachtwoord in: ')
        with sqlite3.connect('studie.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM gebruiker WHERE gebruikersnaam = ? AND wachtwoord = ?')
        cursor.execute(find_user,[(gebruikersnaam),(wachtwoord)])
        results = cursor.fetchall()
        print(results)
        if results:
            for i in results:
                print('Welkom '+i[2])
            return ('Exit')
        else:
            print('gebruikersnaam en wachtwoord zijn niet correct')
            again = input('Wilt u opnieuw proberen? (y/n): ')
            if again.lower() == 'n':
                print('doei')
                time.sleep(1)
                return('Exit')

login()

## Functie 0
### Afsluiten

## Functie 1
###Opvragen aanbod onderwijseenheden (1a)
## Functie 2
###Opvragen aanbod onderwijseenheden extern (1a)
## Functie 3
###STUDENT ONLY:
###        invullen studieboefte op basis van de onderwijseenheden die beschikbaar zijn (kenniselementen)
## Functie 4
###STUDENT ONLY:
###    (Indien) studiebehoefte niet volledig is, kan exterene kenniselkementen gezocht worden (minors/courses) (2)
## Functie 5
###STUDENT ONLY:
###    het verkrijgen van een overzicht van wat hij/zij wilt volgen in het komend blok. (3)
## Functie 6
###SLB ONLY!:
###    goedkeuren/afkeuren voorlopige studiepad (4)





