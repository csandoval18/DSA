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
    