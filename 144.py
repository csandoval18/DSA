class Solution(object):
  def preorderTraversal(self, root):
    result = []
    self.preorderTraversal(root, result)
    return result
    
  def preorderHelper(self, root, result):
    if not root:
      return 
      
    result.append(root.val)
    self.preorderHelper(root.left, result)
    self.preorderHelper(root.right, result)
    
    
    
