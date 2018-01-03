# python2


from collections import defaultdict


def path_exists(graph, n, u, v):
    visited = [False] * (n+1)
    stack = [u]
    while len(stack) > 0:
        u = stack.pop()
        if u == v:
            return True
        visited[u] = True
        for child in graph[u]:
            if not visited[child]:
                stack.append(child)
    return False


def read_data():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
        graph[v].append(u)
    u, v = map(int, raw_input().split())
    return graph, n, u, v


def main():
    graph, n, u, v = read_data()
    print(int(path_exists(graph, n, u, v)))


if __name__ == '__main__':
    main()
