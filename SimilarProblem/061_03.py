from collections import deque

s = input()

q = deque()

turn = 1
l = 0
for i, j in enumerate(s):
    if j == 'R':
        turn *= -1
    elif j != 'R':
        if turn == 1:
            q.append(j)
        elif turn == -1:
            q.appendleft(j)
        l += 1
        while True:
            if l < 2:
                break
            if q[0] == q[1]:
                q.popleft()
                q.popleft()
                l -= 2
            elif q[-1] == q[-2]:
                q.pop()
                q.pop()
                l -= 2
            else:
                break

print(*list(q)[::turn], sep='')