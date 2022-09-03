fibonacciList = [0, 1]
# finding 10 terms of the series starting from 3rd term
N = int(input("Enter the no. of terms: \n"))
for term in range(3, N + 1):
    value = fibonacciList[term - 3] + fibonacciList[term - 2]
    fibonacciList.append(value)
print(f"{N} terms of the fibonacci series are:")
print(fibonacciList)