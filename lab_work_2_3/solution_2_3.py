"""
Generate string with lowercase and uppercase alphabet plus numbers
"""

string = 'HelloUsername1234'

"""
Print 1st symbol of string
"""

print(string[0])

"""
Print last symbol
"""

print(string[-1])

"""
Print 3rd from start and 3rd from the end
"""

print(string[2], string[-2])

"""
Slice first 8 symbols
"""

print(string[0:8])


"""
Print only symbols with index, which divides on 3 without remaining
"""

print(string[3:len(string):3])

"""
Print the symbol of the middle of the string text
"""
print(string[len(string)//2])

"""
Reverse text using slice
"""

print(string[::-1])
