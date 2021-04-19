#! python3

while(1):
    liczba = int(input("Podaj liczbe przez ktora mam podzielic 50: "))
    try:
        wynik = 50.0 / liczba
        print("50 podzielone przez " + str(liczba) + " wynosi " + str(wynik) + "\n")
    except ZeroDivisionError:
        print("Nie dziel przez Zero! \n")
    if liczba == 777:
        break
