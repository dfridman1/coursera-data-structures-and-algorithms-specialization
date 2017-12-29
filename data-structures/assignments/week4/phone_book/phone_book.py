# python2


class PhoneBookManager:
    def __init__(self, max_number=10000000):
        self.mapping = [None]*(max_number+1)

    def process_query(self, query):
        response = None
        if query.command == 'add':
            self.add(query.number, query.name)
        elif query.command == 'del':
            self.remove(query.number)
        elif query.command == 'find':
            response = self.find(query.number)
        return response

    def add(self, number, name):
        self.mapping[int(number)] = name

    def remove(self, number):
        self.mapping[int(number)] = None

    def find(self, number):
        name = self.mapping[int(number)]
        if name is None:
            name = 'not found'
        return name


class Query:
    def __init__(self, command, number, name=None):
        if command not in self.valid_commands():
            raise ValueError('invalid command {}; must be one of {}'.format(
                repr(command), ', '.join(map(repr, self.valid_commands()))
            ))
        self.command = command
        self.number = number
        self.name = name

    @staticmethod
    def valid_commands():
        return {'add', 'find', 'del'}


def get_queries():
    for _ in xrange(int(raw_input())):
        yield Query(*raw_input().split())


def main():
    phone_book_manager = PhoneBookManager()
    for query in get_queries():
        response = phone_book_manager.process_query(query)
        if response is not None:
            print(response)


if __name__ == '__main__':
    main()
