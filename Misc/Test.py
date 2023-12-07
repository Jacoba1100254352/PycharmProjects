

netid = "jacobda2"
for letter in netid:
    print(hex(ord(letter)))


#led = 0b0001001100100100  # example: 0b0010010101110001
#print(bin((int(led) * 3) & int("0xffff", 16)))

# print(hex((int("0x7ff", 16) << 5) | int("0xff", 16)))

"""row = 17
col = 63
start_hex_val = "0x00008000"
print(hex((row << 9) + (col << 2) + int(start_hex_val, 16)))
print(hex(ord('$')))
print(hex(59))
print(chr(59))

start_hex_val = "0x00008000"
end_hex_val = "0x0000a2fc"

# Calculate the intermediate value
intermediate_val = int(end_hex_val, 16) - int(start_hex_val, 16)

# Extract col by dividing the intermediate value by 4 (since col was shifted by 2 bits) and taking the remainder
col = (intermediate_val >> 2) & 0x3f  # % 64

# Extract row by dividing the intermediate value by 512 (since row was shifted by 9 bits)
row = intermediate_val >> 9

print("row:", row)
print("col:", col)


print(bin(ord('j')))"""
