from typing import Optional

# 988 - Smallest String Starting From Leaf

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
  def dfs(root: Optional[TreeNode], depth: int):
    if not root:
      return
    
    if not root.left and not root.right:
      return depth
    
    return min(dfs(root.left, depth+1) + dfs(root.right, depth+1))
    
    
    