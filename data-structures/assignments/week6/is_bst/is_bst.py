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
        last_elem = None
        stack = []
        curr_i = self.root_i
        while len(stack) > 0 or curr_i is not None:
            if curr_i is not None:
                stack.append(curr_i)
                curr_i = self.left_child(curr_i)
            else:
                curr_i = stack.pop()
                key = self.get_key(curr_i)
                if last_elem is not None and key <= last_elem:
                    return False
                else:
                    last_elem = key
                curr_i = self.right_child(curr_i)
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
