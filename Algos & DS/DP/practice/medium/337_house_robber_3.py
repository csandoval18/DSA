from typing import Optional, Tuple

'''
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a
binary tree. It will automatically contat the police if two directly-linked
houses were broken into on the same night.

Given the root of the binary tree, return the max amount of money the thief
can rob without alerting the police
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# This attempt doesn't work because it only considers picking one child at a time 
# (either left or right) when parentRobbed == 0, rather than combining both subtrees' values
# The problem is that you'ree choosing either the left or right subtree, when you should be
# evaluating both.

class SolutionAttempt:
  def rob(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    def helper(node, parentRobbed: int) -> int:
      if not node:
        return 0 
      
      if parentRobbed == 0:
        pickLeft = node.val + helper(node.left, 1)
        pickRight = node.val + helper(node.right, 1)
        return max(pickLeft, pickRight)
      else:
        notPickLeft = helper(node.left, 0)
        notPickRight = helper(node.right, 0)
        return max(notPickLeft, notPickRight)
    
    return max(helper(root, 0), helper(root, 1))


class SolutionRec:
  def rob(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    def helper(node: Optional[TreeNode], parentRobbed: int) -> int:
      if not node:
        return 0
      
      if parentRobbed == 0:
        # If parent is not robbed, we can either rob the current node or skip it
        robNode = node.val + helper(node.left, 1) + helper(node.right, 1)
        skipNode = helper(node.left, 0) + helper(node.right, 0)
        return max(robNode, skipNode)
      else:
        # If parent is robbed, we cannot rob the current node
        return helper(node.left, 0) + helper(node.right, 0)
    return helper(root, 0)


class SolutionMemo:
  def rob(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    memo = {}
    
    def helper(node: Optional[TreeNode], parentRobbed: int) -> int:
      if not node:
        return 0
        
      if (node, parentRobbed) in memo:
        return memo[((node, parentRobbed))]
      
      if parentRobbed == 0:
        robNode = node.val + helper(node.left, 1) + helper(node.right, 1)
        skipNode = helper(node.left, 0) + helper(node.right, 0)
        res = max(robNode, skipNode)
      else:
        res = helper(node.left, 0) + helper(node.right, 0)
      
      memo[(node, parentRobbed)] = res
      return res
    return helper(root, 0)


class SolutionMemo:
  def rob(self, root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
      # Base case: if there's no node, return (0, 0)
      if not node:
        return (0, 0)
      
      # Postorder traversal to calculate values from children up to the root
      left = dfs(node.left)
      right = dfs(node.right)
      
      # If we rob this node, we cannot rob its children
      rob = node.val + left[1] + right[1]
      notRob = max(left) + max(right)
      
      # Return a tuple (rob, notRob) for this node
      return (rob, notRob)
      