# 線形探索
def linear_search(arr, target):
    """
    線形探索アルゴリズム
    特徴: リストの各要素を順番にチェックしていく単純な探索方法
    時間計算量: O(n)
    :param arr: 探索対象のリスト
    :param target: 探索する値
    :return: 見つかった場合はインデックス、見つからなかった場合は-1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 二分探索
# 探索する範囲がおおよそ半分になる概念
def binary_search(arr, target):
    """
    二分探索アルゴリズム
    特徴: ソートされたリストに対して効率的に探索を行う方法
    時間計算量: O(log n) 何回2で割れるか
    :param arr: ソートされた探索対象のリスト
    :param target: 探索する値
    :return: 見つかった場合はインデックス、見つからなかった場合は-1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 木構造
## グラフ理論の一種
## グラフの一種
### サイクル（閉路）を持たない連結無向グラフ
### ノード（頂点）とエッジ（辺）で構成されるデータ構造
### n-1本のエッジでn個のノードが接続される

# 二分探索木
## 木構造を使った二分探索
### 親ノードが左子ノードより大きく、右子ノードより小さい特性を持つデータ構造
### 先端ノード == 葉ノード, 根ノード == 最上位ノード, 内部ノード == 根ノードと葉ノード以外のノード
### ノードは接点、エッジはノード同士をつなぐ線
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

# 深さ優先探索（DFS）
## 再帰的に関数を呼び出す
def depth_first_search(root, target):
    """
    深さ優先探索アルゴリズム
    特徴: 木構造やグラフ構造において、可能な限り深く探索していく方法
    時間計算量: O(V + E) Vは頂点数、Eは辺の数
    :param root: 探索対象の木の根ノード
    :param target: 探索する値
    :return: 見つかった場合はTrue、見つからなかった場合はFalse
    """
    if root is None:
        return False
    if root.val == target:
        return True
    return depth_first_search(root.left, target) or depth_first_search(root.right, target)


# バブルソート
def bubble_sort(arr):
    """
    バブルソートアルゴリズム
    特徴: 隣接する要素を比較し、順序が逆であれば交換することでリストをソートする単純な方法
    時間計算量: O(n^2)
    :param arr: ソート対象のリスト
    :return: ソートされたリスト
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 逆ポーランド記法
def reverse_polish_notation(expression):
    """
    逆ポーランド記法（RPN: Reverse Polish Notation）の解説と実装例。
    特徴: 演算子をオペランドの後に記述する記法で、括弧を使わずに計算の優先順位を明確にできる。
    利点: スタックを用いることで、計算を効率的に行える。

    :param expression: 逆ポーランド記法で記述された数式（リスト形式）
    :return: 計算結果

    例：
    中置記法: (2 + 3) * 4 == 逆ポーランド記法: 2 3 + 4 *
    逆ポーランド記法の計算手順:
    1. 2 と 3 をスタックにプッシュ
    2. '+' 演算子が来たら、スタックから 2 と 3 をポップし、加算して結果 5 をスタックにプッシュ
    3. 4 をスタックにプッシュ
    4. '*' 演算子が来たら、スタックから 5 と 4 をポップし、乗算して結果 20 をスタックにプッシュ
    """
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

# モンテカルロ法
# ランダムサンプリングを用いて数値計算やシミュレーションを行い近似を得る手法の総称
## 近似 == ある数量に非常に近いこと
def monte_carlo_simulation(num_samples):
    """
    モンテカルロ法のシンプルな実装例。
    特徴: ランダムサンプリングを用いて数値計算やシミュレーションを行う手法。
    用途: 数学的問題の近似解、統計的推定、物理シミュレーションなど。

    :param num_samples: サンプリング数
    :return: 単位円内に入った点の割合を用いた円周率の近似値
    """
    import random

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4  # 円周率の近似値

# 確率過程
# 時間とともに確率的に変化する現象をモデル化する数学的手法
# 例: マルコフ過程、ポアソン過程、ウィーナー過程など
# 時刻ごとに確率変数があり、その列全体をまとめて扱う枠組み。離散時間・連続時間、離散状態・連続状態などいろいろなタイプがある。
# 時系列変化する何かしらの要素がプロットされる。　→ 何かしらの要素通しがそれぞれ何パーの確立で遷移するかのイメージがわかりやすいかも

# マルコフ連鎖
# 現在の状態が次の状態にのみ依存する確率過程
# マルコフ性（記憶なし性）を持ち、状態は有限や可算個の離散的な集合で表すことが多い。
# 状態の系列(X0,X1,X2,…)(X0,X1,X2,…)
# 状態は「晴れ・雨」「ページA・ページB・ページC」「機械の稼働・故障」などのような離散的な集合で表され、それぞれの状態間に「どの状態からどの状態へ何％で移るか」という遷移確率が定義される

# 推移行列
# マルコフ連鎖における状態間の遷移確率を表す行列
# python のデータ型で表すと、辞書や2次元リストなどが使われる
# states = ['A', 'B', 'C']
# transitions = {('A', 'A'): 0.1, ('A', 'B'): 0.6, ('A', 'C'): 0.3,
#                ('B', 'A'): 0.4, ('B', 'B'): 0.5, ('B', 'C'): 0.1,
#                ('C', 'A'): 0.2, ('C', 'B'): 0.3, ('C', 'C'): 0.5}
def transition_matrix(states, transitions):
    """
    推移行列の作成
    特徴: マルコフ過程における状態間の遷移確率を表す行列
    :param states: 状態のリスト
    :param transitions: 遷移確率の辞書 {(from_state, to_state): probability}
    :return: 推移行列
    """
    import numpy as np

    n = len(states)
    matrix = np.zeros((n, n))

    state_index = {state: i for i, state in enumerate(states)}

    for (from_state, to_state), prob in transitions.items():
        i = state_index[from_state]
        j = state_index[to_state]
        matrix[i][j] = prob

    return matrix

# ベルヌーイ分布
# 1回の試行で成功か失敗かを表す分布
# 2項分布の特殊ケースで1回の試行で1以外なら2項分布
def bernoulli_distribution(p):
    """
    ベルヌーイ分布の確率質量関数
    特徴: 成功確率pの試行が1回行われる場合の分布
    :param p: 成功確率 (0 <= p <= 1)
    :return: 確率質量関数を表す関数
    """
    def pmf(k):
        if k == 1:
            return p
        elif k == 0:
            return 1 - p
        else:
            return 0
    return pmf


