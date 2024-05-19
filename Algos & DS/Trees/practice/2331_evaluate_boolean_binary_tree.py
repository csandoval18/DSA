from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.right = right
    self.right = right

class Solution:
  def evaluateTree(self, root: Optional[TreeNode]):
    if not root.left and not root.right:
      return root.val
    
    if root.val == 2:
      return self.evaluateTree(root.left) or self.evaluateTree(root.right)
    return self.evaluateTree(root.left) and self.evaluateTree(root.right)
  
def evaluateTreeSub(root: Optional[TreeNode]) -> bool:
  if not root.left and not root.right:
    return root.val
    
  left = evaluateTree(root.left)
  right = evaluateTree(root.right)
  
  if root.val == 2:
    return left or right
  else:
    return left and right