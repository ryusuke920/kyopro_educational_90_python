import sys
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    for i in range(q):
        l = 0
        ans = 0
        cnt = 0
        for r in range(n):
            cnt += a[r]

            while cnt > x[i]:
                cnt -= a[l]
                l += 1

            ans += r - l + 1
        
        print(ans)


if __name__ == "__main__":
    main()