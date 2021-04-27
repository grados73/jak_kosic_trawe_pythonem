#! python3
## 12_szukaj_nr_tel_i_email_w_schowku.py

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
    (\.[a-zA-Z]{2-4})       ## kropka i identyfikator, np. '.com', '.pl'
)''', re.VERBOSE)

