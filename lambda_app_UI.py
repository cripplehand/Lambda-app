
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/


def welcome():
    print("""


+---------------------------------------------------------------------+
|                                                                     |
|  Welkom in het Studieplan registratie systeem.                      |
|                                                                     |
|  In dit systeem kan worden opgevraagd                               |
|  welke onderwijseenheden Hogeschool ZUYD biedt.                     |
|                                                                     |
|  Tevens kan een student zijn studiebehoeftes invullen.              |
|                                                                     |
|  Indien de student zich wil inschrijven voor                        |
|  externe of minors, kan dit ook in dit programma.                   |
|                                                                     |
|  De student kan dan zijn studieplan opslaan,                        |
|  zodat zijn SLB’er deze kan reviewen.                               |
|                                                                     |
+---------------------------------------------------------------------+



Druk op enter om naar het inlog scherm te gaan.
+---------------------------------------------------------------------+
""")

def login():
    print("""


+---------------------------------------------------------------------+
|                                                                     |
|  Login met je gebruikers naam en wachtwoord die je                  |
|                                                                     |
|  Voorbeeld van een gebruikersnaam: bram.sonsbeek123456              |
|  Het wachtwoord dien je zelf te weten, anders kun je deze           |
|                                                                     |  
|  Resetten via het betreffende van hogeschool ZUYD.                  |
|  Tevens kan een student zijn studiebehoeftes invullen.              |
|                                                                     |
+---------------------------------------------------------------------+



Vul je gebruikersnaam in. Vervolgens druk op enter. Voer dan je
wachtwoord in. Indien je deze fout hebt wordt de invoer hier getoont.
+---------------------------------------------------------------------+
""")


def mainmenu_student():
    print("""


            +----------------------------------------------+
            |                                              |
            | Welkom in het Studieplan registratie systeem |
            |   Dit programma is ontworpen voor de casus:  |
            |        Moodle Studiepad Zuyd Hogeschool      |
            |           ~///Ontwikkelaars\\\\\~              |
            |       Camiel Frijns & Wesley de Vree         |
            |                                              |
            +----------------------------------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 0      |    |      Keuze 1      |    |      Keuze 2      |
|   Stop programma  |    |     Opvragen      |    | Opvragen externe  |
|                   |    | Onderwijseenheden |    | Onderwijseenheden |
+-------------------+    +-------------------+    +-------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 3      |    |      Keuze 4      |    |      Keuze 5      |
|  Toon Studieplan  |    |     Invoeren      |    | Invoeren externe  |
|                   |    |  studiebehoefte   |    |  studiebehoefte   |
+-------------------+    +-------------------+    +-------------------+



Kies uit: 0,1,2,3,4 of 5
+---------------------------------------------------------------------+
""")


def mainmenu_slb():
    print("""


            +----------------------------------------------+
            |                                              |
            | Welkom in het Studieplan registratie systeem |
            |   Dit programma is ontworpen voor de casus:  |
            |        Moodle Studiepad Zuyd Hogeschool      |
            |           ~///Ontwikkelaars\\\\\~              |
            |       Camiel Frijns & Wesley de Vree         |
            |                                              |
            +----------------------------------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 0      |    |      Keuze 1      |    |      Keuze 2      |
|   Stop programma  |    |     Opvragen      |    | Opvragen externe  |
|                   |    | Onderwijseenheden |    | Onderwijseenheden |
+-------------------+    +-------------------+    +-------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 3      |    |      Keuze 4      |    |      Keuze 5      |
|       Tonen       |    |     Goedkeuren    |    |       ???         |
|   Studieplannen   |    |   Studieplannen   |    |                   |
+-------------------+    +-------------------+    +-------------------+



Kies uit: 0,1,2,3,4 of 5
+---------------------------------------------------------------------+
""")


#  input()
#  welcome()
#  input()
#  mainmenu_student()
#  input()
#  mainmenu_slb()
#  input()
#  login()
#  input()
