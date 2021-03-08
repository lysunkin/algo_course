# Uses python3
def edit_distance(s, t):
    distances = [[x] + [0]*len(t) for x in range(len(s)+1)]
    distances[0] = [x for x in range(len(t)+1)]

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = min(distances[i][j-1], distances[i-1][j], distances[i-1][j-1])+1

    return distances[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
