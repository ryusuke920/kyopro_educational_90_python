from collections import deque
n, k = map(int,input().split())
s = input()
q = deque()
word = ""
for i, j in enumerate(s):

    # 追加するものよりも、qの中身の数字の方が大きければ、qの中身を捨てる
    while q and q[-1] > j:
        q.pop()
    q.append(j)

    # ここから最後まで１文字ずつ追加していく
    if i >= n - k:
        word += q.popleft()

print(word)