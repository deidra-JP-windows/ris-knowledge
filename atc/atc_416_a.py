# o と x からなる長さ N の文字列がある
# 制約
## N は 1 以上 100 以下
## L は 1 以上 R 以下
## R は L 以上 N 以下
## N,L,R は全て整数
# S の L 文字目から R 文字目までが全て o であるかどうか判定
n,l,r = map(int,input().split())
s = input()
if all(c == 'o' for c in s[l-1:r]):
    print("Yes")
else:
    print("No")
