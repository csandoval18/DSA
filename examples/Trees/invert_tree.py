def invertTree(root):
  if not root:
    return 
    
  invertTree(root.left)
  invertTree(root.right)
  
  tmp = root.left
  root.left = root.right
  root.right = tmp 
  return root
  