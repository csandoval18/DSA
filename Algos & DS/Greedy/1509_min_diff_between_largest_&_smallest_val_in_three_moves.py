def minDifference(nums):
  n = len(nums)
  if n <= 4:
    return 0
  
  nums.sort()
  
  # Consider the different scenarios
  return min(nums[n-1] - nums[3],     # Remove 3 smallest
             nums[n-2] - nums[2],     # Remove 2 smallest and 1 largest
             nums[n-3] - nums[1],     # Remove 1 smallest and 2 largest
             nums[n-4] - nums[0])     # Remove 3 largest

# Example usage
nums = [6, 6, 0, 1, 1, 4, 6]
print(minDifference(nums))  # Output: 2

# 1. Understanding the Problem:
# You are given an array of integers.
# You can remove up to three elements from the array.
# The goal is to minimize the difference between the largest and smallest values of the remaining elements.

# 2. Key Observations:
# - If the array length is less than or equal to 4,you can remove all elements except one,
#   resulting in a difference of 0.
# - If the array is larger, removing up to three elements can be thought of as removing the 
#   largest elements, the smallest elements, or a combination of both to minimize the difference.

# 3. Strategy:
# Sort the array to facilitate the identification of the largest and smallest elements.
# Consider the following scenarios:
# - Remove the three largest elements.
# - Remove the three smallest elements.
# - Remove two largest and one smallest elements.
# - Remove two smallest and one largest elements.
# - Remove one largest and two smallest elements.

Steps to Solve
Sort the Array: [0, 1, 5, 10, 14].

Calculate the Differences for the four scenarios:

Remove the three largest elements: Difference between 0 and 1 (remaining elements: [0, 1]).
Remove the three smallest elements: Difference between 10 and 14 (remaining elements: [10, 14]).
Remove two largest and one smallest elements: Difference between 1 and 10 (remaining elements: [1, 5, 10]).
Remove two smallest and one largest element: Difference between 5 and 14 (remaining elements: [5, 10, 14]).