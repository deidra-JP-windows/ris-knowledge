n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = []
for i in a:
    if len(i) == 1:
        print(min(b))
        b.remove(min(b))
    if len(i) == 2:
        b.append(i[1])
