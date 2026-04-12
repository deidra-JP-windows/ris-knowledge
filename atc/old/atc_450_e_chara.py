x = input()
y = input()
s = []
s.append(x)
s.append(y)
for i in range(10):
    s.append(s[-1] + s[-2])
print(s)