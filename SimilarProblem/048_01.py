import heapq
n, m = map(int,input().split())
a = list(map(lambda x: int(x) * (-1),input().split()))

heapq.heapify(a)
for _ in range(m):
    tmp = heapq.heappop(a)
    heapq.heappush(a, (-1) * (-tmp // 2))

print((-1) * sum(a))