def main():
    """文字列のパース処理_先頭の連続する o 除去
    処理概要:
        1. 文字列の長さ N を入力
        2. 文字列 S を入力
        3. 文字列 S から 先頭の連続する o を除去
        4. パース処理後の文字列 S を出力
    補足：
        1.
    前提:
        1. 
    条件:
        1. S が全て o の場合は、空文字列を出力  
    制約:
        1. 1 ≤ N ≤ 50
        2. S は英小文字からなる長さ N の文字列
    Args:
        None
    Inputs:
        N (int): 文字列 S の長さ
        S (str): 文字列
    Prints:
        str: パース処理後の文字列 S
    Returns:
        None
    """
    # 文字列の長さ N を入力
    N = int(input())
    # 文字列 S を入力
    S = input()
    # 文字列 S から 先頭の連続する o を除去
    S = S.lstrip("o")
    # パース処理後の文字列 S を出力
    print(S)


# ローカル実行
if __name__ == "__main__":
    main()
