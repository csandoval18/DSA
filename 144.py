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