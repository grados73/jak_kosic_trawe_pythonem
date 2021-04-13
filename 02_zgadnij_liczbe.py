import random
naMysli = random.randint(1,20)
licznik = 0
print("Mam na myśli pewną liczbę z zakresu od 1 do 20.")
while 1:
    liczba = int(input("Spróbuj zgadnąć liczbę  "))
    licznik = licznik + 1
    if(liczba == naMysli):
        print("doskonale odgadnąłeś liczbę w ciągu", licznik, "prób")
        break
    elif(liczba>naMysli):
        print("Podana liczba jest za duża")
    else:
        print("podana liczba jest za mała")

input()