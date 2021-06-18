from math import factorial
n = int(input())
a = factorial(n - 1)
b = factorial(11)
c = factorial(n - 12)
print(a // (b * c))