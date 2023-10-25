def majorityElementBF(nums):
  n = len(nums)
  res = []
  
  for i in range(n):
    # Selected element is nums[i]
    # Checking if res is empty or if current element val is already 
    # in the res array
    if len(res) == 0 or res[0] != nums[i]:
      cnt = 0
      for j in range(n):
        # Counting frequency of nums[i]
        if nums[j] == nums[i]:
          cnt += 1
      # Check if frequency is greater than n/3
      if cnt > n//3:
        res.append(nums[i])
    if len(res) == 2:
      break
  return res
  
#TUF using collections counter
from collections import Counter

def majorityElementTUF(nums):
  # Size of the given array
  n = len(nums)
  
  # Count the occurrences of each element using Counter
  counter = Counter(nums)
  # Searching for the majority element
  for num, count in counter.items():
    if count > n // 3:
      return num
  
  return -1
  
  
# O(n+m)
def majorityElementBetterOwnImplementaition(nums):
  n = len(nums)
  hm = {}
  res = []
  
  # O(n)
  for num in nums:
    hm[num] = hm.get(num, 0) + 1
  
  # O(m) where 'm' = # of unique values
  for key, count in hm.items():
    if count > n // 3:
      res.append(key)
    
    if len(res) == 2:
      break
    
  return res
  
# Return all elements that appear more than ⌊ n/3 ⌋ (floor) | (ceil) = ⌈ x ⌉
# nums = [3,2,3]
nums = [1,2]
# print(majorityElement(majorityElement(nums)))
print(majorityElementBetterOwnImplementaition(nums))

def majorityElementOP(nums):
  
  return 0