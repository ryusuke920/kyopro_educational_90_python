import math
n = int(input())
a, b = map(int,input().split())
c, d = map(int,input().split())
X, Y = (a + c) / 2, (b + d) / 2 # 円の中心座標
r = math.sqrt((a - X) ** 2 + (b - Y) ** 2) / 2 # 円の半径
u = complex(a, b) - complex(X, Y)
rad = 360 / n
theta = complex(math.cos(math.radians(rad)), math.sin(math.radians(rad)))
ans = u * theta + complex(X, Y)
print(ans.real, ans.imag)