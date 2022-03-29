def recursive_fac(n):

    if n == 0:
        return 1
    else:
        return n * recursive_fac(n-1)

result = recursive_fac(5)
print(result)
