def collatz(number):
    if(number %2 == 0):
        print(int(number / 2))
        return number / 2
    else:
        print(int(3*number + 1))
        return 3*number + 1

while 1:
    try:
        liczba = int(input("Podaj liczbe calkowita: "))
        break
    except ValueError:
        print("podana wartosc nie jest liczba calkowita")

while 1:
   if liczba == 1:
        break
   else:
        liczba = collatz(liczba)

