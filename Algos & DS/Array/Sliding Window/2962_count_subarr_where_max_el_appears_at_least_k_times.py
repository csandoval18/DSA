from collections import defaultdict
from typing import List

def countSubarraysAttempt(nums: List[int], k: int) -> int:
  n = len(nums)
  cnt = l = 0
  max_num = max(nums)
  hm = defaultdict(int)
  
  for r in range(n):
    hm[nums[r]] += 1
    
    if hm[max_num] >= k:
      cnt += 1
    
    while l < r and hm[max_num] < k:
      hm[nums[l]] -= 1
      l += 1
  
  return cnt
  

# Does not work chatgpt
def countSubarrays2(nums: List[int], k: int) -> int:
  def valid_window(hm: defaultdict) -> bool:
    for count in hm.values():
      if count >= k:
        return True
    return False
    
  n = len(nums)
  l = total = 0
  hm = defaultdict(int)
  
  for r in range(n):
    hm[nums[r]] += 1
    
    while not valid_window(hm) and l <= r:
      hm[nums[l]] -= 1
      l += 1
      
    if valid_window(hm):
      total += l+1
  return total


def countSubarrays(nums: List[int], k: int) -> int:
  n = len(nums)
  max_num = max(nums)
  res = l = curr_max_cnt = 0 
  
  for r in range(n):
    if nums[r] == max_num:
      curr_max_cnt += 1
    
    while curr_max_cnt == k:
      if nums[l] == max_num:
        curr_max_cnt -= 1
      l += 1
    res += l
    
  return res
      
      
nums = [1,3,2,3,3] 
k = 2
print(countSubarrays(nums, k))