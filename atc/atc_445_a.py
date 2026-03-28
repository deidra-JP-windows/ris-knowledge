def main():
    """Sの先頭の文字と末尾の文字が同じ文字かどうか判定する関数
    処理概要:
        1. 文字列 S をインプットする
        2. Sの先頭の文字と末尾の文字が同じ文字であれば "Yes" を、そうでなければ "No" を出力する
    補足：
        None
    前提:
        None
    条件:
        None
    制約:
        1. S は英小文字からなる長さ 2 以上 10 以下の文字列
    Args:
        None
    Inputs:
        S (str): 判定する文字列
    Prints:
        str: Sの先頭の文字と末尾の文字が同じ文字であれば "Yes" を、そうでなければ "No" を出力
    Returns:
        None
    """
    # 文字列 S をインプットする
    S = input()
    # 先頭の文字と末尾の文字が同じか判定する
    if S[0] == S[-1]:
        print("Yes")
    else:
        print("No")
    

# ローカル実行
if __name__ == "__main__":
    main()
