menu = {
    "golden pizza": 70_000.00,
    "golden milkshake": 10_000.00,
    "golden steak": 30_000.00,
    "golden water": 25_000.00
}

def neatMenu(menu):
    for item in menu:
        print(item)
        print("\t" + str(menu[item]))
    

neatMenu(menu)
item = input("Pick whatever you want from our overpriced menu!\n")
while True:
    if item in menu:
        print("all right that will be", menu[item])
        print("(waiter rubs fingers togther, asking for a tip)")
        break
    else:
        print("Sorry that is on the menu. You're dumb, we only have", len(menu) ,"items. They are " + ", ".join(menu))
        item = input("Pick whatever you want from our overpriced menu!\n")
