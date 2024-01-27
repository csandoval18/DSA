from typing import List

# This breaks with repeating numbers
def subset_sum_cnt(arr: List[int], target: int, idx: int, curr_sum: int) -> int:
  n = len(arr)
  if idx == n:
    if target == curr_sum:
      return 1
    return 0
  
  curr_sum += arr[idx]
  left = subset_sum_cnt(arr, target, idx+1, curr_sum)
  curr_sum -= arr[idx]
  right = subset_sum_cnt(arr, target, idx+1, curr_sum)
  
  return left + right
    
# arr = [3,1,2,4]
# k = 4
# print(subset_sum_cnt(arr, k, 0, 0))


# number of subsets => 2^n = 2^3 => 8 
# res = [6,4,5,3,3,1,2,0]
def subset_sum(arr: List[int], res: List[int], idx: int, curr_sum: int)-> None:
  n = len(arr)
  if idx == n:
    res.append(curr_sum)
    return
  
  curr_sum += arr[idx]
  subset_sum(arr, res, idx+1, curr_sum)
  curr_sum -= arr[idx]
  subset_sum(arr, res, idx+1, curr_sum)
  
arr = [3,1,2]
res = []
subset_sum(arr, res, 0, 0)
print(res)