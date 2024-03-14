from typing import List

# Tabulation

# 1. Base case
# 2. Iterate for each changing parameter (idx & weight) => 2 nested loops
# 3. Copy the recurrence

def knapsackRecursive(weights: List[int], values: List[int], weightCapacity: int) -> None:
  def f(idx: int, capacity) -> int:
    # Base case: If we are at the first item (idx = 0), check if it can be included in theknacksack
    if idx == 0:
      if weights[0] <= capacity:
        return values[0]
      else:
        return 0
    
    # In the not take once the index decreases since we are not performing any changes to the initial weight and sum
    notTake = 0 + f(idx-1, capacity)
    
    take = float('-inf') 
    if weights[idx]  <= capacity:
      take = values[idx] + f(idx-1, capacity - weights[idx])
    
    return max(take, notTake)
  
  n = len(weights)
  return f(n-1, weightCapacity)

def knapsackMemoization(weights: List[int], values: List[int], weightCapacity: int)  -> None:
  def f(row: int, capacity: int, dp: List[List[int]]) -> bool:
    # Base case: If we are at the first item (idx = 0), check if it can be included in theknacksack
    if row == 0:
      if weights[0] <= capacity:
        return values[0]
      else:
        return 0
    
    # If the result for this combination of current 'row'(idx) and 'capacity' has already been computed
    if dp[row][capacity] != -1:
      return dp[row][capacity]
    
    # Calculate the value when the current item is taken and not taken (subsets)
    notTake = 0 + f(row-1, capacity, dp)
    
    take = float('-inf')
    if weights[row] <= capacity:
      take = values[row] + f(row-1, capacity - weights[row], dp)
    
    # Update the dp table with the max of the two possibilities
    dp[row][capacity] = max(take, notTake)
    return dp[row][capacity]
  
  n = len(values)
  dp = [[-1 for _ in range(weightCapacity+1)] for _ in range(n)]
  f(n-1, weightCapacity, dp)
  
  return f(n-1, weightCapacity, dp)
  
def knapsackTabulation(weights: List[int], values: List[int], capacity: int)  -> int:
  # Initialize a 2D dp array to store the maximum value for different capacities and items
  n = len(values)
  dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
  
  for j in range(weights[0], capacity+1):
    dp[0][j] = values[0]
  print(dp)
    
  # Iterate through the items and capacities both changing parameters
  for i in range(1, n):
    for cap in range(capacity+1):
      # Calculate the maximun value when the current item is not taken
      notTake = 0 + dp[i-1][cap]
      #Calculate the max value when the current item is taken
      take = float('-inf')
      if weights[i] <= cap:
        take = values[i] + dp[i-1][cap-weights[i]]
      
      # Update the dp table with the max of not taken of the dp array 
      dp[i][cap] = max(notTake, take)
  
  # The result is stored in the bottom-right cell of the dp array
  print()
  for i in range(len(dp)):
    print(dp[i])
  print()
  return dp[n-1][capacity]

# def knapsackTabulation(weights: List[int], values: List[int], capacity: int)  -> int:
#   n = len(values)
#   dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
  
#   for j in range(1, capacity+1):
#     dp[0][j] = values[0]

# Knapsack 1 list space optimization not the 2 array "Rolling Array" Technique

# This technique is possible because each element of the dynamic programming 
# table (knapsack table) depends only on the values in the previous row. 
# Therefore, we don't need to keep the entire table in memory

  
def knapsackSO(weights: List[int], values: List[int], capacity: int) -> int:
  # We initialize to capacity+1 because we dont need the 0 index and index capacity 
  n = len(values)
  prev = [0] * (capacity+1)
  
  # Base condition: Fill in the first row of 'prev' based on the capacity 
  for i in range(weights[0], capacity+1):
    prev[i] = values[0]  
  
  # Iterate through the items and capacities in reverse order
  for i in range(1, n):
    for cap in range(capacity, weights[i]-1, -1):
      # Calculate the max value when the current item is not taken
      notTake = 0 + prev[cap]
      
      take = float('-inf')
      if weights[i] <= capacity:
        take = values[i] + prev[cap - weights[i]]
      
      # Update the prev list with the maximum of notTaken and taken values
      prev[cap] = max(notTake, take)
  # The result is stored in 'prev[capacity]', representing the max value of items 
  # the thief can steal
  return prev[capacity]

weights = [1, 2, 4, 5]
values = [5, 4, 8, 6]
capacity = 5
n = len(weights)

print(knapsackRecursive(weights, values, capacity))
print(knapsackMemoization(weights, values, capacity))
print(knapsackTabulation(weights, values, capacity))
print(knapsackSO(weights, values, capacity))