# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# class Solution(object):
#   def isSameTree(self, p, q):
#     pnums = []
#     qnums = []
#     self.inorderHelper(p, q, pnums, qnums)
#     if pnums != qnums:
#       return false
#     else: return true

#   def inorderHelper(self, p, q, pnums, qnums):
#     if p or q is None:
#       return
#     self.inorderHelper(p.left, q.left, pnums, qnums)
#     pnums.append(p.val)
#     qnums.append(q.val)
#     self.inorderHelper(p.right, q.right, pnums, qnums)


class Solution:
  def isSameTree(self, p, q):
    # Check if both trees are empty (base case)
    # if p == null || q == null
    if not p and not q:
        return True
    # Check if only one tree is empty (base case)
    if not p or not q:
        return False
    # Check if node values are different
    if p.val != q.val:
        return False
    # Recursively check left and right subtrees
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)