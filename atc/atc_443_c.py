def main():
    """始業から終業までに、高橋君が合計で何秒 chokutter を見ていたかを出力
    処理概要:
        1. 青木君が高橋君のデスクの後ろを通りかかった回数と AtCoder 社の終業時刻をインプット
        2. 青木君が通りかかる時刻のリストをインプット
        3. 青木君が通りかかる時刻のリストの要素を順に処理
          1. 開いている現時刻が通りかかる時刻移行の場合以下の処理を実行
            - その時刻までの閲覧時間を加算
            - 100 秒を足して chokutter を再度開く現時刻を設定
        4. 終業時刻までに開いている場合、その分の閲覧時間を加算
        5. 合計閲覧時間を出力
    前提:
        1. AtCoder 社は時刻 0 に始業し時刻 T に終業する
          - 例：0 に始業し 1000 に終業する
        2. 高橋君は AtCoder 社の業務時間中に SNS の chokutter を以下の規則で見る
          - 始業と同時に chokutter を開く
          - 青木君が高橋君のデスクの後ろを通りかかった瞬間に chokutter を開いていた場合、直ちに chokutter を閉じる
          - 高橋君は chokutter を時刻 t に閉じると、時刻 t+100 に必ず chokutter を開く
        3. 時刻 t と時刻 t+1 との間隔は 1 秒
        4. 始業から終業までに N 回青木君が高橋君のデスクの後ろを通りかかっている
          - そのうち i 回目は時刻 A i だった
    制約:
        1. 入力は全て整数
        2. 0 ≤ N ≤ 3 * 10 ^ 5
        3. 1 ≤ A1 < A2 < ⋯ < AN ≤ T ≤ 10 ^9
        4. 高橋君が chokutter を開いた瞬間に青木君がデスクの後ろを通りかかることはない
    Args:
        None
    Inputs:
        N (int): 青木君が高橋君のデスクの後ろを通りかかった回数
        T (int): AtCoder 社の終業時刻
        A (int): 青木君が高橋君のデスクの後ろを通りかかった時刻
    Prints:
        Int: 
    Returns:
        None
    """
    # 青木君が高橋君のデスクの後ろを通りかかった回数と AtCoder 社の終業時刻をインプット
    N, T = map(int, input().split())
    # 青木君が通りかかる時刻のリストをインプット
    A = list(map(int, input().split())) if N > 0 else []
    # 青木君が通りかかる時刻のリストの要素を順に処理
    total_time = 0
    # 開き始めた時間を更新していくための変数
    current_start = 0
    for i in range(N):
        # 開き始めた時間が通りかかる時刻移行の場合以下の処理を実行
        if A[i] >= current_start:
            # 通りかかる時刻からまで開き始めた時間を引いた値を加算
            total_time += A[i] - current_start
            # 開き始めた時間に通りかかる時刻と 100 秒を追加
            current_start = A[i] + 100
    # 終業時刻までに開いている場合、その分の閲覧時間を加算
    if current_start < T:
        total_time += T - current_start
    # 合計閲覧時間を出力
    print(total_time)


# ローカル実行
if __name__ == "__main__":
    main()