#! python3

import pyperclip
import re

## WYRAŻENIA REGULARNE
### WYRAŻENIE REGULARNE SPRAWDZAJĄCE CZY ZAWIERA MAŁE LITERY
maleLiteryRegex = re.compile(r'[a-z]+')
### WYRAŻENIE REGULARNE SPRAWDZAJĄCE CZY ZAWIERA DUŻE LITERY
duzeLiteryRegex = re.compile(r'[A-Z]+')
### WYRAŻENIE REGULARNE SPRAWDZAJĄCE CZY ZAWIERA CYFRY
cyfryRegex = re.compile(r'[0-9]+')
### WYRAŻENIE REGULARNE SPRAWDZAJĄCE CZY ZAWIERA SPACJE
spacjeRegex = re.compile(r'\s+')

## SPRAWDZENIE SIŁY HASŁA ZNAJDUJĄCEGO SIĘ W SCHOWKU
while(1):
    text = str(pyperclip.paste()) ## wklejenie zawartości schowka do zmiennej text
    if len(text) < 8:
        print("Twoje hasło jest zbyt krótkie. Hasło musi zawierać przynajmniej 8 znaków!")
        break

    if  maleLiteryRegex.search(text) == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać małe litery!")
        break

    if duzeLiteryRegex.search(text) == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać duże litery!")
        break

    if cyfryRegex.search(text) == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać cyfry!")
        break

    if spacjeRegex.search(text) != None:
        print("Twoje hasło zawiera spacje lub inny znak biały, to niedozwolone!")
        break

    print("Twoje hasło jest wystarczająco silne.")
    break

