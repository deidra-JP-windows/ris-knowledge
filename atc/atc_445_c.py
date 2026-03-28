# TODO: サイクルについて理解する為、グラフ理論を勉強する
## 辺がどうのってやつと、このケースでサイクルが存在しないケースがない点について理解する必要あり
def main():
    """マス s に駒を置き「駒が置かれているマスに書かれている整数を x として、駒をマス x に移動させる」という操作を 10^100回行った後、駒が置かれているマスの番号を出力する
    処理概要:
        1. マスの数 N を入力する
        2. マス i に書かれている整数 Ai (1≤i≤N) を空白区切りで入力する
        3. 各マスについて最終到達位置を格納する配列 final_pos を初期化（None）
        4. 各マス start (未計算のもの) に対して以下を実行:
            4.1. start から経路を辿り、サイクルまたは計算済みマスに到達するまで path に記録
            4.2. 計算済みマスに到達した場合、path 上の全マスの最終位置を設定
            4.3. サイクルを検出した場合:
                - サイクル内の各マスについて、10^100 % cycle_length 後の位置を計算
                - サイクルより前の各マスについて、サイクルまでの距離を考慮して最終位置を計算
        5. s=1,2,…,N に対する final_pos を、この順に空白を区切りとして一行に出力する
    補足：
        1. 全体のグラフを一度だけ解析することでO(N)の計算量を実現
        2. 既に計算済みのマスの情報を再利用することで重複計算を回避
    前提:
        1. マス 1, マス 2,…, マス N の N 個のマスが 1 列に並んでいる
        2. マス i には整数 Ai が書かれている (1≤i≤N)
        3. s は 1 以上 N 以下の整数である
        3. 最初、駒はマス s に置かれている
    条件:
        1. 駒が置かれているマスには整数が書かれている
    制約:
        1. 1≤N≤5×10^5
        2. 入力はすべて整数
        3. N回の操作ではタイムアウトする
        4. 以下の制約は排除
          - i≤Ai≤N (1≤i≤N) 
          - 当制約がないため、サイクルの検出と処理が必要
          - 当制約がある場合、サイクルは存在しないため、単純に10^100回の移動をシミュレートすればよい
    Args:
        None
    Inputs:
        N (int): マスの数
        A (int): マス i に書かれている整数 Ai (1≤i≤N) を空白区切りで入力
    Prints:
        str: s=1,2,…,N に対する答えを、この順に空白を区切りとして一行に出力
    Returns:
        None
    """
    # マスの数 N を入力する
    N = int(input())
    # マス i に書かれている整数 Ai (1≤i≤N) を空白区切りで入力する
    A = list(map(int, input().split()))
    
    # 各マスの最終到達位置を格納（未計算は None）
    final_pos = [None] * N
    
    # 各マスについて最終位置を計算
    for start in range(N):
        # 既に計算済みならスキップ
        if final_pos[start] is not None:
            continue
        
        # 経路を記録
        path = []
        visited = {}
        current = start
        
        # サイクルまたは計算済みマスに到達するまで進む
        while current not in visited and final_pos[current] is None:
            visited[current] = len(path)
            path.append(current)
            current = A[current] - 1
        
        if final_pos[current] is not None:
            # 既に計算済みのマスに到達
            # path上の全マスの最終位置は final_pos[current] と同じ
            for node in path:
                final_pos[node] = final_pos[current]
        else:
            # サイクルを検出
            cycle_start = visited[current]
            cycle = path[cycle_start:]
            cycle_length = len(cycle)
            
            # サイクル内の各マスの最終位置を計算
            for i, node in enumerate(cycle):
                final_idx = (i + 10**100) % cycle_length
                final_pos[node] = cycle[final_idx]
            
            # サイクルより前の各マスの最終位置を計算
            for i in range(cycle_start):
                steps_to_cycle = cycle_start - i
                remaining = (10**100 - steps_to_cycle) % cycle_length
                final_pos[path[i]] = cycle[remaining]
    
    # 結果を1-indexed で出力
    result = [final_pos[i] + 1 for i in range(N)]
    print(" ".join(map(str, result)))


# ローカル実行
if __name__ == "__main__":
    main()
