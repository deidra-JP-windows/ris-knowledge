s = input()
m = 0.00
for i in range(len(s)):
    if s[i] != "t":
        continue 
    for j in range(i+2, len(s)):
        if s[j] != 't':
            continue
        o = s[i:j+1]
        x = o.count('t')
        l = len(o)
        r = (x - 2) / (l - 2)
        m = max(m, r)
print(f"{m:.9f}")
