# N+1 個の部屋が一列に並んでいる
# 部屋には 0 ~ N の番号がついている
# 部屋の間には N 個のドアがある
# ドアは 1 ~ N の番号がついている
# 各ドアについて鍵の状態を表す値 Li がある
# Li = 0 のときドア i の鍵は開いており、
# Li = 1 のときドア i の鍵は閉まっている
# 2 人の人がおり、1 人は部屋 0 に、もう1 人は部屋 N にいる
# ドア i の鍵が開いているときに限り、部屋 i−1 と部屋 i の間を移動することができる
# このとき、2 人のいずれも到達できない部屋の個数はいくつか

def main():
    number_of_rooms = int(input())
    door_states = "".join(list(input().split()))
    door_open = door_states.find("1")
    door_close = door_states.rfind("1")
    print(door_close - door_open)
main()
