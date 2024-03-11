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


def lengthOfLISTab(nums: List[int]) -> int:
  n = len(nums)
  # Initialize a 2D dp array with 0s
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
  
  # Iterate over the array in reverse 
  for i in range(n-1, -1, -1):
    for prev_i in range(i-1, -2, -1):
      # Case 1: Do not take the curr element
      notTake = 0 + dp[i+1][prev_i+1]
      
      # Case 2: Take the curr element if it's greater than the element at prev_i
      take = 0
      if prev_i == -1 or nums[prev_i] < nums[i]:
        take = 1 + dp[i+1][i+1]
      
      # Store the maximun of taking or not taking the current element
      dp[i][prev_i+1] = max(notTake, take)
        
  return dp[0][0]
  
  
def lengthOfLISSO(nums: List[int]) -> int:
    n = len(nums)
    nxt = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for ind in range(n-1, -1, -1):
      for prev_index in range(ind - 1, -2, -1):
        notTake = 0 + nxt[prev_index + 1]
        
        take = 0
        if prev_index == -1 or nums[ind] > nums[prev_index]:
          take = 1 + nxt[ind + 1]
            
        curr[prev_index + 1] = max(notTake, take)
      nxt = curr[:]
  
    return curr[0]


def lengthOfLISBest(nums: List[int]) -> int:
  n = len(nums)
  # Initialize dp to all 1's to indicate that the min length of an increasing 
  # subsequence (which includes just nums[i]) is 1
  dp  = [1]*n
  
  for i in range(n):
    for prev in range(i):
      if nums[prev] < nums[i]:
        # If nums[i] can be picked after nums[prev]
        dp[i] = max(dp[i], dp[prev]+1)
        
  print(dp)
  return max(dp)

nums = [10,9,2,5,3,7,101,18]

print(lengthOfLISRec(nums))
print(lengthOfLISRec2(nums))
print(lengthOfLISMemo(nums))
print(lengthOfLISTab(nums))
print(lengthOfLISSO(nums))