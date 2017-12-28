# python2


import sys
from collections import namedtuple


Query = namedtuple('Query', 'source destination')


class TableMerger:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.parents = [i for i in xrange(len(row_counts))]
        self.ranks= [0 for _ in xrange(len(row_counts))]
        self.max_size = max(self.row_counts)

    def merge(self, query):
        p_source = self.get_parent(query.source)
        p_destination = self.get_parent(query.destination)
        if p_source != p_destination:
            if self.ranks[p_source] > self.ranks[p_destination]:
                p_destination, p_source = p_source, p_destination
            if self.ranks[p_source] == self.ranks[p_destination]:
                self.ranks[p_destination] += 1
            self.parents[p_source] = p_destination
            self.row_counts[p_destination] += self.row_counts[p_source]
            self.row_counts[p_source] = 0
            self.max_size = max(self.max_size, self.row_counts[p_destination])

    def get_parent(self, i):
        p = self.parents[i]
        if i != p:
            self.parents[i] = self.get_parent(p)
        return self.parents[i]


def get_row_counts():
    raw_input()
    return map(int, raw_input().split())


def get_queries():
    while True:
        try:
            d, s = map(int, raw_input().split())
            yield Query(s-1, d-1)  # force 0-based indexing
        except EOFError:
            break


def main():
    row_counts = get_row_counts()
    merger = TableMerger(row_counts)
    for query in get_queries():
        merger.merge(query)
        print(merger.max_size)


if __name__ == '__main__':
    main()
