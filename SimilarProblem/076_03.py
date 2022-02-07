from collections import deque

n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    JOI, IOI = 0, 0
    bool = [True] * n # bool[i] := i番目のお菓子を食べていない
    q = deque()

    for j in range(n):
        if j % 2 == 0:
            if j == 0:
                bool[i] = False
                JOI += a[i]
                q.append(((i + 1) % n, a[(i + 1) % n]))
                q.append(((i - 1) % n, a[(i - 1) % n]))
            else:
                x = q.popleft()
                y = q.popleft()
                if x[1] <= y[1]:
                    JOI += y[1]
                    bool[y[0]] = False
                    q.append(x)
                    if bool[(y[0] + 1) % n]:
                        q.append(((y[0] + 1) % n, a[(y[0] + 1) % n]))
                    elif bool[(y[0] - 1) % n]:
                        q.append(((y[0] - 1) % n, a[(y[0] - 1) % n]))
                elif x[1] >= y[1]:
                    JOI += x[1]
                    bool[x[0]] = False
                    q.append(y)
                    if bool[(x[0] + 1) % n]:
                        q.append(((x[0] + 1) % n, a[(x[0] + 1) % n]))
                    elif bool[(x[0] - 1) % n]:
                        q.append(((x[0] - 1) % n, a[(x[0] - 1) % n]))
        elif j % 2 == 1:
            x = q.popleft()
            y = q.popleft()
            if x[1] <= y[1]:
                IOI += y[1]
                bool[y[0]] = False
                q.append(x)
                if bool[(y[0] + 1) % n]:
                    q.append(((y[0] + 1) % n, a[(y[0] + 1) % n]))
                elif bool[(y[0] - 1) % n]:
                    q.append(((y[0] - 1) % n, a[(y[0] - 1) % n]))
            elif x[1] >= y[1]:
                IOI += x[1]
                bool[x[0]] = False
                q.append(y)
                if bool[(x[0] + 1) % n]:
                    q.append(((x[0] + 1) % n, a[(x[0] + 1) % n]))
                elif bool[(x[0] - 1) % n]:
                    q.append(((x[0] - 1) % n, a[(x[0] - 1) % n]))
    
    if ans < JOI:
        ans = JOI

print(ans)