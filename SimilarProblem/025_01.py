n = int(input())

def dfs(s, cnt): # 文字列, 出現する文字数
    if len(s) == n:
        print(s)
        return
    for i in range(cnt + 1):
        dfs(s + chr(ord("a") + i), max(cnt, i + 1))

dfs("a", 1)