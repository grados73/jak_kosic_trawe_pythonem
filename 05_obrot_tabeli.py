grid = [['.', '.', '.', '.', '.', '.'], #1
        ['.', '0', '0', '.', '.', '.'], #2
        ['0', '0', '0', '0', '.', '.'], #3
        ['0', '0', '0', '0', '0', '.'], #4
        ['.', '0', '0', '0', '0', '0'], #5
        ['0', '0', '0', '0', '0', '.'], #6
        ['0', '0', '0', '0', '.', '.'], #7
        ['.', '0', '0', '.', '.', '.'], #8
        ['.', '.', '.', '.', '.', '.']] #9
def rysuj_0():
    for i in range(6):
        for j in range(9):
            print(grid[j][i], sep='', end='')
        print('', sep='')

def rysuj_90():
    for i in [8, 7, 6, 5, 4, 3, 2, 1, 0]:
        for j in [5, 4, 3, 2, 1, 0]:
            print(grid[i][j], sep='', end='')
        print('', sep='')

def rysuj_180():
    for i in [5, 4, 3, 2, 1, 0]:
        for j in [8, 7, 6, 5, 4, 3, 2, 1, 0]:
            print(grid[j][i], sep='', end='')
        print('', sep='')

def rysuj_270():
    for i in range(9):
        for j in range(6):
            print(grid[i][j], sep='', end='')
        print('', sep='')



while 1:
    TypWyswietlania = int(input("Jak chcesz wyswietlic serce? (0-0\', 1-90\', 2-180\', 3-270\', 4-end) :"))
    if TypWyswietlania == 4:
        break
    elif TypWyswietlania == 0:
        rysuj_0()
    elif TypWyswietlania == 1:
        rysuj_90()
    elif TypWyswietlania == 2:
        rysuj_180()
    elif TypWyswietlania == 3:
        rysuj_270()
    else:
        print("Podales zla wartosc, podaj wartosc z zakresu 0 - 4! ")

print("Dzieki za skorzystanie z programu, do zobaczenia!")





