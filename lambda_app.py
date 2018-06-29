#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/

# Imports
from lambda_app_UI import * # Importeren menu's (UI)
from lambda_app_RQ import * # Importeren menu's (RQ)
import os #  Opschoonen van de termianl

# Program 

# Groet gebruiker tot de applicatie.
welcome()
input()
os.system('cls')
# Login scherm
login_msg()
login()

# Valideren
## Indien SLB = toon slb functies
## Indien STUDENT = toon student functies

# Toon menu op basis van functies


viewB2()

viewB3()

viewb4()


    

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





