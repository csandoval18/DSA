from typing import List

# Tabulation

# 1. Base case
# 2. Iterate for each changing parameter (idx & weight) => 2 nested loops
# 3. Copy the recurrence

def knapsack(weights: List[int], values: List[int], maxWeight: int) -> None:
  def f(idx: int, ) -> int:
    if idx == 0:
      if weights[0] <= 