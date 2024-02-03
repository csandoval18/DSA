from typing import List, Optional

class TreeNode:
  def __init__(self, left=None, right=None, val=0) -> None:
    self.left = left
    self.right = right
    self.val = val

def pathSum(self, root: Optional[TreeNode]) -> List[List[int]]:
  def backtrack(node: Optional[TreeNode], ds: List[int]):
    if not node:
      res.append(ds[:])
      return
    
    backtrack()
    
    
  
  res = []