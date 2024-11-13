from typing import List

'''
You are given an integer array nums of length n.
Assume arr(k) to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
'''

class Solution:
  def maxRotateFunction(self, nums: List[int]) -> int:
    n = len(nums)
    total_sum = sum(nums)
    F0 = sum(i * nums[i] for i in range(n))
    
    # Recursive helper function to computer F(k)
    def helper(F_prev: int, k: int) -> int:
      if k == n: # Base case, stop after n rotations
        return F_prev
      
      # Calculate F(k) based on F(k-1)
      F_k = F_prev + total_sum - n * nums[n - k]
      return max(F_k, helper(F_k, k+1)) # Recur and take max
    # Start recursion from F(1) using F(0) as F_prev
    return helper(F0, 1)
    
      

class Solution:
  def maxRotateFunction(self, nums: List[int]) -> int:
    n = len(nums)
    total_sum = sum(nums)
    
    for i in range(n):
      F0 = sum(i * nums[i])
    
    # Recursive function to calculate F(k)
    def helper(k: int, F_prev: int) -> int:
      if k == n:
        return F_prev # Stop recursion after n steps
        
      # Here we remove the last element's contribution because we multiply it by 0,
      # and add the first element's contribution since it is no longer multiplied by 0
      F_k = F_prev + total_sum - n * nums[n - k]
      return max(F_k, helper(k+1, F_k)) # Recurse and take max
    
    # Start recursion from F(1) based on F(0)
    return helper(1, F0)
    
'''
PS:
In this problem, memoization does not fit well because each rotation function
F(k) depends on F(k-1) in a specific, sequential way, and we need to examine
all computed values to find the maximum. This is a scenario where a simple loop-
based approach works better than recursion and memoization.
'''
      
class Solution:
  def maxRotateFunction(self, nums: List[int]) -> int:
    n = len(nums)
    total_sum = sum(nums)
    
    # Initial calculation of F(0)
    F0 = sum(i * nums[i] for i in range(n))
    
    # Use F0 as the initial max value
    max_value = F0
    F_prev = F0
    
    # Iterate to compute each F(k) and track the maximum
    for k in range(1, n):
      # Calculate F(k) based on F(k-1)
      F_k = F_prev + total_sum - n * nums[n - k]
      max_value = max(max_value, F_k)
      F_prev = F_k  # Update F_prev for the next iteration
    
    return max_value

nums = [4,3,2,6]
n = len(nums)
# print(nums[n-k:] + nums[:n-k]) # Rotates array clockwise ie. last element comes to the front

# Output: 26
# Explanation:
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.