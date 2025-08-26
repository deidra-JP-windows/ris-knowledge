n,m = map(int, input().split())
s = list(input())
t = list(input())
a = [0]*(n+1)
for i in range(m):wd
    l,r = map(int, input().split())
    l -= 1
    r -= 1
    a[l] += 1
    a[r+1] -= 1

for i in range(1,n+1):
    a[i] += a[i-1]

ans = []
for i in range(n):
    if a[i] % 2 == 0:
        ans.append(s[i])
    else:
        ans.append(t[i])

print(''.join(ans))
