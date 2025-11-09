"""
Help the user calculate their tip at a restaurant. Ask the user for their total bill amount and what percent they would like to tip. Then, calculate the tip. Print out the tip rounded down to the nearest dollar, then rounded down to the nearest cent.

Note: To convert a string into a decimal value, use the function float(). To print out a float (decimal) rounded to two decimal points, use str("%.2f" % num), where num is the variable that stores the float.
"""

bill = float(input("Enter your total bill amount, in dollars: "))
tipPercent = float(input("Enter the percent you would like to tip, as a decimal: "))

tip = bill * tipPercent

print("Your tip, rounded down to the nearest dollar: " + str(int(tip)))
print("Your tip, rounded down to the nearest cent: " + str("%.2f" % tip))
