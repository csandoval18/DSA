class Solution(object):
  def invertTree(self, root):
    self.recursiveInvert(root)
    return root
    
  def recursiveInvert(self, root):
    if not root:
      return
      
    self.recursiveInvert(root.left)
    self.recursiveInvert(root.right)
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
  
    
    
    
    
      
    
  