GOOGL = [1119.94, 1118.61, 1124.12, 1121.43, 1119.54, 1123.21, 1119.32, 1122.41, 1118.99, 1119.69, 1122.00]
AAPL = [177.38, 178.26, 175.22, 179.11, 173.99, 177.99, 175.32, 176.41, 174.59, 177.50, 175.0]
HD = [189.99, 184.26, 190.22, 189.11, 191.99, 188.99, 180.32, 189.14, 188.69, 183.42, 185.32]

print("GOOGL's most recent price: " + str(GOOGL[len(GOOGL) - 1]))
print("AAPL's most recent price: " + str(AAPL[len(AAPL) - 1]))
print("HD's most recent price: " + str(HD[len(HD) - 1]))

GOOGLsum = 0
for trade in GOOGL:
    GOOGLsum += trade
print("The average (mean) price for GOOGL is " + str(GOOGLsum / len(GOOGL)))

AAPLsum = 0
for trade in AAPL:
    AAPLsum += trade
print("The average (mean) price for AAPL is " + str(AAPLsum / len(AAPL)))

HDsum = 0
for trade in HD:
    HDsum += trade
print("The average (mean) price for HD is " + str(HDsum / len(HD)))
