# python2


from collections import defaultdict


def connected_components(graph, n):
    visited = [False] * (n+1)
    cnt = n-len(graph)
    for v in graph:
        if not visited[v]:
            dfs(graph, v, visited)
            cnt += 1
    return cnt


def dfs(graph, v, visited):
    stack = [v]
    while len(stack) > 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for child in graph[v]:
                stack.append(child)


def read_graph():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph, n


def main():
    graph, n = read_graph()
    print(connected_components(graph, n))


if __name__ == '__main__':
    main()
