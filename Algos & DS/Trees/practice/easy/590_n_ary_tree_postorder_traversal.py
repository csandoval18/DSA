class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    def helper(node):
      if not node:
        return
      
      for child in node.children:
        helper(child)
      res.append(child) 
    
    res = []
    helper(root)
    return res