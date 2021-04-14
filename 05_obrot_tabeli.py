grid = [['.', '.', '.', '.', '.', '.'], #1
        ['.', '0', '0', '.', '.', '.'], #2
        ['0', '0', '0', '0', '.', '.'], #3
        ['0', '0', '0', '0', '0', '.'], #4
        ['.', '0', '0', '0', '0', '0'], #5
        ['0', '0', '0', '0', '0', '.'], #6
        ['0', '0', '0', '0', '.', '.'], #7
        ['.', '0', '0', '.', '.', '.'], #8
        ['.', '.', '.', '.', '.', '.']] #9

def rysuj_270():
    for i in range(9):
        for j in range(6):
            print(grid[i][j], sep='', end='')
        print('', sep='')

while 1:
    TypWyswietlania = int(input("Jak chcesz wyswietlic serce? (0-0\', 1-90\', 2-180\', 3-270\', 4-end) :"))
    if TypWyswietlania == 4:
        break
    elif TypWyswietlania == 3:
        rysuj_270()






