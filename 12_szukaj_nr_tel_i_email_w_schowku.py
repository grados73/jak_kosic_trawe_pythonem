#! python3

import pyperclip
import re

##WYRAŻENIE REGULARNE DOPASOWUJĄCE NUMER TELEFONU
phoneRegex = re.compile(r'''(
    (\d{3})         ##pierwsze 3 cyfry (1-3)
    (\s|-|\.)       ##separator
    (\d{3})         ##drugie 3 cyfry (4-6)
    (\s|-|\.)       ##separator
    (\d{3})         ##trzecie 3 cyfry (7-9)
)''', re.VERBOSE)

##WYRAŻENIE REGULARNE DOPASOWUJĄCE ADRES E-MAIL
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       ## nazwa użytkownika
    @                       ## Znak @ - wymagany
    [a-zA-Z0-9.-]+          ## Nazwa domeny
    (\.[a-zA-Z]{2,4})       ## kropka i identyfikator, np. '.com', '.pl'
)''', re.VERBOSE)

##WYSZUKIWANIE DOPASOOWAŃ W SCHOWKU
text = str(pyperclip.paste()) ## wklejenie zawartości schowka do zmiennej text
matches = [] ##pusta tablica na wyniki dopasowania
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

##KOPIOWANIE ZNALEZIONYCH NUMERÓW I EMAILI DO SCHOWKA
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka: ')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego numeru telefonu ani adresu email :( ')

input()
