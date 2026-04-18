# 桁数取得
def get_len(n):
    return len(str(n))

p = [[] for _ in range(10)]
# 10桁までの2^xを作っておく
t = 1
while t <= 10**9:
    p[get_len(t)].append(t)
    t *= 2

# 全部入れる
a = [set() for _ in range(10)]
for i in range(1,10):
    # i桁の良い整数を作る
    # いったん2^xをそのまま入れる
    for pp in p[i]:
        a[i].add(pp)
    # 合成してi桁になるやつ
    for j in range(1,i):
        # j桁の2-xを末尾に持ってきた良い整数を作る
        for pi in p[j]:
            # i-j桁の良い整数を列挙（今まで生成したものを使いまわす）
            # その良い整数の後ろに2^xをくっつける
            for pj in a[i-j]:
                a[i].add(pj * (10 ** j) + pi)

# 一つの配列に入れる
ans = []
for s in a:
    for i in s:
        ans.append(i)

# ソートしてn番目の数が答え
ans.sort()
n = int(input())
print(ans[n-1])
