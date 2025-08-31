def solve(n, m, votes):
    score = [0] * n
    for vvv in zip(*votes):
        c0 = vvv.count('0')
        c1 = n - c0
        if c0 == 0 or c1 == 0:
            for i in range(n):
                score[i] += 1
            continue
        if c0 < c1:
            for i in range(n):
                if vvv[i] == '0':
                    score[i] += 1
        else:
            for i in range(n):
                if vvv[i] == '1':
                    score[i] += 1
    best = max(score)
    ans = [i for i, s in enumerate(score, start=1) if s == best]
    return ans


n, m = map(int, input().split())
votes = [input() for _ in range(n)]
ans = solve(n, m, votes)
print(*ans)
