from typing import List

def coinChange(self, coins: List[int], amount: int) -> int:
  def f(idx: int, target: int) -> int:
    if idx == 0:
      # If the target T is divisible by the first element, 
      if target % coins[0] == 0:
        return target // [0]
      else:
        return int(1e9)