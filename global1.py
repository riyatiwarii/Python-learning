# l = 15 #Global
# m = 6
# def function1(a):
#     # l = 7
#     m = 8
#     global l
#     l = l+45
#     print(l,m)
#     print(a, "It is printed.")
#
# function1("I wrote the code.")
# print(l,m)

# This function modifies the global variable 's'
# def f():
#     global s
#     s += ' GFG'
#     print(s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s)
# # Global Scope
# s = "Python is great!"
# f()
# # print(s)

# def func():
#     global x
#     x = "Python"
#     print(x)
#     s = "Tutorialspoint"
#     print(s)
# func()
# print(x)

# def calculation():
#     global a
#     a = 10
#     a = a*10
#     print(a)
# calculation()
# print(a)

def riya():
    a = 10
    def preeti():
        global a
        a = 15
    print("Before calling preeti:", a)
    preeti()
    print("After calling preeti:", a)

riya()
print(a)