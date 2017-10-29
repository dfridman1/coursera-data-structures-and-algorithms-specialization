# Uses python2

from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def cover_segments(segments):
    segments = sorted(segments, key=lambda s: s.end)
    points = []
    i = 0
    while i < len(segments):
        end = segments[i].end
        while i < len(segments) and segments[i].start <= end:
            i += 1
        points.append(end)
    return points


def _parse_segments():
    n = int(raw_input())
    segments = []
    for _ in xrange(n):
        start, end = map(int, raw_input().split())
        segments.append(Segment(start=start, end=end))
    return segments


def main():
    segments = _parse_segments()
    points = cover_segments(segments)
    print(len(points))
    print(' '.join(map(str, points)))


if __name__ == '__main__':
    main()
