# 1. Convert the problem to a recursive function marked by the pointers i and j and the isTrue variable discussed above.
# 2. Use a loop to check all possible partitions of the expression and calculate the total number of ways.
# 3. Return the total number of ways calculated.
# 4. Base case 1: If i > j, we will return 0.
#    Base case 2: If i and j become equal, we will observe two different cases:

# * Case 1 (If we want the number of ways of true(i.e. isTrue = 1)):
#   If the single operand left is T(true), it will return 1 way and if it is F(false), it will return 0 ways.
# * Case 2 (If we want the number of ways of false(i.e. isTrue = 0)):
#   If the single operand left is T(true), it will return 0 ways and if it is F(false), it will return 1 way.

def parseBoolExprRec(expression: str) -> bool:
  def evaluate(i, j):
    if i == j:
      return expression[i] == 't'
    
    if memo[i][j] != -1:
      return memo[i][j]
    
    result = False
    for k in range(i + 1, j, 2):
      if expression[k] == '&':
        result |= evaluate(i, k - 1) and evaluate(k + 1, j)
      elif expression[k] == '|':
        result |= evaluate(i, k - 1) or evaluate(k + 1, j)
      elif expression[k] == '!':
        result |= (not evaluate(k + 1, j))
    
    memo[i][j] = result
    return result

  n = len(expression)
  memo = [[-1] * n for _ in range(n)]
  return evaluate(0, n - 1)

# Example usage:
expression1 = "!(f)&(t)"
print(parseBoolExprRec(expression1))  # Output: False

expression2 = "|(f,t)"
print(parseBoolExprRec(expression2))  # Output: True


def parseBoolExprTab(expression: str) -> bool:
  n = len(expression)
  
  # dp[i][j][0] stores the result of expression[i:j+1] being evaluated to False
  # dp[i][j][1] stores the result of expression[i:j+1] being evaluated to True
  dp = [[[False, False] for _ in range(n)] for _ in range(n)]
  
  for i in range(n):
    if expression[i] == 't':
      dp[i][i][1] = True
    elif expression[i] == 'f':
      dp[i][i][0] = True
  
  for length in range(3, n+1, 2):
    for i in range(n - length + 1):
      j = i + length - 1
      for k in range(i+1, j, 2):
        if expression[k] == '&':
          dp[i][j][0] |= dp[i][k-1][0] and dp[k+1][j][0]
          dp[i][j][1] |= dp[i][k-1][1] and dp[k+1][j][1]
        elif expression[k] == '|':
          dp[i][j][0] |= dp[i][k-1][0] or dp[k+1][j][0]
          dp[i][j][1] |= dp[i][k-1][1] or dp[k+1][j][1]
        elif expression[k] == '!':
          dp[i][j][0] |= dp[i][k+1][1] and dp[k+2][j][0]
          dp[i][j][1] |= dp[i][k+1][0] and dp[k+2][j][1]

  return dp[0][n-1][1]

# Example usage:
expression1 = "!(f)&(t)"
print(parseBoolExprTab(expression1))  # Output: False

expression2 = "|(f,t)"
print(parseBoolExprTab(expression2))  # Output: True


def parseBoolExprRec2(expression: str) -> bool:
  def evaluate(expr):
    if expr == 't':
      return True
    elif expr == 'f':
      return False
    elif expr.startswith('!'):
      return not evaluate(expr[2:-1])
    elif expr.startswith('&'):
      return all(evaluate(subexpr) for subexpr in expr[2:-1].split(','))
    elif expr.startswith('|'):
      return any(evaluate(subexpr) for subexpr in expr[2:-1].split(','))

  return evaluate(expression)

# Example usage:
expression1 = "!(f)&(t)"
print(parseBoolExprRec2(expression1))  # Output: False

expression2 = "|(f,t)"
print(parseBoolExprRec2(expression2))  # Output: True