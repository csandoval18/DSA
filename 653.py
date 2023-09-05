def findTarget(root, k):
  
  def inorder(root):
    if not root: return False
    
    x = k - root.val
    
    if x not in hm:
      hm[root.val] = root
    else:
      return True
    
    return inorder(root.left) or inorder(root.right)
    
  hm = {}
  res = inorder(root, k, hm)
  return res
  
  # ////////////////// FIRST ATTEMPT ////////////////
  
  # Did not work
  
# def findTarget(root, k):
#   hm = {}
#   res = inorder(root, k, hm)
#   return res

# def findTargetHelper(root, k, hm):
#   if not root: return

#   x = k - root.val
  
#   if x not in hm:
#     hm[root.val] = root
#   else: 
#     res = True

#   findTargetHelper(root.left, k, hm)
#   findTargetHelper(root.right, k, hm)
  