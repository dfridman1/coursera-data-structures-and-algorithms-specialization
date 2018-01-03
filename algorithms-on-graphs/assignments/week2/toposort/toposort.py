# python2

import sys

sys.setrecursionlimit(10**7)

from collections import defaultdict


def topological_sort(graph, n):
    visited = [False] * (n+1)
    ordering = [None] * n
    pos = n-1
    for v in xrange(1, n+1):
        if not visited[v]:
            pos = dfs(graph, v, ordering, pos, visited)
    return ordering


def dfs(graph, v, ordering, pos, visited):
    visited[v] = True
    for child in graph[v]:
        if not visited[child]:
            pos = dfs(graph, child, ordering, pos, visited)
    ordering[pos] = v
    return pos-1


def read_graph():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
    return graph, n


def main():
    graph, n = read_graph()
    ordering = topological_sort(graph, n)
    print(' '.join(map(str, ordering)))


if __name__ == '__main__':
    main()
