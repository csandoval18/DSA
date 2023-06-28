def sortedArrayToBST(self, nums):
<<<<<<< HEAD
  #base case
  return
=======
  l = 0
  r = len(nums) -1
  
  def binarySearch(l, r):
    m = (l + r) // 2
    
    # base case 
    if l <= r:
      node = TreeNode(nums[m])
      node.left = binarySearch(l, m - 1)
      node.right = binarySearch(m + 1, r)
      return node
    else: return None
    
    
  return binarySearch(l, r)
    
  
  
>>>>>>> 6b8721014e1de0b346cccc2a033771a73abfa010
