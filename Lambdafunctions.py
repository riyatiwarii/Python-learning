# Lambda functions or anonymous functions

# add = lambda x: x+15
# print(add(10))
#
# mul = lambda x,y: x*y
# print(mul(12, 4))
#
# def add_no(x):
#     return x+15
# print( add_no(10))
#
# def mul(x,y):
#     return x*y
# print(12*4)

# A Python program to create a function that takes one argument, and that argument will be multiplied with
# an unknown given number.

# n = (int(input("Enter the no you want its multiples:\n")))
# def multino(n):
#     return lambda x: x*n
# doubler = multino(2)
# tripler = multino(3)
# quadrupler = multino(4)
# quintupler = multino(5)
# print("Double the number of 15 =", doubler(n))
# print("Triple the number of 15 =", tripler(n))
# print("Quadruple the number of 15 =", quadrupler(n))
# print("Quintuple the number of 15 =", quintupler(n))

# A Python program to sort a list of tuples using Lambda.
# subjects_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subjects_list.sort(key=lambda x:x[1])
# print(subjects_list)

# A Python program to sort a list of dictionaries using Lambda.
# cellmodels =[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#             {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# sorted_cellmodels = sorted(cellmodels, key= lambda x:x['color'])
# print(sorted_cellmodels)
# sorted_cellmodels = sorted(cellmodels, key= lambda x:x['model'])
# print(sorted_cellmodels)

