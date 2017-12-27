# python2


class Node:
    def __init__(self, value):
        self.value = value
        self.next_e = self.prev_e = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self._sz = 0

    def size(self):
        return self._sz

    def empty(self):
        return self.size() == 0

    def enqueue(self, value):
        node = Node(value)
        if self.empty():
            self.head = self.tail = node
        else:
            self.tail.next_e = node
            self.tail = node
        self._sz += 1

    def dequeue(self):
        self.head = self.head.next_e
        if self.head is not None:
            self.head.prev_e = None
        self._sz -= 1

    @property
    def first(self):
        return self.head.value

    @property
    def last(self):
        return self.tail.value



class Request:
    def __init__(self, start_t, processing_t):
        self.start_t = start_t
        self.processing_t = processing_t

    @property
    def end_t(self):
        return self.start_t + self.processing_t


def process_requests(requests, buffer_size):
    response_times = []
    buffer = Queue()
    request_id = 0
    while request_id < len(requests):
        request = requests[request_id]
        if buffer.size() < buffer_size:
            start_t = request.start_t
            if not buffer.empty():
                start_t = max(request.start_t, buffer.last.end_t)
            request.start_t = start_t
            buffer.enqueue(request)
            response_times.append(start_t)
            request_id += 1
        else:
            while not buffer.empty() and buffer.first.end_t <= request.start_t:
                buffer.dequeue()
            if buffer.size() == buffer_size:
                response_times.append(-1)
                request_id += 1
    return response_times


def read_data():
    buffer_size, num_requests = map(int, raw_input().split())
    requests = []
    for id in xrange(num_requests):
        start_t, processing_t = map(int, raw_input().split())
        requests.append(Request(start_t, processing_t))
    return buffer_size, requests

def main():
    buffer_size, requests = read_data()
    response_times = process_requests(requests, buffer_size)
    for t in response_times:
        print(t)


if __name__ == '__main__':
    main()
