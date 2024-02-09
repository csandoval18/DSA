from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
  n = len(nums)
  def backtrack(idx: int, ds: List[int], curr_sum: int) -> int:
    if idx == n:
      print(ds)
      if curr_sum == target:
        return 1
      return 0
    
    # add (+)
    ds.append(abs(nums[idx]))
    left = backtrack(idx+1, ds, curr_sum + abs(nums[idx]))
    ds.pop()
    
    # add(-)
    if nums[idx] > 0:
      num = nums[idx] - (nums[idx]*2)
      ds.append(num)
      right = backtrack(idx+1, ds, curr_sum + num)
    else:
      ds.append(nums[idx])
      right = backtrack(idx+1, ds, curr_sum + nums[idx])
    ds.pop()
    
    return left+right
  
  return backtrack(0, [], 0)

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))

def findTargetSumWaysBT(nums: List[int], target: int) -> int:
  def backtrack(idx: int, curr_sum: int) -> int:
    if idx == len(nums):
      if curr_sum == target:
        return 1
      return 0

    left = backtrack(idx+1, curr_sum + nums[idx])
    right = backtrack(idx+1, curr_sum - nums[idx])

    return left + right

  return backtrack(0, 0)

print(findTargetSumWaysBT(nums, target))

# Memoization
def findTargetSumWaysDP(nums: List[int], target: int) -> int:
  dp = {}
  
  def backtrack(idx: int, curr_sum: int) -> int:
    if idx == len(nums):
      if curr_sum == target:
        return 1
      return 0
      
    
    if (idx, curr_sum) in dp:
      return dp[(idx, curr_sum)]
    
    left = backtrack(idx+1, curr_sum + nums[idx])
    right = backtrack(idx+1, curr_sum - nums[idx])
    
    dp[(idx, curr_sum)] = left + right
    return dp[(idx, curr_sum)]
  
  return backtrack(0, 0)

print(findTargetSumWaysDP(nums, target))