# python2


from collections import defaultdict


class PriorityQueue:
    def __init__(self, n):
        self.nodes = [PriorityQueue.Node(i, float('inf')) for i in xrange(1, n+1)]
        self.positions = [None] + range(n)

    def get_node(self, v):
        return self.nodes[self.positions[v]]

    def set_priority(self, v, priority):
        node = self.get_node(v)
        assert priority <= node.priority
        node.priority = priority
        self.sift_up(node.v)

    def get_priority(self, v):
        return self.get_node(v).priority

    def size(self):
        return len(self.nodes)

    def empty(self):
        return self.size() == 0

    def get(self):
        self.swap(0, self.size()-1)
        node = self.nodes.pop()
        if not self.empty():
            self.sift_down(self.nodes[0].v)
        return node

    def sift_down(self, v):
        i = self.positions[v]
        while True:
            min_i = i
            left, right = (i << 1)+1, (i << 1)+2
            if left < self.size() and self.nodes[left].priority < self.nodes[min_i].priority:
                min_i = left
            if right < self.size() and self.nodes[right].priority < self.nodes[min_i].priority:
                min_i = right
            if i != min_i:
                self.swap(i, min_i)
                i = min_i
            else:
                break

    def sift_up(self, v):
        i = self.positions[v]
        p = (i-1) >> 1
        while p >= 0 and self.nodes[i].priority < self.nodes[p].priority:
            self.swap(i, p)
            i = p
            p = (i-1) >> 1

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]
        self.positions[self.nodes[i].v] = i
        self.positions[self.nodes[j].v] = j

    class Node:
        def __init__(self, v, priority):
            self.v = v
            self.priority = priority


def dijkstra(graph, n, u, v):
    visited = [False] * (n+1)
    queue = PriorityQueue(n)
    queue.set_priority(u, 0)
    while not queue.empty():
        node = queue.get()
        if node.v == v:
            return node.priority if node.priority < float('inf') else -1
        visited[node.v] = True
        for child, w in graph[node.v]:
            if not visited[child]:
                prev = queue.get_priority(child)
                if node.priority + w < prev:
                    queue.set_priority(child, node.priority + w)
    return -1


def read_graph():
    n, m = map(int, raw_input().split())
    graph = defaultdict(list)
    for _ in xrange(m):
        u, v, w = map(int, raw_input().split())
        graph[u].append((v, w))
    u, v = map(int, raw_input().split())
    return graph, n, u, v


def main():
    graph, n, u, v = read_graph()
    print(dijkstra(graph, n, u, v))


if __name__ == '__main__':
    main()
