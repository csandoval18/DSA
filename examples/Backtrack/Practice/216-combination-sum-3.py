from typing import List

def combinationSum3(k: int, n: int) -> List[List[int]]:
  def backtrack(idx: int, curr_sum: int, ds: List[int]) -> None:
    if len(ds) > k:
      return
      
    if curr_sum == n:
      res.append(ds[:])
      print(ds)
      return
      
    ds.append(idx+1)
    curr_sum += idx+1
    backtrack(idx+1, curr_sum, ds)
    ds.pop()
    curr_sum -= idx+1
    backtrack(idx+1, curr_sum, ds)
    
  res = []
  backtrack(0, 0, [])    
  return res
  
  # nums = 1->9
  # each num used at most once

k = 3
n = 7
print(combinationSum3(k, n))