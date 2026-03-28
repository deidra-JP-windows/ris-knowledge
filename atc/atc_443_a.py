def main():
    """文字列 S の末尾に s を追加した文字列を出力
    処理概要:
        1. 文字列 S をインプット
          - 前提の条件を満たさない場合 return で終了
        2. 文字列 S の末尾に s を追加した文字列を出力
    前提:
        : S は英小文字からなる長さ 1 以上 10 以下の文字列
    制約:
        1. 
    Args:
        None
    Inputs:
        S (str): 英小文字からなる文字列
    Prints:
        Int: 
    Returns:
        None
    """
    # 文字列 S をインプット
    S = input()
    if not (1 <= len(S) <= 10) or not S.islower():
        return
    # 文字列 S の末尾に s を追加した文字列を出力
    print(S + "s")


# ローカル実行
if __name__ == "__main__":
    main()