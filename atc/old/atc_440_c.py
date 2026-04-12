from concurrent.futures import ProcessPoolExecutor


def _wrapper_calculate_min_cost(args):
    """ProcessPoolExecutor用のラッパー関数"""
    return _calculate_min_cost(*args)

def _calculate_min_cost(N, W, C):
    """黒く塗るマスのコストの合計の最小値を計算する
    処理概要:
        1. マス i を2Wで割った余りがWより小さくなる場合黒く塗る為、位置mod(2W)ごとのコスト集計
        2. 累積和を構築（円環対応）しx=0の場合のコストを計算
          - x=0のとき、位置0~W-1が黒く塗られる
        3. xをずらしながらスライディングウィンドウ
        4. 最小値を返す
    Args:
        N (int): マスの数
        W (int): 閾値
        C (list): 各マスのコストのリスト
    Returns:
        int: コストの合計の最小値
    """
    # マス i を2Wで割った余りがWより小さくなる場合黒く塗る為、位置mod(2W)ごとのコスト集計
    position_costs = [0] * (2 * W)
    for i in range(1, N + 1):
        pos = i % (2 * W)
        position_costs[pos] += C[i - 1]

    # 累積和を構築（円環対応）しx=0の場合のコストを計算
    # x=0のとき、位置0~W-1が黒く塗られる
    current_cost = sum(position_costs[0:W])
    min_cost = current_cost
    
    # xをずらしながらスライディングウィンドウ
    # マスが2W個分あるので、xを1から2W-1までずらす
    # マスを1つ左にずらす = 削除する位置と追加する位置
    for x in range(1, 2 * W):
        # 窓を1つ左にずらす = 削除する位置と追加する位置
        remove_pos = (W - x + 2 * W) % (2 * W)
        add_pos = (2 * W - x + 2 * W) % (2 * W)
        current_cost = current_cost - position_costs[remove_pos] + position_costs[add_pos]
        min_cost = min(min_cost, current_cost)
    # 最小値を返す
    return min_cost


def main():
    """マスを黒く塗るためのコストの合計の最小値を求めるプログラム

        処理概要:
            1. ユーザーからテストケースの数 T を入力として受け取る
            2. 各テストケースについて、N (マスの数) と W (閾値) を入力として受け取る
            3. 各テストケースについて、C (コスト) のリストを入力として受け取る
            4. 受け取ったデータをタプル形式でリストに格納
            5. 並列処理で各テストケースについて、x を 0 から 2W-1 まで変化させながら、黒く塗るマスのコストの合計を計算する
            6. コストの合計の最小値をリストに格納
            7. 各テストケースについて、コストの合計の最小値を格納したリストを最後に要素ごとに別々で出力する
        マスを黒く塗る条件:
            前提: - 正整数 x を自由に選ぶ。 
                  - 1≤i≤N を満たす整数 i 
                  - T,N,Wは整数で偶数
            条件: (i + x) を 2W で割った余りが W より小さくなるもの全てに対し、マス i を黒く塗る。
            → (i + x) % (2W) < W
        例;
            入力:
                4  # テストケースの数 T
                8 2 # 各テストケースの N (マスの数) と W (閾値)
                1 10 10 1 1 10 10 1 # C (コスト) のリスト
                8 3
                1 10 10 1 1 10 10 1
                8 4
                1 10 10 1 1 10 10 1
                4 100
                100000 100000 100000 100000
            出力:
                4
                12
                22
                0
        Arguments:
            None
        Returns:
            None
    """
    # 受け取ったデータをタプル形式でリストに格納
    test_cases = []
    # ユーザーからテストケースの数 T を入力として受け取る
    T = int(input())
    # 各テストケースについて、N (マスの数) と W (閾値) を入力として受け取る
    results_list = []
    for _ in range(T):
        N, W = map(int, input().split())
        # 各テストケースについて、C (コスト) のリストを入力として受け取る
        C = list(map(int, input().split()))
        if len(C) != N:
            raise ValueError("コストの数がマスの数と一致しません。")
        test_cases.append((N, W, C))

    # 各テストケースについて、x を 0 から 2W-1 まで変化させながら、黒く塗るマスのコストの合計を計算する
    for args in test_cases:
        result = _calculate_min_cost(*args)
        results_list.append(result)

    # 並列処理で各テストケースについて、x を 0 から 2W-1 まで変化させながら、黒く塗るマスのコストの合計を計算する
    #with ProcessPoolExecutor() as executor:
    #    results = list(executor.map(_wrapper_calculate_min_cost, test_cases))
    #    # コストの合計の最小値をリストに格納
    #    results_list.extend(results)

    # 各テストケースについて、コストの合計の最小値を格納したリストを最後に要素ごとに別々で出力する
    for result in results_list:
        print(result)

if __name__ == '__main__':
    main()