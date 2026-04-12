# 入力は以下の形式で標準入力から与えられる。
# x_age, y_age, rate
def main():
    x_age, y_age, rate = map(int, input().split())
    for n in range(0, x_age * rate):
        if x_age + n == rate * (y_age + n):
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
