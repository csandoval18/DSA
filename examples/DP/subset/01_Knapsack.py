from typing import List

# Tabulation

# 1. Base case
# 2. Iterate for each changing parameter (idx & weight) => 2 nested loops
# 3. Copy the recurrence

def knapsackRecursive(weights: List[int], values: List[int], maxWeight: int) -> None:
  def f(idx: int, maxW) -> int:
    if idx == 0:
      if weights[0] <= maxW:
        return values[0]
      else:
        return 0
    
    notTake = 0 + f(idx-1, maxW-weights[idx])
    take = float('-inf') 
    if weights[idx]  <= maxW:
      take = values[idx] + f(idx-1, maxW - weights[idx])
    
    return max(take, notTake)

def knapsackDP(weights: List[int], values: List[int], maxWeight: int)  -> None:
  def f(idx: int, maxW: int, dp: List):
  