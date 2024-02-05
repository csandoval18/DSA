from ast import List
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

def pathSum(root: Optional[TreeNode]) -> List[List[int]]:
  def backtrack(node: Optional[TreeNode], targetSum: int, ds: List[int]):
    if not node:
      return

    ds.append(node.val)

    if not node.left and not node.right and targetSum - node.val == 0:
      res.append(ds[:])
    
    backtrack(node.left, targetSum-node.val, ds)
    backtrack(node.right, targetSum-node.val, ds)
    
    ds.pop()

  res = []
  backtrack(root, targetSum, [])
  return res


root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22

def createBST(treeValues: List[int]) -> Optional[TreeNode]:
  n = len(treeValues)
  left = 1
  right = 2
  
  node = TreeNode(treeValues[0])
  head = node
  while right < n:
    node.left = TreeNode(treeValues[left])
    node.right = TreeNode(treeValues[right])
    
    left += 2
    right += 2
    
    
    