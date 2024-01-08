from ast import List

def frogJump(n: int, heights: List[int]) -> int:
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
  
  
def frogJump(n: int, heights: [int]) -> int:
  dp=[0]*n
  dp[0]=0
  for i in range(1,len(heights)):
    fs=dp[i-1]+abs(heights[i]-heights[i-1])
    sc=float("inf")
    if i>1:
      sc=dp[i-2]+abs(heights[i]-heights[i-2])

    dp[i]=min(sc,fs)
  return dp[-1]