from typing import List


class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
    

class Solution:
  def balanceBST(self, root: TreeNode) -> TreeNode:
    # Helper function to perform in-order traversal and colelct values
    def in_order_traversal(node):
      if not node:
        return []
      return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    # Helper function to build a balanced BST from a sorted array
    def sorted_array_to_bst(arr: List[int]):
      if not arr:
        return None
      mid = len(arr) // 2
      node = TreeNode(arr[mid])
      node.left = sorted_array_to_bst(arr[:mid])
      node.right = sorted_array_to_bst(arr[mid+1:])
      return node
    
    # Get the sorted values from the BST
    sorted_values = in_order_traversal(root)
    # Construct a balanced BST from the sorted values
    return sorted_array_to_bst(sorted_values)