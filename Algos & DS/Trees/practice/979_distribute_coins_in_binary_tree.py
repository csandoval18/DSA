from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def distributeCoins(self, root: Optional[TreeNode]) -> int:
    self.moves = 0
    
    def postorder(node: TreeNode) -> int:
      if not node:
        return 0
      
      left_excess = postorder(node.left)
      right_excess = postorder(node.right)
      
      excess = node.val + left_excess + right_excess - 1
      self.moves += abs(excess)
      
      return excess
    
    postorder(root)
    return self.moves
      