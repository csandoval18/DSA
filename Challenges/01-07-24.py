from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left 
    self.right = right
    
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
  if not root:
    return 0
    
  total_sum = 0
  
  if low <= root.val <= high:
    total_sum += root.val
  
  total_sum += self.rangeSumBST(root.left, low, high)
  total_sum += self.rangeSumBST(root.right, low, high)
  
  return total_sum
    