
def factorial_iterative(n):

    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):

    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

number = int(input("Enter the number\n"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))

def series(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (series(n-1) + series(n-2))
num = int(input("Term you want = "))
for i in range(num):
    print(series(i+1), end = " ")

# Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = int(input("Enter nth term\n"))

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))
