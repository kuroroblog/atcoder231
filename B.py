import collections

# 標準入力を受けつける。
N = int(input())

data = []
for i in range(N):
    S = input()
    data.append(S)

# 候補者ごとに、得票数をまとめる。
# collections参考 : https://note.nkmk.me/python-collections-counter/
c = collections.Counter(data)

# 得票数の多い順に候補者を並べる。
# 得票数の一番多い候補者を出力する。
print(c.most_common()[0][0])
