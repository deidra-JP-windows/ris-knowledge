def main():
    """ AtCoder 国の公用語の単語の種類を判定する。
        処理概要：
            1. 入力値を取得する。
            2. 各単語について、その単語に含まれる文字からその単語が次のうちどれに該当するか判定する。
                - 高橋語の単語であることが確定する
                - 青木語の単語であることが確定する
                - どちらともいえない
            3. 判定結果を出力する。
        Args: None
        Returns: None
        入力例:
            None
        インプット例: 
            6 5
            ahikst
            aikot
            5
            asahi
            okita
            kiai
            hash
            it
        print例: 
            Takahashi
            Aoki
            Unknown
            Takahashi
            Unknown
            Aoki
            Unknown
        出力例
            None
    """
    # 1. 入力値を取得する。
    N, M = map(int, input().split())
    S = set(input().strip())
    T = set(input().strip())
    Q = int(input().strip())
    results = []
    for _ in range(Q):
        w = input().strip()
        # 2. 各単語について、その単語に含まれる文字からその単語が次のうちどれに該当するか判定する。
        is_takahashi = all(c in S for c in w)
        is_aoki = all(c in T for c in w)
        if is_takahashi and not is_aoki:
            results.append("Takahashi")
        elif is_aoki and not is_takahashi:
            results.append("Aoki")
        else:
            results.append("Unknown")
    # 3. 判定結果を出力する。
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
