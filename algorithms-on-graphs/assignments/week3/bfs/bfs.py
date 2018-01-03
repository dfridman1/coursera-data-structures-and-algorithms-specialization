# python2

from collections import defaultdict
from Queue import Queue


class Node:
    def __init__(self, v, dist=0):
        self.v = v
        self.dist = dist


def find_distance(graph, n, u, v):
    visited = [False] * (n+1)
    visited[u] = True
    q = Queue()
    q.put(Node(u))
    while not q.empty():
        u = q.get()
        if u.v == v:
            return u.dist
        for child in graph[u.v]:
            if not visited[child]:
                q.put(Node(child, u.dist+1))
                visited[child] = True
    return -1


def read_graph():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
        graph[v].append(u)
    u, v = map(int, raw_input().split())
    return graph, n, u, v


def main():
    graph, n, u, v = read_graph()
    print(find_distance(graph, n, u, v))


if __name__ == '__main__':
    main()
