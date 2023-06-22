#graphs

#recursive pseudo
# def inorderTraversal(self, root):
#   ans = []
#   if not root:
#     return 
#   #traverse to left-most tree node
#   inorderTraversal(root.left)
#   #process node
#   ans.append(root.val)
#   inorderTraversal(root.right)
#   return ans


#recursive approach
class Solution:
    def inorderTraversalRecursive(self, root):
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, node, result):
        if node is None:
            return
        self.inorderHelper(node.left, result)
        result.append(node.val)
        self.inorderHelper(node.right, result)



class Solution:
  def inorderTraversal(self, root):
    result = []
    stack = []
    current = root
    
    while stack or current:
      while current:
          stack.append(current)
          current = current.left
      current = stack.pop()
      result.append(current.val)
      current = current.right
    
    return result
