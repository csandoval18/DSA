class SolutionRecursion:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1
    return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
class SolutionRecursion:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1
    return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

class SolutionTabulation:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1
      
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
      dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return dp[n]

class SolutionSO:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1

    f = 0
    s = 1
    t = 1
    c = 0

    for i in range(3, n+1):
      c = f + s + t
      tmp = t
      t = c
      tmp2 = s
      s = tmp
      f = tmp2

    return c
  
n = 4
s = SolutionTabulation()
print(s.tribonacci(n))