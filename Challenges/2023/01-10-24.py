# 1026. Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the max val for which there exists different nodes "a" and "b" where 
# v = | a.val - b.val | and "a" is an ancestor of "b"

#       8
#     /   \
#   3       10
#  /  \        \
# 1    6         14
#     /  \      /
#   4     7   13

# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# ans = |node(8) - node(1)| = 7 = max diff between node and ancestor
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
    
def maxAncestorDiff(root: Optional[TreeNode]) -> int:
  def dfs(node: Optional[TreeNode], min_val: int, max_val: int) -> int:
    if not node:
      return max_val - min_val
    
    min_val = min(min_val, node.val)
    max_val = max(max_val, node.val)
    
    left_diff = dfs(node.left, min_val, max_val)
    right_diff = dfs(node.right, min_val, max_val)
    
    return max(left_diff, right_diff)
  # We start with root vals as max and min differences
  return dfs(root, root.val, root.val)