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


def login_msg():
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


def login_fail():
    print("""


Het ingevulde wachtwoord of gebruikersnaam is onjuist.
Druk op enter om opnieuw in te loggen.
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

+-------------------+    +-------------------+ 
|      Keuze 3      |    |      Keuze 4      | 
|  Toon Studieplan  |    |     Invoeren      | 
|                   |    |  studiebehoefte   | 
+-------------------+    +-------------------+ 



Kies uit: 0,1,2,3 of 4
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

+-------------------+    +-------------------+   
|      Keuze 3      |    |      Keuze 4      |   
|       Tonen       |    |     Goedkeuren    |   
|   Studieplannen   |    |   Studieplannen   |   
+-------------------+    +-------------------+   



Kies uit: 0,1,2,3,4 of 5
+---------------------------------------------------------------------+
""")


def menu_intern():
        print("""


            +----------------------------------------------+
            |                                              |
            |       In dit submenu kunt u kiezen uit:      |
            |             Propedeuze vakken                |
            |             IT-Service vakken                |
            |       Business Intelligence vakken           |
            |            IT-Development vakken             |
            |                                              |
            +----------------------------------------------+

+-------------------+    +-------------------+    +-------------------+
|      Keuze 0      |    |      Keuze 1      |    |      Keuze 2      |
|  Keer terug naar  |    | Propedeuze vakken |    | IT-Service vakken |
|      Hoofdmenu    |    |                   |    |                   |
+-------------------+    +-------------------+    +-------------------+

+-------------------+    +-------------------+   
|      Keuze 3      |    |      Keuze 4      |   
|      Business     |    |   IT-Development  |   
|Intelligence vakken|    |       vakken      |   
+-------------------+    +-------------------+   



Kies uit: 0,1,2,3 of 4
+---------------------------------------------------------------------+
""")


def overzicht_eind():
    print("""
Druk op enter om terug te keren naar het hoofd menu.
+---------------------------------------------------------------------+
""")


def overzicht_keuze_blok():
    print("""


+-------------------+    +-------------------+    +-------------------+
|      Keuze 0      |    |      Keuze 1      |    |      Keuze 2      |
|  Keer terug naar  |    |  Blok 1 invoeren  |    |  Blok 2 invoeren  |
|      Hoofdmenu    |    |   studiebehoefte  |    |   studiebehoefte  |
+-------------------+    +-------------------+    +-------------------+

+-------------------+    +-------------------+ 
|      Keuze 3      |    |      Keuze 4      | 
|  Blok 3 invoeren  |    |  Blok 4 invoeren  | 
|   studiebehoefte  |    |   studiebehoefte  | 
+-------------------+    +-------------------+ 



Kies uit: 0,1,2,3 of 4
+---------------------------------------------------------------------+
""")


def overzicht_keuze():
    print("""
Type in de code van het vak dat je wilt toevoegen, druk dan op enter.
+---------------------------------------------------------------------+
""")


def overzicht_keuze_slb_keuze_keuring():
    print("""
Type in de code van de student om zijn studieplan te keuren.
+---------------------------------------------------------------------+
""")


def overzicht_keuze_slb_keuring():
    print("""
Type in: "goedgekeurd" of "afgekeurd" om.
+---------------------------------------------------------------------+
""")


def keuze_blok():
    print("""
Type in: "1,2,3 en 4" voor het kiezen van een blok.
+---------------------------------------------------------------------+
""")
