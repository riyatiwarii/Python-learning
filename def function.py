# a = 9
# b = 8
# c = sum((a,b))
# print(c)

# def function1(a,b):
#     """ This is a function which will calculate average of two numbers.
#     this function doesn't work for three numbers"""
#     average = (a+b)/2
#     return average
# v = function1(4,12)
# print(v)
# print(function1.__doc__)

# def my_function(a):
#     print(a+1/2)
#
# my_function(0)
# my_function(1)
# my_function(2)
# my_function(3)

# def my_function(*fruits):
#   print("The variety of fruits is " + str(fruits))
# my_function("Mango","Banana","Apple","Strawberry")

# def my_function(country="Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(a):
#     return 3 * a
# print(my_function(1))
# print(my_function(2))
# print(my_function(3))
# print(my_function(4))
# print(my_function(5))

# def funct(a, b, c):
#     return a*b*c
# print(funct(10, 20, 30))
# print(funct(20, 50, 60))
# print(funct(70, 80, 90))

from datetime import date
def get_age(birth_year, birth_month, birth_day):
    """Calculates age (in years) based on birth year, birth month, and birth day."""
    birth_date = date(birth_year, birth_month, birth_day)
    age = date.today() - birth_date
    age_years = age.days / 365.2425
    return age_years
print(get_age(2000,5,16))