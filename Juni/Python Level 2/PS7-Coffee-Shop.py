drinks = ["Coffee", "Decaf", "Vanilla Latte", "Mocha", "Hot Chocolate", "Iced Coffee", "Smoothie"]
prices = [2.50, 2.50, 4.00, 4.25, 3.00, 2.75, 5.25]

menu = {}
for i in range(len(drinks)):
    menu[drinks[i]] = prices[i]

print("Here is our menu!")

for drink in menu:
    print(drink + ": $" + str(menu[drink]))
