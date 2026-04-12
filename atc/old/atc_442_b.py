def main():
    """ i 回目の操作を終えた直後に音量 3 以上で音楽が再生されているか判定する
    処理概要:
        1. Q （操作回数）をインプット
        2. Q 回の各操作について以下を実行
          - A i をインプット
            - A i の値に応じて音量と再生状態を更新
            - 音量と再生状態に基づき "Yes" もしくは "No" を結果リストに追加
        3. 結果リストを出力
    制約:
        1. 1≤Q≤2*10 5
        2. A i∈{1,2,3}
        3. 入力される値はすべて整数
    Args:
        None
    Inputs:
        Q (int): 操作回数
            : i = 1 から Q までの各操作についての情報が続く
        A (int): 操作の種類を表す整数 (1 or 2 or 3)
            : A i=1 のとき、音量を 1 上げる
            : A i=2 のとき、現在の音量が 1 以上であれば音量を 1 下げ、0 であれば何もしない
            : A i=3 のとき、曲が停止中であれば曲を再生し、曲が再生中であれば曲を停止する。
    Prints:
        int: Q 行出力
          : i 行目には、i 回目の操作を終えた直後に音量 3 以上で音楽が再生されているならば Yes を、そうでないならば No を出力
    Returns:
        None
    """
    # Q （操作回数）をインプット
    Q = int(input())
    volume = 0
    is_playing = False
    results = []

    # Q 回の各操作について以下を実行
    for _ in range(Q):
        # A i をインプット
        A = int(input())
        # A i の値に応じて音量と再生状態を更新
        if A == 1:
            volume += 1
        elif A == 2:
            if volume > 0:
                volume -= 1
        elif A == 3:
            is_playing = not is_playing

        # 音量と再生状態に基づき "Yes" もしくは "No" を結果リストに追加
        if is_playing and volume >= 3:
            results.append("Yes")
        else:
            results.append("No")
    
    # 結果リストを出力
    for result in results:
        print(result)


# ローカル実行
if __name__ == "__main__":
    main()