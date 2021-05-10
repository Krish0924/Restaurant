menu = {
    "golden pizza": 70_000.00,
    "golden milkshake": 10_000.00,
    "golden steak": 30_000.00
}

def neatMenu(menu):
    for item in menu:
        print(item)
        print("\t" + str(menu[item]))

neatMenu(menu)
input("Pick whatever you want from our overpriced menu!")

