# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def iterateInOrder(self, i):
    if i == -1:
      return
    self.iterateInOrder(self.left[i])
    self.result.append(self.key[i])
    self.iterateInOrder(self.right[i])

  def inOrder(self):
    self.result = []
    self.iterateInOrder(0)
    return self.result

  def iteratePreOrder(self, i):
    if i == -1:
      return
    self.result.append(self.key[i])
    self.iteratePreOrder(self.left[i])
    self.iteratePreOrder(self.right[i])

  def preOrder(self):
    self.result = []
    self.iteratePreOrder(0)
    return self.result

  def iteratePostOrder(self, i):
    if i == -1:
      return
    self.iteratePostOrder(self.left[i])
    self.iteratePostOrder(self.right[i])
    self.result.append(self.key[i])

  def postOrder(self):
    self.result = []
    self.iteratePostOrder(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
