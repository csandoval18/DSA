from typing import List

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
# and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space

def findDuplicates(nums: List[int]) -> List[int]:
  print(nums)
  print()
  duplicates = []
  for num in nums:
    # Find the index this number should mark
    index = abs(num) - 1
    print("index:", f"abs({num})-1 =", index)
    
    # If the value at this index is negative, it means we've seen this number before
    if nums[index] < 0:
      duplicates.append(abs(num))
    else:
      # Mark this number as seen by negating the value at its corresponding index
      nums[index] = -nums[index]
    
    print(nums)
    print()

  return duplicates

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
# out: [2,3]


# Why abs(num)?
# The use of abs(num) ensures that the algorithm correctly accesses the index 
# regardless of whether the number at that index has already been negated (marked 
# as seen). This is crucial because, after marking a number as seen by negating it, we 
# still need a reliable way to refer back to that number's original value, which is what 
# the abs function allows.


# PS: This algorithm is very confusing, but basically it uses a mapping technique for the index (|num|-1).
# In the initial iteration when we mark 7 as negative we are not marking the actual 7 as 'seen', 
# we are marking the starting 4 as 'seen'

# Example:

# Iteration 1: num = 4
# Calculate i = abs(4) - 1 = 3. The abs function ensures we always get a positive index.
# nums[3] is 7, a positive number. We haven't seen the number 4 before, so we mark its presence
# by making nums[3] negative: nums[3] = -7.