def main():
    """L 以上 R 以下の整数がいくつあるか求める処理
    処理概要:
        1. 整数 L と R を半角スペース区切りで入力
        2. L 以上 R 以下の整数の個数を出力
    補足：
        1.
    前提:
        1. 
    条件:
        1. 
    制約:
        1. 入力される値は全て整数
        2. 1 ≤ L ≤ R ≤ 100
    Args:
        None
    Inputs:
        L (int): 下限値
        R (int): 上限値
    Prints:
        int: L 以上 R 以下の整数の個数
    Returns:
        None
    """
    # 整数 L と R を半角スペース区切りで入力
    L, R = map(int, input().split())
    # L 以上 R 以下の整数の個数を出力
    print(R - L + 1)


# ローカル実行
if __name__ == "__main__":
    main()
