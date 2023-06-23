class Solution(object):
    def isSymmetric(self, root):
      if not root:
        return True
      return self.isMirror(root.left, root.right)
    
    def isMirror(self, leftNode, rightNode):
      if not leftNode and not rightNode:
        return True
      if not leftNode or not rightNode:
        return False
      return (
        leftNode.val == rightNode.val and
        self.isMirror(leftNode.left, rightNode.right) and
        self.isMirror(leftNode.right, rightNode.left) 
      )
      
      
      
      