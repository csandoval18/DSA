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


nums = [10,9,2,5,3,7,101,18]
print(lengthOfLISRec(nums))