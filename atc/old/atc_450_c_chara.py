from collections import deque
h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
q = deque()
for i in range(h):
    if s[i][0] == ".":
        q.append((i,0))
    if s[i][w-1] == ".":
        q.append((i,w-1))
for j in range(w):
    if s[0][j] == ".":
        q.append((0,j))
    if s[h-1][j] == ".":
        q.append((h-1,j))

def bfs(s,q):
    while q:
        i,j = q.popleft()
        s[i][j] = "#"
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = i+di,j+dj
            if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == ".":
                s[ni][nj] = "#"
                q.append((ni,nj))

bfs(s,q)

q.clear()
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            q.append((i,j))
            bfs(s,q)
            ans += 1
print(ans)
