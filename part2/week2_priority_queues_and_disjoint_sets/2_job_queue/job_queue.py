# python3

import math
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class BinaryHeap:
    def __init__(self):
        self.heap = [AssignedJob(-math.inf, -math.inf)]

    def siftUp(self,i):
        while i//2 > 0:
            mid = i//2
            if (self.heap[i].started_at, self.heap[i].worker) < (self.heap[mid].started_at, self.heap[mid].worker):
                self.heap[mid], self.heap[i] = self.heap[i], self.heap[mid]
            i = mid

    def insert(self,k):
      self.heap.append(k)
      self.siftUp(len(self.heap)-1)

    def siftDown(self,i):
        while i*2 <= len(self.heap)-1:
            mc = self.getMin(i)
            if (self.heap[i].started_at, self.heap[i].worker) > (self.heap[mc].started_at, self.heap[mc].worker):
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def getMin(self,i):
        if i*2+1 > len(self.heap)-1:
            return i*2
        else:
            if (self.heap[i*2].started_at, self.heap[i*2].worker) < (self.heap[i*2+1].started_at, self.heap[i*2+1].worker):
                return i*2
            else:
                return i*2+1

    def removeMin(self):
      retval = self.heap[1]
      self.heap[1] = self.heap[len(self.heap)-1]
      self.heap.pop()
      self.siftDown(1)
      return retval

    def buildHeap(self,data):
        i = len(data)//2
        self.heap = [AssignedJob(-math.inf, -math.inf)]+data[:]
        while i>0:
            self.siftDown(i)
            i -= 1

def assign_jobs(n_workers, jobs):
    result = []
    bh = BinaryHeap()
    job_runners = [AssignedJob(k, 0) for k in range(n_workers)]
    bh.buildHeap(job_runners)
    for i in range(len(jobs)):
        runner = bh.removeMin()
        result.append(runner)
        bh.insert(AssignedJob(runner.worker, runner.started_at + jobs[i]))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
