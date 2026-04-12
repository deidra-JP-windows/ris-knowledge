# 入力は以下の形式で標準入力から与えられる。
# S A B X

def main():
    meters_run_distance, seconds_run_time, seconds_stop_time, seconds_end_time = map(int, input().split())

    cycle = seconds_run_time + seconds_stop_time
    full_cycles = seconds_end_time // cycle
    mooving_distance = full_cycles * meters_run_distance * seconds_run_time

    remainder = seconds_end_time % cycle
    mooving_distance += meters_run_distance * min(remainder, seconds_run_time)

    print(mooving_distance)


if __name__ == '__main__':
    main()