from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def countNodes(root: Optional[TreeNode]) -> int:
  def dfs(root: Optional[TreeNode], cnt: int) -> int:
    if not root:
      return 
    
    cnt += 1
    dfs(root.left, cnt)
    dfs(root.right, cnt)
    
  cnt = 0
  dfs(root, cnt)
  return cnt