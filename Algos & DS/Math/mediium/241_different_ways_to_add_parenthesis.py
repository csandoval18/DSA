class Solution:
  def diffWaysToCompute(self, expression: str) -> List[int]:
    def helper(expr):
      if expr.isdigit():
        return [int(expr)]
      
      results = []
      for i, char in enumerate(expr):
        if char in "+-*":
            # Divide the expression at the operator
            left = helper(expr[:i])
            right = helper(expr[i+1:])
            
            # Combine results from left and right sub-expressions
            for l in left:
              for r in right:
                if char == '+':
                  results.append(l + r)
                elif char == '-':
                    results.append(l - r)
                elif char == '*':
                    results.append(l * r)
    
      return results
  
    return helper(expression)