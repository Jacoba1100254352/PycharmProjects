bill = float(input("Enter your total bill amount, in dollars: "))
tipPercent = float(input("Enter the percent you would like to tip, as a decimal: "))

tip = bill * tipPercent

print("Your tip, rounded down to the nearest dollar: " + str(int(tip)))
print("Your tip, rounded down to the nearest cent: " + str("%.2f" % tip))
