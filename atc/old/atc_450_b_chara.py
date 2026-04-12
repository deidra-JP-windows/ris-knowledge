n = int(input())
c = [list(map(int,input().split())) for _ in range(n-1)]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if c[i][k-i-1] > c[i][j-i-1] + c[j][k-j-1]:
                print("Yes")
                exit()
print("No")