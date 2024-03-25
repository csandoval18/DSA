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
    print("index:", f"{num}-1 =", index)
    
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

