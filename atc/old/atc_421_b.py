def main():
    number_list = [0] * 10
    number_list[0], number_list[1] = map(int, input().split())
    for i in range(2, 10):
        number = str(number_list[i - 2] + number_list[i - 1])
        number_list[i] = int(number[::-1])
    print(number_list[9])
main()
