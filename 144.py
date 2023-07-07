<<<<<<< HEAD
def preorderTraversal(root):
  result = [root.val]
  preorderHelper(root, result)
  return result
  
  
  
def preorderHelper(root, result):
  if not root:
    return 
  preorderHelper(root.left,result)
  result.append(root.val)
  preorderHelper(root.right, result)
  
  return 
=======
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
    
    
    
>>>>>>> 829d037bb324d9d21b32e9fc2d50001ca87569dc
