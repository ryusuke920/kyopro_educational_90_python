n = int(input())
s = input()

# dp[i] := i番目までの条件を満たす個数
dp = [0] * n

for i in range(1, len(s)):
    if dp[i - 1] == 0: # 初めて最初の文字以外の文字が現れた場合
        if s[i] != s[0]:
            dp[i] += i
            l = i
    elif s[i - 1] != s[i]: # １つ前の文字と異なる場合
        dp[i] += dp[i - 1] + i
        l = i
    elif s[i - 1] == s[i]: # １つ前の文字と一致する場合
        dp[i] += dp[i - 1] + l

print(dp[n - 1])