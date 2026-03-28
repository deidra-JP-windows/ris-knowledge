def main():
    """整数列 A の各要素をルールに元に X と比較して更新し、更新の有無を出力する
    処理概要:
        1. 整数 N と X を半角スペース区切りで入力する
        2. 整数列 A を入力する
        3. i=1,2,…,N の順に以下を実行する
            1. もし Ai < X なら、 X=Ai に更新した上で 1 を出力
            2. そうでないなら 0 を出力
    補足：
        1. None
    前提:
        1. None
    条件:
        1. i=1,2,…,N
    制約:
        1. 入力は全て整数
        2. 1 ≤ N,X,Ai ≤ 100
    Args:
        None
    Inputs:
        N (int): 整数列 A の長さ
        A (list of int): 整数列 A
        X (int): 整数 X
    Prints:
        str: 
    Returns:
        None
    """
    # 整数 N と X を半角スペース区切りで入力する
    N, X = map(int, input().split())
    # 整数列 A を入力する
    A = list(map(int, input().split()))
    # i=1,2,…,N の順に以下を実行する
    for i in range(N):
        # もし Ai < X なら、 X=Ai に更新した上で 1 を出力
        if A[i] < X:
            X = A[i]
            print(1)
        # そうでないなら 0 を出力
        else:
            print(0)



# ローカル実行
if __name__ == "__main__":
    main()
