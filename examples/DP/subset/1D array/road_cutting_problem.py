from typing import List

def unboundedKnapsack(knapsack: int, values: List[int], weights: List[int]) -> int:
  def f(idx: int, capacity: int) -> int:
    # Base case: If there are no more itens to consider (idx = 0)
    if idx == 0:
      return (capacity // weights[0]) * values[0]
    
    notTake = 0 + f(idx-1, capacity)
    
    take = float('-inf')
    if weights[idx] <= capacity:
      take = values[idx] + f(idx, capacity - weights[idx])
    
    return max(notTake, take)

  n = len(values)
  return f(n-1, knapsack)
  
def unboundedKnapsackMemo(knapsack: int, values: List[int], weights: List[int]) -> int:
  def f(idx: int, capacity: int, dp: List[List[int]]) -> int:
    # Base case: If there are no more itens to consider (idx = 0)
    if idx == 0:
      return (capacity // weights[0]) * values[0]
    
    if dp[idx][capacity] != -1:
      return dp[idx][capacity]
    
    notTake = 0 + f(idx-1, capacity, dp)
    
    take = float('-inf')
    if weights[idx] <= capacity:
      take = values[idx] + f(idx, capacity - weights[idx], dp)
    
    dp[idx][capacity] = max(notTake, take)
    return dp[idx][capacity]

  n = len(values)
  dp = [[-1 for _ in range(knapsack+1)] for _ in range(n)]
  return f(n-1, knapsack, dp)
  
def unboundedKnapsackTab(knapsack: int, values: List[int], weights: List[int]) -> int:
  n = len(values)
  dp = [[0 for _ in range(knapsack+1)] for _ in range(n)]
  
  for cap in range(weights[0], knapsack+1, weights[0]):
    dp[0][cap] = (cap // weights[0]) * values[0]
    
  for i in range(1, n): 
    for cap in range(knapsack+1):
      notTake = 0 + dp[i-1][cap]
      
      take = float('-inf')
      if weights[i] <= cap:
        take = values[i] + dp[i][cap - weights[i]]
      
      dp[i][cap] = max(notTake, take)

  return dp[n-1][knapsack]
  
def unboundedKnapsackSO(knapsack: int, values: List[int], weights: List[int]) -> int:
  n = len(values)
  prev = [0]*(knapsack+1)
  
  for cap in range(weights[0], knapsack+1, weights[0]):
    prev[cap] = (cap // weights[0]) * values[0]
    
  for i in range(1, n): 
    curr = [0]*(knapsack+1)
    for cap in range(knapsack+1):
      notTake = 0 + prev[cap]
      
      take = float('-inf')
      if weights[i] <= cap:
        take = values[i] + curr[cap - weights[i]]
      
      curr[cap] = max(notTake, take)
    prev = curr

  return prev[knapsack]
  
weights = [2,4,6]
values = [5,11,13]
knapsack = 10

print(unboundedKnapsack(knapsack, values, weights))
print(unboundedKnapsackMemo(knapsack, values, weights))
print(unboundedKnapsackTab(knapsack, values, weights))
print(unboundedKnapsackSO(knapsack, values, weights))