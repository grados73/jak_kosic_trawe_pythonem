message = ' kamil 608-110-658 , zuza, motyl 697 334 828'

def isPhoneNumber(text):
        if len(text) != 11:
            return False
        for k in range(0, 3):
            if not text[k].isdecimal():
                return False
        if (text[3] != '-' and text[3] != ' '):
            return False
        for l in range(4, 7):
            if not text[l].isdecimal():
                return False
        if (text[7] != '-' and text[7] != ' '):
            return False
        for m in range (8, 11):
            if not text[m].isdecimal():
                return False
        return True


for i in range(len(message)-10):
    ciagOperacyjny = message[i:i + 11]
    if isPhoneNumber(ciagOperacyjny):
        print("Znaleziony numer telefonu to: " + ciagOperacyjny)
print("Koniec szukania")
