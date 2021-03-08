# Uses python3
import sys

def generate_hops(n):
    hops = [0] * (n + 1)

    hops[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        min_hops = min([hops[x] for x in indices])
        hops[i] = min_hops + 1

    return hops

def optimal_sequence(n):

    hops = generate_hops(n)

    current = n
    optimal_seq = [current]
    while current != 1:

        candidates = [current - 1]
        if current % 2 == 0:
            candidates.append(current // 2)
        if current % 3 == 0:
            candidates.append(current // 3)

        current = min([(c, hops[c]) for c in candidates], key=lambda x: x[1])[0]
        optimal_seq.append(current)

    return reversed(optimal_seq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
