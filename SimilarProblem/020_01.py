def float2int(FLOAT):
    return int(FLOAT.replace(".", "")), len(FLOAT) - FLOAT.index(".") - 1

a, b = map(str,input().split())
a = int(a)
x, y = float2int(b)
print(a * x // (10 ** y))