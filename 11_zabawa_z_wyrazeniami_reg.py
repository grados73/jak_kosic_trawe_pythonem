import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumberRegex.search("Moj numer telefonu to 608-110-658, kamil.")
print('Znaleziony numer telefonu to: ' + mo.group())