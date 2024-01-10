class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
  def getSequence(root: TreeNode):
    if not root:
      return []
  
    if not root.left and not root.right:
      return [root.val]
    
    left_seq = getSequence(root.left)
    right_seq = getSequence(root.right)
    
    return left_seq + right_seq

  return getSequence(root1) == getSequence(root2)