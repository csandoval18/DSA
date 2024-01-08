from ast import List

def frogJump(n: int, heights: List[int]) -> int:
  def frog_energy(i: int, heights: List[int]) -> int:
    # BC last floor no energy used
    if i == 0:
      return 0
    
    left = frog_energy(i-1, heights) + abs(heights[i] - heights[i-1])
    right = float('inf')
    
    # Condition check if i>1 because it's not possible to jump 2 floors if the floor left is 1 or less
    if i>1:
      right = frog_energy(i-1, heights) + abs(heights[i] - heights[i-1])
    
    return min(left, right) 
      
      
  # Recusive function starting from 0
  def min_cost_recursive(heights, curr_idx):
    # Base case: if at the first position, no cost to move
    if curr_idx == 0:
      return 0

    # Base case: if at the second position, consider only 1-step move
    if curr_idx == 1:
      return abs(heights[curr_idx] - heights[curr_idx - 1])

    # Calculate the cost for taking 1 step
    one_step_cost = abs(heights[curr_idx] - heights[curr_idx - 1]) + min_cost_recursive(heights, curr_idx - 1)
    # Calculate the cost for taking 2 steps
    two_step_cost = abs(heights[curr_idx] - heights[curr_idx - 2]) + min_cost_recursive(heights, curr_idx - 2)

    # Return the minimum of the two costs
    return min(one_step_cost, two_step_cost)
    
    
  # Recursive function starting from n-1
  def rec(heights, curr_idx):
    # Base case: if at the last position, no cost to move
    if curr_idx == n-1: 
      return 0
    
    # Base case: if at the second-to-last position, 
    # consider only 1-step move
    if curr_idx == n-2:
      return abs(heights[curr_idx]-heights[curr_idx + 1])
    
    # Calculate the cvost for taking 1 step
    one_step_cost = abs(heights[curr_idx]-heights[curr_idx + 1]) + rec(heights, curr_idx + 1)
    # Calculate the cost for taking 2 steps
    two_step_cost = abs(heights[curr_idx]-heights[curr_idx + 2]) + rec(heights, curr_idx + 2)

    # Return the minimun of the two costs
    return min(one_step_cost, two_step_cost)
  
  
  
# DP 
def frogJump(n: int, heights: [int]) -> int:
  dp = [0]*n
  dp[0] = 0
  
  for i in range(1, n):
    fs = dp[i-1] + abs(heights[i] - heights[i-1])
    sc = float("inf")
    if i>1:
      sc = dp[i-2] + abs(heights[i] - heights[i-2])

    dp[i] = min(sc,fs)
  return dp[-1]