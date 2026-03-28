def main():
    """N 以下の正整数のうち、桁和が K であるものの個数を出力
    処理概要:
        1. 正数 N と桁和 K をインプットする
        2. N 以下の正整数のうち、各桁の値の和が K である正整数の個数をカウントし出力する
          1. N を桁ごとのリストに変換
          2. 桁ごとのリストから各桁の値の和を計算する
    前提:
        1. 正整数 n の桁和を、n を十進法で表したときの各桁の和とする
          - 例: 2026 の桁和は 2 + 0 + 2 + 6 = 10 
    制約:
        1. 1 ≤ N
        2. K ≤ 10^5
    Args:
        None
    Inputs:
        N (int): 正数
        K (int): 桁和
    Prints:
        str: 
    Returns:
        None
    """
    # 正数 N と桁和 K をインプットする
    N, K = map(int, input().split())
    # N 以下の正整数のうち、各桁の値の和が K である正整数の個数をカウントし出力する
    count = 0
    for i in range(1, N + 1):
        # N を桁ごとのリストに変換
        print(i)
        digits = [int(d) for d in str(i)]
        # 桁ごとのリストから各桁の値の和を計算する
        digit_sum = sum(digits)
        if digit_sum == K:
            count += 1
    # 結果を出力する
    print(count)
    


# ローカル実行
if __name__ == "__main__":
    main()