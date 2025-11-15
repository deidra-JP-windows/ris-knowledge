def get_factorial():
    """
    階乗の100桁までの階乗を計算する関数。
    Args:
        None
    Returns:
        set: 階乗の値を格納したセット
    """
    print('start: get_factorial()')
    threshold = 100
    indent_number = 1
    factorial_number = 1
    exp_set = set()
    while True:
        exp_set.add(factorial_number)
        indent_number += 1
        factorial_number = factorial_number * indent_number
        if factorial_number > threshold:
            break
        if len(exp_set) > 200:
            break
        if len(exp_set) == 0 or 0 in exp_set:
            break
    print(exp_set)
    print('end: get_factorial()')
    return exp_set


def main():
    """
    100桁目までの小数計算で、インプットで与えられた桁の数が何かを求めるプログラム。
    Args:
        None
    Returns:
        None
    """
    print(('start: main()'))
    print('Please enter an integer number:')
    number = int(input())
    exp_set = get_factorial()
    if number in exp_set:
        print(f'The Riville number exp {number} is: 1')
    else:
        print(f'The Riville number exp {number} is: 0')
    print('end: main()')


main()
