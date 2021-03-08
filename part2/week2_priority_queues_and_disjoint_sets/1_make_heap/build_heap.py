# python3

class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.swaps = []

    def siftDown(self,i):
        while i*2 <= len(self.heap)-1:
            mc = self.getMin(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
                self.swaps.append((i-1, mc-1))
            i = mc

    def getMin(self,i):
        if i*2+1 > len(self.heap)-1:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2+1

    def buildHeap(self,data):
        i = len(data)//2
        self.heap = [0]+data[:]
        while i>0:
            self.siftDown(i)
            i -= 1

    def getSwaps(self):
        return self.swaps

def build_heap(data):
    bh = BinaryHeap()
    bh.buildHeap(data)
    return bh.getSwaps()

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
