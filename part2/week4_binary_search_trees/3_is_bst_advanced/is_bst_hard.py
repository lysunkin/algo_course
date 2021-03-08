#!/usr/bin/python3

import sys, threading

#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**25)  # new thread will get stack of such size

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

def isBinary(tree, i, minimum, maximum):
  if i < 0:
    return True

  if len(tree) == 0:
    return True

  if i >= len(tree):
    return False

  item = tree[i]

  if len(item) < 3:
    return False

  key = item[0]

  if key < minimum or key > maximum: 
    return False

  return isBinary(tree, item[1], minimum, key - 1) and isBinary(tree, item[2], key, maximum)

def IsBinarySearchTree(tree):
  return isBinary(tree, 0, -sys.maxsize+1, sys.maxsize)

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for _ in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
