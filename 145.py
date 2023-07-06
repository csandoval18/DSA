class Solution(object):
  def postorderTraversal(self, root):
    result = []
    self.postorderHelper(root, result)
    return result
    
  def postorderHelper(self, root, result):
    if not root:
      return
    
    self.postorderHelper(root.left, result)
    self.postorderHelper(root.right, result)
    result.append(root.val)
    