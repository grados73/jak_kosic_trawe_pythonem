tableData = [[ 'jabka', 'pomarancze', 'wisnie', 'banany'],
             ['Alicja', 'Bob', 'Karol', 'David'],
             ['psy', 'koty', 'losie', 'gesi'],
             ['ogorek', 'marchewka', 'rzodkiew', 'cebula']]

def printTable(table):
    ##obliczanie najdluzszego slowa w danym wierszu
    colWidth = [0] * len(table)
    for i in range(len(table)):
        for k in range(4):
            if len(table[i][k]) > colWidth[i]:
                colWidth[i] = len(table[i][k])
    print(colWidth)
    for i in range(4):
        for k in range(len(table)):
            if k < (len(table)-1):
                print((table[k][i]).rjust(colWidth[k]), sep='', end ='  ')
            else:
                print((table[k][i]).rjust(colWidth[k]), sep='', end ='\n')

printTable(tableData)