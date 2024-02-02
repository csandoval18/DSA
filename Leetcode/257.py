# Get all paths of from root to leaf node in tree
# Fomart of result example: ["1->2->3", "1->5->6"]
class Solution(object):
  def binaryTreePaths(self, root):
    res = []
    
    def dfs(self, node):
      if not node:
        return
        
      path += str(node.val)
      
      if not node.left and not node.right:
        res.append(path)
      else:
        path += '->'
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        
    self.dfs(root, '')
    return res


class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        self.dfs(root, "", res)
        return res
    
    def dfs(self, node, path, res):
        if not node:
            return
        
        path += str(node.val)
        
        if not node.left and not node.right:
            res.append(path)
        else:
            path += '->'
            self.dfs(node.left, path, res)
            self.dfs(node.right, path, res)