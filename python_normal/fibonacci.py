def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fib(i), end=" ")


n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b