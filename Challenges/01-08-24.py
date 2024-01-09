from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
  def leafSequence(root):
    if not root:
      return []
  
    # Check if the node is a leaf
    if not root.left and not root.right:
      return [root.val]
    
    # Recursively get the leaf sequence for left and right subtrees
    left_seq = leafSequence(root.left)
    right_seq = leafSequence(root.right)
    
    # Combine the leaf sequences
    return left_seq + right_seq

  return leafSequence(root1) == leafSequence(root2)