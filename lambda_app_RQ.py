#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/

# Imports
import sqlite3
import os #  Opschoonen van de termianl
from lambda_app_UI import * 

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
        global gebruikersnaam
        global wachtwoord
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
                status = ('SELECT functie FROM gebruiker WHERE gebruikersnaam = ? AND wachtwoord = ?')
                cursor.execute(find_user,[(gebruikersnaam),(wachtwoord)])
                resultaten = cursor.fetchone()[6]
                status = ('SELECT functie FROM gebruiker WHERE gebruikersnaam = ? AND wachtwoord = ?')
                cursor.execute(find_user,[(gebruikersnaam),(wachtwoord)])
                studentnummer = cursor.fetchone()[1]
                if resultaten == 'student':
                   run = True
                   while run:
                       mainmenu_student()
                       keuze = input('maak je keuze: ')
                       if keuze == '0':
                           run = False
                           exit
                       elif keuze == '1':
                          menu_intern()
                          run_sub = True
                          while run_sub:
                              keuze = input('maak je keuze: ')
                              if keuze == '0':
                                  run_sub = False
                              elif keuze == '1':
                                  get_modulesprop()
                              elif keuze == '2':
                                  get_modulesSERV()
                              elif keuze == '3':
                                  get_modulesBI()
                              elif keuze == '4':
                                  get_modulesDEV()
                       elif keuze == '2':
                          get_minors()
                       elif keuze == '3':
                          keuze_blok()
                          run_sub = True
                          while run_sub:
                              keuze = input('maak je keuze: ')
                              if keuze == '0':
                                  run_sub = False
                              elif keuze == '1':
                                  viewB1()
                              elif keuze == '2':
                                  viewB2()
                              elif keuze == '3':
                                  viewB3()
                              elif keuze == '4':
                                  viewB4()
                       elif keuze == '4':
                          overzicht_keuze_blok()
                          run_sub = True
                          while run_sub:
                              keuze = input('maak je keuze: ')
                              if keuze == '0':
                                  run_sub = False
                              elif keuze == '1':
                                  studiebehoefteB1(studentnummer)
                              elif keuze == '2':
                                  studiebehoefteB2(studentnummer)
                              elif keuze == '3':
                                  studiebehoefteB3(studentnummer)
                              elif keuze == '4':
                                  studiebehoefteB4(studentnummer)
                                      
                       
                elif resultaten == 'slb':
                   run = True
                   mainmenu_slb()
                   keuze = input('maak je keuze: ')
                   while run:
                       if keuze == '0':
                           run_sub = False
                       elif keuze == '1':
                           menu_intern()
                           run_sub = True
                           while run_sub:
                               keuze = input('maak je keuze: ')
                               if keuze == '0':
                                   run_sub = False
                               elif keuze == '1':
                                   get_modulesprop()
                               elif keuze == '2':
                                   get_modulesSERV()
                               elif keuze == '3':
                                   get_modulesBI()
                               elif keuze == '4':
                                   get_modulesDEV()
                       elif keuze == '2':
                           get_minors()
                       elif keuze == '3':
                           keuze_blok()
                           run_sub = True
                           while run_sub:
                               keuze = input('maak je keuze: ')
                               if keuze == '0':
                                   run_sub = False
                               elif keuze == '1':
                                   viewB1()
                               elif keuze == '2':
                                   viewB2()
                               elif keuze == '3':
                                   viewB3()
                               elif keuze == '4':
                                   viewB4()
                       elif keuze == '4':
                           keuze_blok()
                           run_sub = True
                           while run_sub:
                               keuze = input('maak je keuze: ')
                               if keuze == '0':
                                   run_sub = False
                               elif keuze == '1':
                                   goedkeuringB1()
                                   run_sub = False
                               elif keuze == '2':
                                   goedkeuringB2()
                               elif keuze == '3':
                                   goedkeuringB3()
                               elif keuze == '4':
                                   goedkeuringB4()

            return ('Exit')
        else:
            print('gebruikersnaam en wachtwoord zijn niet correct')
            again = input('Wilt u opnieuw proberen? (y/n): ')
            if again.lower() == 'n':
                print('doei')
                time.sleep(1)
                return('Exit')





def get_modulesprop():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_propedeuse  ")
        print(cursor.fetchall())

#get_modulesprop()

def get_modulesBI():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_BI  ")
        print(cursor.fetchall())

#get_modulesBI()


def get_modulesDEV():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_DEV  ")
        print(cursor.fetchall())

#get_modulesDEV()


def get_modulesSERV():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM modules_SERV  ")
        print(cursor.fetchall())

#get_modulesSERV()


def get_minors():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM externe_modules ")
        print(cursor.fetchall())

#get_minors()



def studiebehoefteB1(studentnummer):
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB1(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB1()


def studiebehoefteB2(studentnummer):
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB2(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()

#studiebehoefteB2()

def studiebehoefteB3(studentnummer):
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB3(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB3()


def studiebehoefteB4(studentnummer):
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    vak_1 = input('Vul je eerste vak in: ')
    vak_2 = input('Vul je tweede vak in:')
    vak_3 = input('Vul je derde vak in: ')
    

    insertData = '''INSERT INTO studieplanB4(studentnummer,vak_1,vak_2,vak_3)
    VALUES(?,?,?,?)''' 
    cursor.execute(insertData, [(studentnummer),(vak_1),(vak_2),(vak_3)])
    db.commit()


#studiebehoefteB4()


def viewB1():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM studieplanB1 ")
        print(cursor.fetchall())

#viewB1()


def viewB2():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM studieplanB2 ")
        print(cursor.fetchall())



def viewB3():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM studieplanB3 ")
        print(cursor.fetchall())



def viewB4():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM studieplanB4 ")
        print(cursor.fetchall())





#def goedkeuringB1(studentnummer):
    #with sqlite3.connect('studie.db') as db:
        #cursor = db.cursor()

   # studentnummer == input('vul het studentnummer in van de student: ')
    #status = input('keur het studieplan van blok 1 goed of af: ')
    #insertData = '''INSERT INTO studieplanB1 (status) WHERE studentnummer == studentnummer
    #VALUES(?)''' 
    #cursor.execute(insertData, (status))
    #db.commit()

 

#goedkeuringB1()

def goedkeuringB1():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    studentnummer = input('wat is het studentnummer: ')
    status = input('keur het studieplan van blok 1 goed of af: ')
    cursor.execute("UPDATE studieplanB1 SET status=(?) WHERE studentnummer = (?)", (status, studentnummer))
    db.commit()



def goedkeuringB2():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    studentnummer = input('wat is het studentnummer: ')
    status = input('keur het studieplan van blok 2 goed of af: ')
    cursor.execute("UPDATE studieplanB2 SET status=(?) WHERE studentnummer = (?)", (status, studentnummer))
    db.commit()


def goedkeuringB3():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    studentnummer = input('wat is het studentnummer: ')
    status = input('keur het studieplan van blok 3 goed of af: ')
    cursor.execute("UPDATE studieplanB3 SET status=(?) WHERE studentnummer = (?)", (status, studentnummer))
    db.commit()



def goedkeuringB4():
    with sqlite3.connect('studie.db') as db:
        cursor = db.cursor()

    studentnummer = input('wat is het studentnummer: ')
    status = input('keur het studieplan van blok 4 goed of af: ')
    cursor.execute("UPDATE studieplanB4 SET status=(?) WHERE studentnummer = (?)", (status, studentnummer))
    db.commit()


## Functie 0
### Afsluiten *

## Functie 1
###Opvragen aanbod onderwijseenheden (1a) *
## Functie 2
###Opvragen aanbod onderwijseenheden extern (1a) *
## Functie 3
###STUDENT ONLY:
###        invullen studieboefte op basis van de onderwijseenheden die beschikbaar zijn (kenniselementen) * 
## Functie 4
###STUDENT ONLY:
###    (Indien) studiebehoefte niet volledig is, kan exterene kenniselkementen gezocht worden (minors/courses) (2) * 
## Functie 5
###STUDENT ONLY:
###    het verkrijgen van een overzicht van wat hij/zij wilt volgen in het komend blok. (3) * 
## Functie 6
###SLB ONLY!:
###    goedkeuren/afkeuren voorlopige studiepad (4)





