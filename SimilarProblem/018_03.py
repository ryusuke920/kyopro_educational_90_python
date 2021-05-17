import math
a, b, x = map(int,input().split())
if x >= a ** 2 * b / 2:
    deg = (2 * (a * a * b - x)) / a ** 3
    print(math.degrees(math.atan(deg)))
else:
    deg = a * b * b / (2 * x)
    print(math.degrees(math.atan(deg)))