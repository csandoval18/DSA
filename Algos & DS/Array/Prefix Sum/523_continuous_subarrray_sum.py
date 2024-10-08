from typing import List

# Given an integer array nums and an integer k, return true if nums has a good subarray or
# false otherwise.

# A good subarray is a subarray where:
# * its length is at least two, and
# * the sum of the elements of the subarray is a multiple of k.

# Note that:
# * A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is
# always a multiple of k.

def checkSubarraySum(nums: List[int], k: int) -> bool:
  #                     sum
  prefix_sum_remainder = {0: -1}
  curr_sum = 0
  
  for i, num in enumerate(nums):
    curr_sum += num
    
    if k != 0:
      curr_sum %= k
      
    if curr_sum in prefix_sum_remainder:
      if i - prefix_sum_remainder[curr_sum] > 1:
        return True
    else:
      prefix_sum_remainder[curr_sum] = i
      
  return False

#       0  1 2 3 4
nums = [23,2,4,6,7]
k = 6
# Output: true

nums = [23,2,6,4,7]
k = 6
# Output: true

nums = [23,2,6,4,7]
k = 13
# Output: false

# Compute Prefix Sums:
# Prefix sum 0: 23 => 23
# Prefix sum 1: 23+2 = 25
# Prefix sum 2: 23+2+4 = 29
# Prefix sum 3: 23+2+4+6 = 35 
# Prefix sum 4: 23+2+4+6+7 = 42

# Compute Remainders:
# i = 0
# 23 % 6 = 5
# i = 1
# 25 % 6 = 1
# i = 2
# 29 % 6 = 5
# i = 3
# 29 % 6 = 5
# i = 4
# 35 % 6 = 5
# i = 5
# 42 % 6 = 0 

# Find Matching Remainders:
# Notice that the remainder 5 repeats. The prefix sums at indices 0 and 2 have the same remainder 5.
# This means the sum of the subarray from index 1 to 2 (elements [2, 4]) is a multiple of 𝑘
# k: Sum from index 1 to 2: 2 + 4 = 6, which is a multiple of 6.

# Remember that there is a cyclic nature to modulo