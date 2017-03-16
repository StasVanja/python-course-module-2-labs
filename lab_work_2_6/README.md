##Laboratory Work 2.6.

####Description:

Write the code to do following:

- Generate two sets with not unique numbers and few symbols 
- Print 1st set 
- Create tuple from intersection of first and second set 
- Create tuple from difference first and second set 
- Slice first 3 symbols from first tuple 
- Print only symbols with numbers from second set 
- Reverse tuple using slice 
- Convert both tuples into list 

####Here is its solution code:

*solution_2_6.py*
```"""
Generate two sets with not unique numbers and few symbols
"""

set1 = set('hello-baddy1')
set2 = set('bye-bye2')

"""
Print 1st set
"""

print(set1)

"""
Create tuple from intersection of first and second set
"""


tuple1= tuple(set(set1)&set(set2))
print(tuple1)

"""
Create tuple from difference first and second set
"""

tuple2 = tuple(set1-set2)
print(tuple2)

"""
Slice first 3 symbols from first tuple
"""

print(tuple1[0:3])

"""
Print only symbols with numbers from second set
"""

digits = []
mylist = str(set1)+str(set2)


for symbol in mylist :
    try:digits.append(int(symbol))

    except ValueError:
        pass
print(digits)

"""
Reverse tuple using slice
"""

print(tuple1[::-1])
print(tuple2[::-1])

"""
Convert both tuples into list
"""

print(list(tuple1))
print(list(tuple2))

```