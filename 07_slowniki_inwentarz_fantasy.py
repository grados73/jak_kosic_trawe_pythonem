import pprint

Inventory = {}
def displayInventory(inventory):
    print("Inwentarz: ")
    item_total = 0
    for itm, ilsc in inventory.items():
        print(ilsc, end=' ')
        print(itm)
        item_total = item_total + int(ilsc)
    print("Calkowita ilosc przedmiotow: " + str(item_total))

while 1:
    item = input("Podaj nazwe przedmiotu, ktory chcesz dodac do inwentarza(0 - koniec): ")
    if item == '0':
        break
    num = int(input("Podaj ilosc " + str(item)+ ", ktory chcesz dodac do inwentarza: "))
    if item not in Inventory:
        Inventory[item] = num
    else:
        Inventory[item] = Inventory[item] + num

displayInventory(Inventory)