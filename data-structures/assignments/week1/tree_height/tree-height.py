# python2


from collections import defaultdict


def get_graph():
    graph = defaultdict(list)
    root = None
    raw_input()
    parents = map(int, raw_input().split())
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            graph[p].append(i)
    return root, graph


def get_height(root, graph):
    stack = [(root, 0)]
    curr = height = 1
    while len(stack) > 0:
        v, child_pos = stack.pop()
        children = graph[v]
        height = max(height, curr)
        if child_pos < len(children):
            stack.append((v, child_pos+1))
            stack.append((children[child_pos], 0))
            curr += 1
        else:
            curr -= 1
    return height


def main():
    root, graph = get_graph()
    print(get_height(root, graph))


if __name__ == '__main__':
    main()
