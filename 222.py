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
    cnt = dfs(root.left, cnt)
    cnt = dfs(root.right, cnt)

    return cnt
    
  res = 0
  dfs(root, res)
  return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(countNodes(root))