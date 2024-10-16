from typing import List, Optional

# Given an integer n, return all the structurally unique BST's (binary search trees), 
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class SolutionRec:
  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    if n == 0:
      return []
      
    def helper(start: int, end: int) -> List[Optional[TreeNode]]:
      if start > end:
        return [None]
      
      allTrees = []
      for i in range(start, end+1): # i = root of BST
        # Recursively generate all left and right subtrees
        leftTrees = helper(start, i-1)
        rightTrees = helper(i+1, end)
        
        # Combine each left and right subtree with the current root i
        for l in leftTrees:
          for r in rightTrees:
            currTree = TreeNode(i)
            currTree.left = l
            currTree.right = r
            allTrees.append(currTree)
        return allTrees
      return helper(1, n)
            