#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/

# Imports
import sqlite3
from lambda_app_UI import * # Importeren menu's (UI)
import os #  Opschoonen van de termianl

# Program 

# Groet gebruiker tot de applicatie.
welcome()
input()
os.system('cls')
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


def get_modulesprop():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_propedeuse  ")
        print(cursor.fetchall())

get_modulesprop()

def get_modulesBI():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_BI  ")
        print(cursor.fetchall())

get_modulesBI()


def get_modulesDEV():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_DEV  ")
        print(cursor.fetchall())

get_modulesDEV()


def get_modulesSERV():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_SERV  ")
        print(cursor.fetchall())

get_modulesSERV()


def get_minors():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM externe_modules ")
        print(cursor.fetchall())

get_minors()



def studiebehoefteB1():
    found = 0 
    while found==0:
        studentnummer = input('Vul je studentnummer in')   
        with sqlite3.connect('studie.db') as db:
            cursor = db.cursor()
            find_user = ('SELECT * FROM studieplanB1 WHERE studentnummer = ?')
            cursor.execute(find_user,[(studentnummer)])

            if cursor.fetchall():
                print('studentnummer is niet correct')
            else:
                found = 1 

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB1(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB1()


def studiebehoefteB2():
    found = 0 
    while found==0:
        studentnummer = input('Vul je studentnummer in')   
        with sqlite3.connect('studie.db') as db:
            cursor = db.cursor()
            find_user = ('SELECT * FROM studieplanB2 WHERE studentnummer = ?')
            cursor.execute(find_user,[(studentnummer)])

            if cursor.fetchall():
                print('studentnummer is niet correct')
            else:
                found = 1 

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB2(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()

#studiebehoefteB2()

def studiebehoefteB3():
    found = 0 
    while found==0:
        studentnummer = input('Vul je studentnummer in')   
        with sqlite3.connect('studie.db') as db:
            cursor = db.cursor()
            find_user = ('SELECT * FROM studieplanB3 WHERE studentnummer = ?')
            cursor.execute(find_user,[(studentnummer)])

            if cursor.fetchall():
                print('studentnummer is niet correct')
            else:
                found = 1 

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB3(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB3()


def studiebehoefteB4():
    found = 0 
    while found==0:
        studentnummer = input('Vul je studentnummer in')   
        with sqlite3.connect('studie.db') as db:
            cursor = db.cursor()
            find_user = ('SELECT * FROM studieplanB4 WHERE studentnummer = ?')
            cursor.execute(find_user,[(studentnummer)])

            if cursor.fetchall():
                print('studentnummer is niet correct')
            else:
                found = 1 

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB4(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB4()



## Functie 0
### Afsluiten *

## Functie 1
###Opvragen aanbod onderwijseenheden (1a) *
## Functie 2
###Opvragen aanbod onderwijseenheden extern (1a) *
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





