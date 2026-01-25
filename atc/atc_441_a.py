def main():
    """ マス (X,Y) が黒く塗られているか判定する。
        処理概要：
            1. 入力値を取得する。
            2. マス (P,Q) から右に100、下に100の範囲が黒く塗られている範囲の中にいる
              - この範囲に含まれているかで、マス (X,Y) が黒く塗られているか判定する。
            3. 判定結果を出力する。
        Args: None
        Returns: None
        入力例:
            None
        インプット例: 
            150 200
            160 250
        print例: 
            Yes
        出力例
            None
    """
    # 1. 入力値を取得する。input は2行に分ける
    P, Q = map(int, input().split())
    X, Y = map(int, input().split())
    # 2. マス (P,Q) から右に100、下に100の範囲が黒く塗られている範囲の中にいる
    #  - この範囲に含まれているかで、マス (X,Y) が黒く塗られているか判定する。
    if P <= X < P + 100 and Q <= Y < Q + 100:
        result = "Yes"
    else:
        result = "No"

    # 3. 判定結果を出力する。
    print(result)


if __name__ == '__main__':
    main()
