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
  
  
#TUF using collections counter
from collections import Counter

def majorityElementTUF(nums):
  # Size of the given array
  n = len(nums)
  
  # Count the occurrences of each element using Counter
  # O(n)
  counter = Counter(nums)
  
  # Searching for the majority element
  # O(n)
  for num, count in counter.items():
    if count > n // 3:
      return num
  
  return -1
  

# Optimal Solution TC: O(n) + O(n) SC: O(1)

# Extended Boyer Moore's Voting Algorithm

# 1. Initialize 4 vars:
# cnt1, cnt2: for tracking the counts of elements  
# el1, el2: for sotring the majority of elements 

# 2. Traverse through the given array.
  # 1. If (cnt1 is 0) and (curr element is not el2) then store the current element of the array
  # as el1 along with increasing the cnt1 value by 1.
  # 2. If cnt2 is 0 and the current element is not el1 then store teh current element of the array
  # as el2 along with increasing the cnt2 value by 1.
  # 3. If thecurrent element and el1 are the same increase the cnt1 by 1.
  # 4. If the current element and el2 are the same increase cnt2 by 1.
  # 5. Other than all the above cases: decrease cnt1 and cnt2 by 1.
# 3. The ints present in el1 & el2 should be the result we are expecting. So, using another loop,
# we will manually check their accounts if they are greater than the floor(N/3)  

def majorityElementOP(nums):
  n = len(nums)
  cnt1, cnt2 = 0, 0
  el1, el2 = float('-inf'), float('-inf')
  
  # Extended Boyer Moore's Voting Algorithm:
  for i in range(n):
    if cnt1 == 0 and el2 != nums[i]:
      cnt1 = 1
      el1 = nums[i]
    elif cnt2 == 0 and el1 != nums[i]:
      cnt2 = 1
      el2 = nums[i]
    elif nums[i] == el1:
      cnt1 += 1
    elif nums[i] == el2:
      cnt2 += 1
    else:
      cnt1 -= 1
      cnt2 -= 1
  
  res = []
  
  cnt1, cnt2 = 0, 0
  for i in range(n):
    if nums[i] == el1:
      cnt1 += 1
    if nums[i] == el2:
      cnt2 += 1
  
  mini = int(n/3) + 1
  if cnt1 >= mini:
    res.append(el1)
  if cnt2 >= mini:
    res.append(el2)
  
  return res
  
  
# Return all elements that appear more than ⌊ n/3 ⌋ (floor) | (ceil) = ⌈ x ⌉
# nums = [3,2,3]
nums = [1,2]
# print(majorityElement(majorityElement(nums)))
print(majorityElementBetterOwnImplementaition(nums))