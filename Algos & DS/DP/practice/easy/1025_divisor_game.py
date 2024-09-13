# 1. Alice start with a number N and they take turns
# 2. On each player's turn, the current player chooses any X such that 0 < X < N and N % X == 0, 
# then they replace N with N - x.
# 3. 
class SolutionSimple:
  def divisorGame(self, n: int) -> bool:
    return n % 2 == 0

class SolutionDP:
  def divisorGame(self, n: int) -> bool:
    dp = [False] * (n+1)
    dp[1] = False
    
    for i in range(2, n+1):
      for x in range(1, i):
        if i % x == 0 and not dp[i-x]:
          dp[i] = True
          break
    return dp