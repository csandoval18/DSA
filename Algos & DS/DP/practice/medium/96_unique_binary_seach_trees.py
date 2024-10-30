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
    right subtrere contain the nodes {i+1, i+2, ..., n} (n-i nodes)

3. Combining left and right subtree counts:
  The total number of unique BSTs for a given root u (i) is the product of the number
  of unique BSTs that can be formed with the left and right subtrees. This is because:
    * For every unique way to arrange the left subtree, there are multiple unique
      ways to arrange the right subtree.
    * If there are left_trees unique ways to arrange the left subtree, and 
      right_trees unique ways to arrange the right subtree, then the total number
      of trees with u (i) as the root is the product left_trees * right_trees.

4. Summing up all possibilities:
  For each possible root i, we add the product of the number of unique left and right 
  subtree trees to the total:
  
  total_trees += left_trees * right_trees
  
  This accounts for all possible configurations where u/i is the root. Since we are 
  interating over all possible roots (from 1 to n), we sum the products for all values of
  u/i 
"""


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
    
class SolutionDP:
  def numTrees(self, n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1 # One unique BST with 0 nodes (empty tree)
    dp[1] = 1 # One unique BST with 1 node
    
    # Fill the DP table for all numbers of nodes from 2 to n
    for num in range(2, n+1):
      # For each possible root node `j` (from 1 to `i`) , calc the number of trees
      for u in range(1, num+1):
        # The number of trees with `i` nodes is the product of left and right subtrees
        left_trees = dp[u-1]
        right_trees = dp[num-u]
        dp[num] += left_trees * right_trees
    
    # The answer is the number of unique BSTs with `n` nodes
    return dp[n]
    
n = 3
# Output: 5
s = SolutionRec()
print(s.numTrees(n))