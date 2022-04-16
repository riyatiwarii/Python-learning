numlist = [3, 5, 13, 7, 9, 29, 44]
odds = list(filter(lambda x: x%2!=0, numlist ))
print(odds)
square = list(map(lambda x: x*x, odds))
print(square)
from functools import reduce
sumnum = reduce(lambda x,y: x+y, square)
print(sumnum)