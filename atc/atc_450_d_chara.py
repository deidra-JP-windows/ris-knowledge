n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    a[i] %= k

a.sort()
ans = a[-1] - a[0]
for i in range(n-1):
    ans = min(ans, a[i] + k - a[i+1])

print(ans)