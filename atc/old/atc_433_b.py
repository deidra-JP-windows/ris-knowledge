# 入力は以下の形式で標準入力から与えられる。
# number_of_people, height_1 height_2 ... height_number_of_people
def main():
    number_of_people = int(input())
    height = list(map(int, input().split()))
    for i in range(number_of_people):
        if i > 0:
            for j in range(i-1, -1, -1):
                if height[j] > height[i]:
                    print(j + 1)
                    break
            else:
                print("-1")
        else:
            print("-1")

if __name__ == '__main__':
    main()
