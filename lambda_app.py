#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conform PEP8 http://pep8online.com/

# Imports
from lambda_app_UI import *  # Importeren menu's (UI)
from lambda_app_RQ import *  # Importeren menu's (RQ)
import os  # Opschoonen van de terminal

# Program

# Groet gebruiker tot de applicatie.
welcome()
input()
os.system('cls')
# Login scherm
login_msg()
login()
