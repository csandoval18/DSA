from typing import List

def lengthOfLISRec(nums: List[int]) -> int:
  def f(i: int, prev_i: int) -> int:
    # Base case when index of nums array is exhausted, we return 0 since
    # the length can no longer increase
    if i == n:
      return 0
    
    length = 0 + f(i+1, prev_i) # Not take
    
    if prev_i == -1 or nums[prev_i] < nums[i]: # Take
      length = max(length, 1 + f(i+1, i))
    
    return length
      
  n = len(nums)
  return f(0, -1)
  
def lengthOfLISRec2(nums: List[int]) -> int:
  def f(i: int, prev_i: int) -> int:
    if i == n:
      return 0
    
    notTake = 0 + f(i+1, prev_i)
    
    take = 0
    if prev_i == -1 or nums[prev_i] < nums[i]:
      # Increment length by 1, increment index, and update prev index to current index
      take = 1 + f(i+1, i)
    
    return max(take, notTake)
  
  n = len(nums)
  return f(0, -1)
    
  
# prev_i ranges from -1 (no prev) to n-1. When memoizing this solution, the problem arises that -1 is not indexable
# in a dp table since indexing starts from 0. To solve this problem, a coordinate shift is necessary to allow for the prev_i  indexing
def lengthOfLISMemo(nums: List[int]) -> int:
  def f(i: int, prev_i: int, dp: List[List[int]]) -> int:
    # Base case
    if i == n:
      return 0
    
    if dp[i][prev_i+1] != -1: 
      return dp[i][prev_i+1]
      
    notTake = 0 + f(i+1, prev_i, dp)
    
    take = 0
    if prev_i == -1 or nums[prev_i] < nums[i]:
      take = 1 + f(i+1, i, dp)
    
    dp[i][prev_i+1] = max(notTake, take)
    return dp[i][prev_i+1]
  

  n = len(nums)
  dp = [[-1 for _ in range(n+1)] for _ in range(n)]
  return f(0, -1, dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLISRec(nums))
print(lengthOfLISRec2(nums))
print(lengthOfLISMemo(nums))