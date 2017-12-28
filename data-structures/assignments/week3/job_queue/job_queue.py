# python2


def process_jobs(num_threads, processing_times):
    heap = [(i, 0) for i in xrange(num_threads)]
    for t in processing_times:
        thread_id, start_time = heap[0]
        yield thread_id, start_time
        heap[0] = (thread_id, start_time+t)
        sift_down(heap, 0)


def sift_down(heap, i):
    cmp = lambda i, j: heap[i][1] < heap[j][1] or (heap[i][1] == heap[j][1] and heap[i][0] < heap[j][0])
    while True:
        min_i = i
        left_i, right_i = 2*i+1, 2*i+2
        if left_i < len(heap) and cmp(left_i, min_i):
            min_i = left_i
        if right_i < len(heap) and cmp(right_i, min_i):
            min_i = right_i
        if min_i != i:
            heap[i], heap[min_i] = heap[min_i], heap[i]
            i = min_i
        else:
            break



def get_data():
    num_threads, num_jobs = map(int, raw_input().split())
    processing_times = map(int, raw_input().split())
    return num_threads, processing_times


def main():
    num_threads, processing_times = get_data()
    for thread_id, start_time in process_jobs(num_threads, processing_times):
        print('{} {}'.format(thread_id, start_time))


if __name__ == '__main__':
    main()
