import math
t = int(input())
l, x, y = map(int,input().split()) # 高さ・直大のx座標・直大のy座標
q = int(input())
for i in range(q):
    e = int(input())
    theta = e / t * 360 # 度数法
    """
    e8_xは常に固定(x = 0)
    e8_y = l/2 * sin(θ - π) = -l/2 * sin(θ)
    """
    e8_x, e8_y, e8_z = 0, -l / 2 * math.sin(math.radians(theta)), l / 2  - l / 2 * math.cos(math.radians(theta))
    dist = math.sqrt((e8_x - x) ** 2 + (e8_y - y) ** 2 + (e8_z - 0) ** 2)
    ans = math.degrees(math.asin(e8_z / dist))
    print(ans)