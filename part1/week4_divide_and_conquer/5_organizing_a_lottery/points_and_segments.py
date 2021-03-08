# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    points_num = []
    for _, i in sorted(zip(points, range(len(points)))):
        points_num.append(i)

    # order: 0 - starts; 1 - points; 2 - ends
    all_points = [(s, 0) for s in starts]
    all_points.extend([(p, 1) for p in points])
    all_points.extend([(e, 2) for e in ends])

    opened_segments = 0
    i = 0
    for _, point_type in sorted(all_points):
        if point_type == 0:     # starts
            opened_segments += 1
        elif point_type == 2:   # ends
            opened_segments -= 1
        else:                   # complete
            cnt[points_num[i]] = opened_segments
            i += 1

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
