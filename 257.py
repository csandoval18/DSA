class Solution(object):
  def binaryTreePaths(self, root):
    res = []
    self.dfs(root, '')
    return res
  
  def dfs(self, node, res):
    if not node:
      return
      
    path += str(node.val)
    
    if not node.left and not node.right:
      res.append(path)
    else:
      path += '->'
      self.dfs(node.left, path)
      self.dfs(node.right, path)