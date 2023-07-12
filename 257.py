class Solution(object):
  def binaryTreePaths(self, root):
    paths = []
    self.dfs(root, '')
    return paths
  
  def dfs(self, node, path):
    if not node:
      return
      
    path += str(node.val)
    
    if not node.left and not node.right:
      paths.append(path)
    else:
      path += '->'
      self.dfs(node.left, path)
      self.dfs(node.right, path)