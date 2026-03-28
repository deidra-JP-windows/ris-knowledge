def main():
    """すべての桁の数字が同じであるかどうかを判定
    処理概要:
        1.3 桁の正整数 N をインプットする
        2. すべての桁の数字が同じであるかどうかを判定し、結果を出力する
    前提:
        None 
    制約:
        1.N を十進法の 3 桁の正整数とする
    Args:
        None
    Inputs:
        N (int): 3 桁の正整数
    Prints:
        str: Yes または No
    Returns:
        None
    """
    # 3 桁の正整数 N をインプットする
    N = input()
    # すべての桁の数字が同じであるかどうかを判定し、結果を出力する
    if N[0] == N[1] == N[2]:
        print("Yes")
    else:
        print("No")


# ローカル実行
if __name__ == "__main__":
    main()