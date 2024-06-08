from typing import List

# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers 
# where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return 
# this repeated number.

# You must solve the problem without modifying the array 
# nums and uses only constant extra space.

# Brute Force

def findDuplicateBF(nums: List[int]) -> int:
  n = len(nums)
  
  for i in range(n):
    for j in range(i+1, n):
      if nums[i] == nums[j]:
        return nums[i]
  
# This can be thought of a cycle detection problem, thus it can be solved
# efficiently using Floyd's Tortoise and Hare (Cycle Detection) algorithm

def findDuplicate(nums: List[int]) -> int:
  # Phase 1: Finding the intersection point of the two runners
  tortoise = nums[0]
  hare = nums[0]
  
  while True:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    
    if tortoise == hare:
      break
    
  # Phase 2: Finding the "entrance" to the cycle
  tortoise = nums[0]
  while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[hare]
    
  return hare


# Tortoise reset: 0
# Tortoise moves: 0 -> 3 -> 4 -> 2 -> 3
# Hare moves:     4 -> 2 -> 3

# Last step
# Indices:    0    1    2    3    4
#             |         |    |    |
# Values:    [3,   1,   3,   4,   2]
#                      T/H
