from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class SolutionAttempt:
  def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    def dfs(treeNode, listNode):
      if not treeNode:
        return False
      
      if treeNode.val != listNode.val:
        return False
      
      if treeNode.val == listNode.val and listNode.next == None:
        return True
      
      left = dfs(treeNode.left, listNode.next)
      right = dfs(treeNode.right, listNode.next)
      return (left or right)

    if not root:
      return
    
    leftDFS, rightDFS = False, False

    if root.val == head.val:
      leftDFS = dfs(root.left, head.next)
      rightDFS = dfs(root.right, head.next)
    
    self.isSubPath(head, root.left)
    self.isSubPath(head, root.right)

    return (leftDFS or rightDFS)

class SolutionAttempt:
  def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    def dfs(treeNode, listNode):
      if not listNode:
        return True # Entire linked list has been matched
      if not treeNode:
        return False # Reached a leaf in the tree without completing
      if treeNode.val != listNode.val:
        return False # Values don't match 
      
      # Check both left and right subtrees for continuing the list match
      return dfs(treeNode.left, listNode.next) or dfs(treeNode.right, listNode.next)
    
    if not root:
      return False
    
    return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)