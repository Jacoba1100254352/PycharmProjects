d = {
    'd2': {'d3': {'d4': 'eight'}},
    'l3': [1, 'two'],
    't2': ('three', ('four', ('five', 6))),
    'l2': ['six', {'d5': 'seven'}],
    's2': 'one'
}

# print "one"
print(d['s2'])

# print "two"
print(d['l3'][1])

# print "three"
print(d['t2'][0])

# print "four"
print(d['t2'][1][0])

# print "five"
print(d['t2'][1][1][0])

# print "six"
print(d['l2'][0])

# print "seven"
print(d['l2'][1]['d5'])

# print "eight"
print(d['d2']['d3']['d4'])
