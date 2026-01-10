def main():
    """競争の順位を決定するプログラム
        処理概要:
            1. ユーザーから馬の頭数 N と各馬のタイム T を入力として受け取る
            2. T を馬の番号の key を持つdictに変換する
            3. タイムをもとに順位を決定する
            4. 1,2,3 着の馬の番号を出力する
        例;
            入力:
                4
                100 110 105 95
            出力:
                4 1 3
        Arguments:
            None
        Returns:
            None
    """

    # ユーザーから馬の頭数 N を入力として受け取る
    n = int(input())

    # 各馬のタイム T を入力として受け取る
    t = list(map(int, input().split()))
    
    # T を馬の番号の key を持つdictに変換する
    time_dict = {i+1: t[i] for i in range(n)}
    
    # タイムをもとに順位を決定する
    sorted_horses = sorted(time_dict.items(), key=lambda x: x[1])

    # 1,2,3 着の馬の番号を出力する
    print(sorted_horses[0][0], sorted_horses[1][0], sorted_horses[2][0])

if __name__ == '__main__':
    main()
