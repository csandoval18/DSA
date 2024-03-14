from typing import List, Optional

# PS: This is not a backtracking question

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val =  val
    self.left = left
    self.right = right
  
def generateTrees(n: int) -> List[Optional[TreeNode]]:
  def rec(start, end):
    if start > end:
      return [None]

    res = []
    
    for i in range(start, end+1):
      left_trees = rec(start, i-1)
      right_trees = rec(i+1, end)

      for left_tree in left_trees:
        for right_tree in right_trees:
          current_tree = TreeNode(i)
          current_tree.left = left_tree
          current_tree.right = right_tree
          res.append(current_tree)

    return res

  if n == 0:
      return []
  return rec(1, n)