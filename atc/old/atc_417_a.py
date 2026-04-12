# 英小文字からなる N 文字の文字列 S
## xadwdwda = S みたいな感じ N文字 = ここでは 8 文字
# S の先頭から A 文字、末尾から B 文字取り除いた N−A−B 文字の文字列を出力
## 
# 制約
## 1≤N≤20
## 0≤A
## 0≤B
## A+B<N
## S は英小文字からなる 
## N 文字の文字列
## N,A,B はすべて整数
# input 
# N A B
# S
n,a,b = map(int,input().split())
s = input()
print(s[a:n-b])
