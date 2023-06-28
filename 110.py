def isBalanced(self, root):
  
  # dfs function uses a bottom up approach to determine if all nodes are balanced
  # O(n) since every node is checked
  def dfs(root):
    # [balanced?, heightValue]
    
    #base case
    if not root:
      return [True, 0]
      
    # Get to bottom most left and right node of subtrees
    left, right = dfs(root.left), dfs(root.right)
    
    # True or False. Abs gets difference between left and right subtrees
    balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
    
    # 
    return [balanced, 1 + max(left[1], right[1])]
    
  # dfs function returns tuple, so first index is returned for boolean value
  return dfs(root)[0]
    
  
  
   