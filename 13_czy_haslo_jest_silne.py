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

## SPRAWDZENIE SIŁY HASŁA ZNAJDUJĄCEGO SIĘ W SCHOWKU
while(1):
    text = str(pyperclip.paste()) ## wklejenie zawartości schowka do zmiennej text
    if len(text) < 8:
        print("Twoje hasło jest zbyt krótkie. Hasło musi zawierać przynajmniej 8 znaków!")
        break

    mo1 = maleLiteryRegex.search(text)
    if  mo1 == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać małe litery!")
        break

    mo2 = duzeLiteryRegex.search(text)
    if mo2 == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać duże litery!")
        break

    mo3 = cyfryRegex.search(text)
    if mo3 == None:
        print("Twoje hasło jest słabe. Hasło musi zawierać cyfry!")
        break
    print("Twoje hasło jest wystarczająco silne.")
    break

