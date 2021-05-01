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
