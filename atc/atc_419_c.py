n = int(input())
r = [0]*n
c = [0]*n
for i in range(n):
    r[i],c[i] = map(int,input().split())
rmax = max(r)
rmin = min(r)
cmax = max(c)
cmin = min(c)
ra = (rmax+rmin)//2
ca = (cmax+cmin)//2
ans = 0
for i in range(n):
    ans = max(ans,abs(r[i]-ra))
    ans = max(ans,abs(c[i]-ca))
print(ans)