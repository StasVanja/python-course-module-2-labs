"""
Generate list with lowercase and uppercase alphabet plus numbers
"""

mylist = ['H', 'E', 'L', 'l', 'o', '2', 8, 1, 9, 'b', 'Y', 'e']

"""
Print 1st symbol of list
"""

print(mylist[0])

"""
Print last symbol
"""

print(mylist[-1])

"""
Print 3rd from start and 3rd from the end
"""

print(mylist[2], mylist[-2])

"""
Slice first 10 symbols
"""

print(mylist[0:10])

"""
Print only symbols with index, which divides on 2 without remaining
"""

print(mylist[2:len(mylist):2])

"""
Print only integer values from list
"""

s = str(mylist)
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
"""
Reverse list using slice
"""

print(mylist[::-1])

"""
Convert base list into string
"""

print(str(mylist))

