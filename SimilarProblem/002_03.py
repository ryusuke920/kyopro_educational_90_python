n = int(input())
s = input()
A = [0] * (n + 1)
for i in range(n):
    if s[i] == "(":
        A[i + 1] += A[i] + 1
    else:
        A[i + 1] += A[i] - 1

ans_left = max(0, -min(A))
s = ans_left * "(" + s

# Aを初期化
A = [0] * (n + 1 + ans_left)
for i in range(n + ans_left):
    if s[i] == "(":
        A[i + 1] += A[i] + 1
    else:
        A[i + 1] += A[i] - 1

print(s + max(0, A[-1]) * ")")