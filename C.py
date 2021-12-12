# bisectについて : https://docs.python.org/ja/3/library/bisect.html
import bisect

# 標準入力を受け付ける。
N, Q = map(int, input().split())

A = list(map(int, input().split()))

# A1〜ANを昇順ソートする。
A.sort()

for i in range(Q):
    X = int(input())
    # 二分探索を用いて、x1の身長がA1〜ANの身長の、何番目に位置するのか確かめる。x1の身長より大きいAx〜ANの数を出力する。x2, x3, ...に関しても同様の処理を繰り返す。
    idx = bisect.bisect_left(A, X)
    print(len(A) - idx)
