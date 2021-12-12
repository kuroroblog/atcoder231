import sys

# 参考 : https://note.nkmk.me/python-sys-recursionlimit/
sys.setrecursionlimit(10 ** 6)

# 標準入力を受け付ける。
N, M = map(int, input().split())

# edges[0]は利用しない。
edges = []
for _ in range(N + 1):
    edges.append([])

for _ in range(M):
    A, B = map(int, input().split())

    edges[A].append(B)
    edges[B].append(A)

    # 同じ番号のついた人が3回以上登場してはならない。
    if 3 <= max(len(edges[A]), len(edges[B])):
        print('No')
        exit()

def dfs(now, pre=-1):
    # 一度訪れたところに再度訪れようとしている場合は、`No`とする。
    if visited[now] == True:
        print('No')
        exit()

    visited[now] = True
    for to in edges[now]:
        if pre == to:
            continue
        dfs(to, now)

# visited[0]は利用しない。
visited = [False] * (N + 1)
for i in range(1, N + 1):
    # visited[i]がTrueの場合、探索を行わない。iから始まる探索を既に終えているため。
    if not visited[i]:
        dfs(i)

print('Yes')
