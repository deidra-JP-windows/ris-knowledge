def main():
    """音の周波数をオクターヴ上げるプログラム
        処理概要:
            1. ユーザーから周波数 X とオクターヴ数 Y を入力として受け取る
            2. 周波数 * 2 の Y 乗で計算する
            3. 結果を出力する 
        例;
            入力:
                440 1
            出力:
                880
        Arguments:
            None
        Returns:
            None
    """
    x, y = map(int, input().split())
    result = x * (2 ** y)
    print(result)

if __name__ == '__main__':
    main()
