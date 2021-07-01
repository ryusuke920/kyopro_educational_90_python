a, b = map(int,input().split())

if a > 0:
    print("Positive")
elif a == 0:
    print(0)
else:
    if b >= 0:
        print("Zero")
    else:
        cnt = a - b + 1
        if cnt % 2 == 0:
            print("Positive")
        else:
            print("Negative")