from typing import List

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Solution with linear time TC and constant SC
# TC: O(N) | SC: O(1)
def firstMissingPositive(nums: List[int]) -> int:
  n = len(nums)
  
  # Mark non-positive integers as 0
  for i in range(n):
    if nums[i] <= 0:
      nums[i] = 0
      
  # Mark out-of-range integers as 0
  for i in range(n):
    if nums[i] > n:
      nums[i] = 0
  
  # Place each positive integer at its index
  for i in range(n):
    while nums[i] != 0 and nums[i] != i+1: # While the curr number is not 0 and not at its index position (i+1)
      num = nums[i] # Store the curr number value
      if nums[num-1] == num: # This basically checks if the curr number is that its index position (i+1) or (num-1)
        break
      # Swap current number and its "sorted" position in num-1
      nums[i], nums[num-1] = nums[nums-1], nums[i] 
  
  # Find the first missing positive integer
  for i in range(n):
    if nums[i] != i+1:
      return i+1
    
  return n+1


def firstMissingPositive2(nums: List[int]) -> int:
  n = len(nums)
  
  for i in range(n):
    if nums[i] <= 0 or nums[i] > n:
      nums[i] = 0
  
  for i in range(n):
    while nums[i] != 0 and nums[i] != i+1:
      num = nums[i]
      if nums[num-1] == num:
        break
      nums[i], nums[num-1] = nums[num-1], num[i]

  for i in range(n):   
    if nums[i] != i+1:
      return i+1
      
  return n+1
    
    
def firstMissingPositiveHM(nums: List[int]) -> int:
  # Create a set to store the presence of positive ints
  st = set(nums)
  
  # Start with the first positive integer
  i = 1
  
  # Iterate until we find the smallest missing positive int
  while i in st:
    i += 1
  
  return i