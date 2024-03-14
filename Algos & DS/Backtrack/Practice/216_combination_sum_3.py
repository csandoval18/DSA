from typing import List

def combinationSum3(k: int, n: int) -> List[List[int]]:
  def backtrack(idx: int, curr_sum: int, ds: List[int]) -> None:
    if idx > 9 or len(ds) > k or curr_sum > n:
      return
      
    if len(ds) == k and curr_sum == n:
      res.append(ds[:])
      return
      
    num = idx+1
    ds.append(num)
    backtrack(idx+1, curr_sum+num, ds)
    ds.pop()
    backtrack(idx+1, curr_sum, ds)
    
  res = []
  backtrack(0, 0, [])    
  return res
  
  # nums = 1->9
  # each num used at most once

k = 3
n = 7
print(combinationSum3(k, n))

  #                        (pick 1) /   |   \ (not pick 1)
  #                              [1]   [2]   [3] ... [9]
  #                           /       / | \   \
  #                       (pick 2)   ...  ...  (not pick 2)
  #                          /   \               /  \
  #                       [1,2]  ...         [1,4]  ...
  #                        /  \               /   \
  #                   (pick 3)  ...    (not pick 3) ...
  #                      /  \                     /  \
  #                   [1,2,3] ...          [1,4,5]  ...
  #                   / |  | \
  #               (pick 4) ... ...
  #                /  |  |  \
  #           [1,2,3,4] ... ...
  #           /   |   |   \
  #       (pick 5) ... ...
  #        /  |  |  \
  #  [1,2,3,4,5] ... ...
