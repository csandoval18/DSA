
class SolutionRec:
  def numTrees(self, n: int) -> int:
    # Base case: Empty tree or single node tree
    if n == 0 or n == 1:
      return 1
    
    # Initialize total number of unique BSTs
    total_trees = 0
    
    # Loop through each number as a root (from 1 to n)
    for i in range(1, n+1):
      # Recursively count the number of trees in the left and right subtrees
      left_trees = self.numTrees(i-1)
      right_trees = self.numTrees(n-i)
      
      # Multiply the number of unique trees on the left and right and add to total
      total_trees += left_trees * right_trees
    return total_trees

n = 3
# Output: 5
s = SolutionRec()
print(s.numTrees(n))