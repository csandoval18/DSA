from ast import List

def frogJump(n: int, heights: List[int]) -> int:
  def rec(heights, curr_idx):
    # Base case: if at the last position, no cost to move
    if curr_idx == n-1: 
      return 0
    
    # Base case: if at the second-to-last position, 
    # consider only 1-step move
    if curr
  
  
  
  min_cost = []