
class SolutionRec:
  def numTrees(self, n: int) -> int:
    # Base case: Empty tree or single node tree
    if n == 0 or n == 1:
      return 1
    
    # Initialize total number of unique BSTs
    total_trees = 0
    
    # Loop through each number as a root (from 1 to n)
    for u in range(1, n+1):
      # Recursively count the number of trees in the left and right subtrees
      left_trees = self.numTrees(u-1)
      right_trees = self.numTrees(n-u)
      
      # Multiply the number of unique trees on the left and right and add to total
      total_trees += left_trees * right_trees
    return total_trees

# Recursion Explanaition | PS: u = i
""" 
1. Choosing the root:
  In a BST, the root node determines how the tree is structured.
  Any node from 1 ton can be selected as the root. 
    - For each root node i, all nodes less than i must go into the left subtree,
    - All nodes greater than i must go into the right subtree.

2. Recursively counting trees for left and right subtrees:
For each root node i:
  left subtree contains the nodes {1,2, ..., i-1} (i-1 nodes)
"""

class SolutionMemo:
  def numTrees(self, n: int) -> int:
    memo = [-1] * (n+1)
    
    def helper(num: int) -> int:
      if n == 0 and n == 1:
        return 1
      
      if memo[n] != -1:
        return memo[n]
      
      total_trees = 0
      
      for u in range(1, n+1):
        left_trees = helper(u-1)
        right_trees = helper(n-u)
        total_trees += left_trees * right_trees
        
      memo[n] = total_trees
      return total_trees
    return helper(n)

n = 3
# Output: 5
s = SolutionRec()
print(s.numTrees(n))