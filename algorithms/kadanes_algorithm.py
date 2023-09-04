# Kadane's algorithm is a widely used dynamic programming technique 
# for solving the maximum subarray sum problem. It efficiently finds 
# the maximum sum of a contiguous subarray within a given array. '
# The algorithm has a time complexity of O(n), 
# making it one of the most optimal solutions for this problem.

# 1. Initialize two variables: maxEndingHere and maxSoFar, both initially set to the first element of the array.

# 2. Iterate through the array starting from the second element:
  # a. Update maxEndingHere to the maximum of the current element and the sum of the current element and maxEndingHere.
  # b. Update maxSoFar to the maximum of maxSoFar and maxEndingHere.
  
# 3. After iterating through the entire array, maxSoFar will hold the maximum subarray sum.

def max_subarray_sum_kadane(arr):
  maxEndingHere = maxSoFar = arr[0]
  
  for i in range(1, len(arr)):
    maxEndingHere = max(arr[i], maxEndingHere + arr[i])
    maxSoFar = max(maxSoFar, maxEndingHere)
    
  return maxSoFar

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum_kadane(arr))  
# Output should be 6 (subarray [4, -1, 2, 1])