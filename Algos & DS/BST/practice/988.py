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
    
def smallestFromLeaf(root):
  if not root:
    return ""
  
  # Helper function to convert numeric value to character
  def to_char(val):
    return chr(val + ord('a'))

  # DFS function to find the smallest string
  def dfs(node):
    if not node:
        return None
    
    # Convert current node's value to character and append it to the path
    current_char = to_char(node.val)
    
    # Recursively find the smallest string from both children
    left_smallest = dfs(node.left)
    right_smallest = dfs(node.right)
    
    # Determine the smallest string between left and right child
    if left_smallest is None and right_smallest is None:
      return current_char  # Leaf node, return its character
    elif left_smallest is None:
        return right_smallest + current_char
    elif right_smallest is None:
        return left_smallest + current_char
    else:
        # Choose the lexicographically smaller string and append the current character
        return (min(left_smallest, right_smallest) + current_char)

  # Call the DFS function starting from the root
  return dfs(root)
  