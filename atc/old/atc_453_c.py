def main():
    """座標 0 を最大で何回通り過ぎるか出力
    処理概要:
        1. プレイヤの移動回数 N を入力する
        2. プレイヤの移動距離を表す長さ N の整数列 L を半角スペース区切りで入力する
        3. 深さ優先探索（DFS）を用いて、プレイヤの移動の全パターンを探索する
          - プレイヤの移動回数が N に達したとき、座標 0 を通り過ぎた回数を更新する
          - プレイヤは i 回目の移動では、「正の方向」「負の方向」のいずれかを選ぶ
          - その方向に L_i だけ移動する
        4. 座標 0 を通り過ぎた回数の最大値を出力する
    補足：
        1.
    前提:
        1. 数直線上の座標 0.5 にプレイヤがいる
        2. プレイヤはこれから N 回の移動を行う
        3. プレイヤは i 回目の移動では、「正の方向」「負の方向」のいずれかを選ぶ
          - その方向に L_i だけ移動する
    条件:
        1. 座標 0 で完了する移動が生じることはない
    制約:
        1. 1 ≤ L_i ≤ 10^9
        2. 1 ≤ N ≤ 20
        3. 入力はすべて整数
    Args:
        None
    Inputs:
        N (int): プレイヤの移動回数
        L (list of int): プレイヤの移動距離を表す長さ N の整数列
    Prints:
        str: 座標 0 を最大で何回通り過ぎるか
    Returns:
        None
    """
    # プレイヤの移動回数 N を入力する
    N = int(input())
    # プレイヤの移動距離を表す長さ N の整数列 L を半角スペース区切りで入力する
    L = list(map(int, input().split()))
    # 座標を2倍して整数で扱う（開始位置 0.5 -> 1）
    L2 = [x * 2 for x in L]
    # 深さ優先探索（DFS）を用いて、プレイヤの移動の全パターンを探索する
    max_count = dfs(0, 1, 0, N, L2)
    # 座標 0 を通り過ぎた回数の最大値を出力する
    print(max_count)


def dfs(i, pos, count, N, L):
    """プレイヤの移動の全パターンを探索するための深さ優先探索（DFS）
    Args:
        i (int): プレイヤの移動回数
        pos (int): プレイヤの現在地
        count (int): プレイヤが座標 0 を通り過ぎた回数
        N (int): プレイヤの移動回数の総数
        L (list of int): プレイヤの移動距離を表す長さ N の整数列
    Returns:
        max_count (int): プレイヤの移動の全パターンを探索したときの、座標 0 を通り過ぎた回数の最大値
    """
    # プレイヤの移動回数が N に達したとき、座標 0 を通り過ぎた回数を更新する
    if i == N:
        return count
    # プレイヤは i 回目の移動では、「正の方向」「負の方向」のいずれかを選ぶ
    # その方向に L_i だけ移動する
    next_pos_plus = pos + L[i]
    crossed_plus = pos * next_pos_plus < 0
    plus_result = dfs(i + 1, next_pos_plus, count + crossed_plus, N, L)

    next_pos_minus = pos - L[i]
    crossed_minus = pos * next_pos_minus < 0
    minus_result = dfs(i + 1, next_pos_minus, count + crossed_minus, N, L)

    return max(plus_result, minus_result)


# ローカル実行
if __name__ == "__main__":
    main()
