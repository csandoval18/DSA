def hasPathSum(self, root, targetSum):
  if not root:
    return False
    
  if targetSum == root.val and not root.left  and not root.right:
    return True
    
  return (self.hasPathSum(root.left, targetSum - root.val) or
  self.hasPathSum(root.right, targetSum - root.val))
    
   