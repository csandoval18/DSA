#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#Input: p = [1,2,3], q = [1,2,3]
#Output: true

class Solution(object):
  def isSameTree(self, p, q):
    pnums = []
    qnums = []
    self.inorderHelper(p, q, pnums, qnums)
    if pnums != qnums:
      return false
    else: return true
  
  def inorderHelper(self, p, q, pnums, qnums):
    if p and q is None:
      return
    self.inorderHelper(node.left, result)
    result.append(node.val)
    self.inorderHelper(node.right, result)
    
    