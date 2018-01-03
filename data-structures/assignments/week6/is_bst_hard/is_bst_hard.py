# python2


class Tree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.root_i = 0 if len(nodes) > 0 else None

    def get_key(self, node_i):
        return self.get_node(node_i).key

    def left_child(self, node_i):
        return self.get_node(node_i).left_i

    def right_child(self, node_i):
        return self.get_node(node_i).right_i

    def get_node(self, node_i):
        return self.nodes[node_i]

    def is_bst(self):
        stack = []
        l, curr_i, u = float('-inf'), self.root_i, float('inf')
        while len(stack) > 0 or curr_i is not None:
            if curr_i is not None:
                key = self.get_key(curr_i)
                if key < l or key >= u:
                    return False
                stack.append((l, curr_i, u))
                curr_i, u = self.left_child(curr_i), self.get_key(curr_i)
            else:
                l, curr_i, u = stack.pop()
                curr_i, l = self.right_child(curr_i), self.get_key(curr_i)
        return True

    @staticmethod
    def parse_tree():
        num_vertices = int(raw_input())
        nodes = []
        for _ in xrange(num_vertices):
            key, left_i, right_i = map(int, raw_input().split())
            nodes.append(Tree.Node(key, left_i if left_i != -1 else None, right_i if right_i != -1 else None))
        return Tree(nodes)

    class Node:
        def __init__(self, key, left_i, right_i):
            self.key = key
            self.left_i = left_i
            self.right_i = right_i


def main():
    tree = Tree.parse_tree()
    print('CORRECT' if tree.is_bst() else 'INCORRECT')


if __name__ == '__main__':
    main()
