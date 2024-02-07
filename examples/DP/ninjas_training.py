from typing import List

# Greedy fails => try all possible ways
# try all possible ways => recursion
# 1. Express every possible problem terms of idx
# 2. Do changes on that idx 
# 3. Find the max 
def ninjaTraining(n: int, points: List[List[int]]) -> int:
  def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)