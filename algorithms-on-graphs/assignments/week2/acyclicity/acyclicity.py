# python2


from collections import defaultdict


class Color:
    WHITE = 'white'
    GREY = 'grey'
    BLACK = 'black'


class Node:
    def __init__(self, v):
        self.v = v
        self.color = Color.WHITE

    def set_color(self, color):
        self.color = color


def contains_cycle(graph, n):
    visited = [Node(v) for v in xrange(n+1)]
    for v in graph.keys():
        if visited[v].color == Color.WHITE:
            if dfs_contains_cycle(graph, v, visited):
                return True
    return False


def dfs_contains_cycle(graph, v, visited):
    if visited[v].color == Color.GREY:
        return True
    visited[v].color = Color.GREY
    for child in graph[v]:
        t = dfs_contains_cycle(graph, child, visited)
        if t:
            return True
    visited[v].color = Color.BLACK
    return False


def read_graph():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
    return graph, n


def main():
    graph, n = read_graph()
    print(int(contains_cycle(graph, n)))


if __name__ == '__main__':
    main()
