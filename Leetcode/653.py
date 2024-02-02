def findTarget(root, k):
  
  def dfs(root):
    if not root: return False
    
    x = k - root.val
    
    if x not in hm:
      hm[root.val] = root
    else:
      return True
    
    return dfs(root.left) or dfs(root.right)
    
  hm = {}
  res = dfs(root, k, hm)
  return res


# DFS Preorder solution (starts in root)

def findTarget(root, k):
  def dfs(node):
    if not node: return False
    
    x = k - node.val
    if x not in visited:
      visited.add(node.val)
    else:
      return True
    
    return dfs(node.left) or dfs(node.right)
  
  visited = set()
  return dfs(root)
  
# ////////////////// FIRST ATTEMPT ///////////////////

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
  
  
# //////////////////// For Educational purposes //////////////////////

# Inorder solution
def findTarget(root, k):
  def inorder(node):
      if not node:
          return False
          
      if inorder(node.left):
          return True
          
      if (k - node.val) in visited:
          return True
      else:
        visited.add(node.val)
      
      return inorder(node.right)

  visited = set()
  return inorder(root)

# Postorder solution
def findTarget(root, k):
  def postorder(node):
    if not node: return False
    
    if postorder(node.left):
      return True
    
    if postorder(node.right):
      return True
    
    if k-node.val not in visited:
      visited.add(node.val)
    else:
      return True
    
    return False
  
  visited = set()
  return postorder(root)
  