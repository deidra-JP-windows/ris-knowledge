# 英小文字からなる長さ 3 以上の文字列 S が与えられます。
# S はちょうど 2 種類の文字を含み、 1 文字だけ他の文字と異なります。その 1 文字を答えてください。
# 例えば、 S が odd なら o と答えてください。
def main():
    string = input().strip()
    # 文字列の中から文字別の数が一番少ない文字を取得
    print(min(string, key=string.count))
main()
