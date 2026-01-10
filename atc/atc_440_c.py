from concurrent.futures import ThreadPoolExecutor

# TODO: 現時点で非機能要件を満たす実行速度を出せて言いない為、最適化が必要
def _calculate_min_cost(N, W, C):
    """黒く塗るマスのコストの合計の最小値を計算する
    Args:
        N (int): マスの数
        W (int): 閾値
        C (list): 各マスのコストのリスト
    Returns:
        int: コストの合計の最小値
    """
    min_cost = float('inf')
    for x in range(2 * W):
        total_cost = 0
        for i in range(1, N + 1):
            if (i + x) % (2 * W) < W:
                total_cost += C[i - 1]
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost


def main():
    """マスを黒く塗るためのコストの合計の最小値を求めるプログラム
        処理概要:
            1. ユーザーからテストケースの数 T を入力として受け取る
            2. 各テストケースについて、N (マスの数) と W (閾値) を入力として受け取る
            3. 各テストケースについて、C (コスト) のリストを入力として受け取る
            4. 受け取ったデータをタプル形式でリストに格納
            5. 並列化で各テストケースについて、x を 0 から 2W-1 まで変化させながら、黒く塗るマスのコストの合計を計算する
            6. コストの合計の最小値をリストに格納
            7. 各テストケースについて、コストの合計の最小値を格納したリストを最後に要素ごとに別々で出力する
        マスを黒く塗る条件:
            前提: 正整数 x を自由に選ぶ。 
                  1≤i≤N を満たす整数 i 
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
    # 並列化で各テストケースについて、x を 0 から 2W-1 まで変化させながら、黒く塗るマスのコストの合計を計算する
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda args: _calculate_min_cost(*args), test_cases))
        # コストの合計の最小値をリストに格納
        results_list.extend(results)
    # 各テストケースについて、コストの合計の最小値を格納したリストを最後に要素ごとに別々で出力する
    for result in results_list:
        print(result)

if __name__ == '__main__':
    main()