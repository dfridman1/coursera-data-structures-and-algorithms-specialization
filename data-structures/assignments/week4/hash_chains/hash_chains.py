# python2


def make_string_hash_fn(m):
    p, x = 1000000007, 263

    def hash_fn(string):
        hash = 0
        for c in reversed(string):
            hash = (ord(c) + x*hash) % p
        return hash % m

    return hash_fn


class LinkedList:
    def __init__(self, eq=lambda x, y: x == y):
        self.eq_fn = eq
        self.head = None

    def remove(self, x):
        while not self.empty() and self.eq_fn(self.head.value, x):
            self.head = self.head.next
        if self.empty():
            return
        prev = self.head
        while prev.next is not None:
            if self.eq_fn(prev.next.value, x):
                prev.next = prev.next.next
            else:
                prev = prev.next

    def insert(self, x):
        node = LinkedList.Node(x)
        node.next = self.head
        self.head = node

    def find(self, x):
        node = self._find_node(x)
        return node.value if node is not None else None

    def contains(self, x):
        return self._find_node(x) is not None

    def _find_node(self, x):
        node = self.head
        while node is not None and not self.eq_fn(node.value, x):
            node = node.next
        return node

    def empty(self):
        return self.head is None

    def to_list(self):
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.value)
            node = node.next
        return lst

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class SetChain:
    def __init__(self, num_buckets=1000, create_hash_fn=make_string_hash_fn):
        self.buckets = [LinkedList() for _ in xrange(num_buckets)]
        self.hash_fn = create_hash_fn(num_buckets)

    def add(self, value):
        lst = self.buckets[self.hash_fn(value)]
        if not lst.contains(value):
            lst.insert(value)

    def remove(self, value):
        lst = self.buckets[self.hash_fn(value)]
        lst.remove(value)

    def contains(self, value):
        lst = self.buckets[self.hash_fn(value)]
        return lst.contains(value)

    def get_list(self, bucket_id):
        return self.buckets[bucket_id].to_list()


def process_query(set_chain, query):
    response = None
    if query.command == 'add':
        set_chain.add(query.value)
    elif query.command == 'del':
        set_chain.remove(query.value)
    elif query.command == 'find':
        response = 'yes' if set_chain.contains(query.value) else 'no'
    elif query.command == 'check':
        response = set_chain.get_list(query.value)
        response = ' '.join(response)
    return response


class Query:
    def __init__(self, command, value):
        if command not in self.valid_commands():
            raise ValueError('invalid command {}; must be one of {}'.format(
                repr(command), ', '.join(map(repr, self.valid_commands()))
            ))
        self.command = command
        if command == 'check':
            self.value = int(value)
        else:
            self.value = value

    @staticmethod
    def valid_commands():
        return {'add', 'find', 'del', 'check'}


def read_data():
    num_buckets = int(raw_input())

    def get_queries():
        num_queries = int(raw_input())
        for _ in xrange(num_queries):
            yield Query(*raw_input().split())

    return num_buckets, get_queries


def main():
    num_buckets, queries_generator = read_data()
    set_chain = SetChain(num_buckets)
    for query in queries_generator():
        response = process_query(set_chain, query)
        if response is not None:
            print(response)


if __name__ == '__main__':
    main()
