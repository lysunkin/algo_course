# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    ordered_by_ends = sorted(segments, key=lambda s: s.end)

    while ordered_by_ends:
        segment = ordered_by_ends.pop(0)
        intersection = segment.end
        points.append(intersection)

        for s in ordered_by_ends[:]:
            if s.start <= intersection and intersection <= s.end:
                ordered_by_ends.remove(s)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
