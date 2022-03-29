def iterative_fibonacci(n):

    a = 0
    b = 1

    if n==1:
        print(a)

    elif n<=0:
        print("No negative values allowed.")

    elif n>11:
        print("Fibonacci is greater than 100")

    else:

        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c

            print(c)

iterative_fibonacci(6)
