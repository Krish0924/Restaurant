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

# Homework:
# Add 5%, 10%, 15%, and 20% tip
# Anything else you want to add 
def tip(total):
    # percentage / 100 = decimal
    print("The recommended tip is", 15 / 100 * total)

def tax(sub_total):
    eightpercent = 8 / 100 * sub_total
    print("your tax will be", eightpercent)
    return sub_total + eightpercent

item = input("Pick whatever you want from our overpriced menu!\n")
while True:
    if item in menu:
        sub_total = menu[item]
        print("all right that will be", sub_total)
        print("(waiter rubs fingers togther, asking for a tip)")
        tip(sub_total)
        t_i_p = float(input("what would you like to tip? "))
        total = t_i_p + sub_total + tax(sub_total)
        print("your total will be", total, "thank you very much for eating with us!")
        break
    else:
        print("Sorry that is on the menu. You're dumb, we only have", len(menu) ,"items. They are " + ", ".join(menu))
        item = input("Pick whatever you want from our overpriced menu!\n")
