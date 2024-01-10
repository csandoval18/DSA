class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
def lcaOfThreeNodes(root, node1, node2, node3):
  if not root:
    return None
  
  # If the current node is one of the target nodes, return it
  if root.val == node1.val or root.val == node2.val or root.val == node3.val:
    return root
  
  # Recusrively seearch in the left and right subtrees
  left_LCA = lcaOfThreeNodes(root.left, node1, node2, node3)
  right_LCA = lcaOfThreeNodes(root.right, node1, node2, node3)
  
  # If two nodes are found in different subtrees, the curr node the LCA
  if left_LCA and right_LCA:
    return root
  
  # If only one subtree contains nodes, return the LCA
  return left_LCA if left_LCA else right_LCA

arr = [1,2,3,4,5]
m = 2
print(arr[:m+1] + arr[m+1:][::-1])
