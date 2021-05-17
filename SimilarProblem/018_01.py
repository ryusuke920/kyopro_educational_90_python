import math
A, B, H, M = map(int,input().split())
print(math.sqrt((A ** 2) + (B ** 2) - 2 * A * B * math.cos(math.radians((30 * H) - (6 * M) + (M / 2)))))