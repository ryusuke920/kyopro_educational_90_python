import math
t = int(input())
l, x, y = map(int,input().split()) # 高さ・直大のx座標・直大のy座標
q = int(input())
chokudai_x, chokudai_y, chokudai_z = x, y, 0

for i in range(q):
    e = int(input())
    e = e % t
    if e != 0:
        r = 360 / (t / e)
    else:
        r = 0
    print(i,e,r)
    people_x = 0
    people_y = math.cos(r) * (l / 2)
    people_z = math.sin(r) * (l / 2)
    print(people_y,people_z)
    dist = math.sqrt((people_x - chokudai_x) ** 2 + (people_y - chokudai_y) ** 2 + (people_z - chokudai_z) ** 2)
    ans = math.asin(abs(people_z - chokudai_z) / dist)
    print(ans,dist)