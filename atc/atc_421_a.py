def main():
    number_of_rooms = input()
    name_list = []
    for i in range(int(number_of_rooms)):
        name = input()
        name_list.append(name)
    roomn_number, name = map(str, input().split())
    if name_list[int(roomn_number) - 1] == name:
        print("Yes")
    else:
        print("No")

main()