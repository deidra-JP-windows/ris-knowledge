def get_midpoint(a, b):
    """
    2つの整数a, bの中点を計算する関数。
    Args:
        a (int): 整数a
        b (int): 整数b
    Returns:
        float: aとbの中点
    """
    print(('start: get_midpoint()'))
    midpoint = (a + b) / 2
    print(('end: get_midpoint()'))
    return midpoint


def main():
    """
    2つの整数p, rの中点が第2の整数qと等しいかを判定するプログラム。
    3つの整数p, q, rを空白区切りで入力し、pとrの中点がqと等しい場合は"Yes"、そうでない場合は"No"を出力する。
    Args:
        None
    Returns:
        None
    """
    print(('start: main()'))
    print('Please enter three integers p, q, r separated by spaces:')
    p, q, r = map(int,input().split())
    if q == (get_midpoint(p, r)):
        print('Yes')
    else:
        print('No')
    print('end: main()')


main()
