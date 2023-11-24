# You are given an array 'arr'sorted in non-decreasing order and a number 'x'.
# You must return the index of lower bound of 'x'.
# Note:
# For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'
# If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.
# Consider 0-based indexing.

# Example:
# Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0
# Output: 0
# Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.


# Basically this is a binary search problem since its asking for O(log(n)), but the array has repeating numbers

def lowerBound(arr: [int], n: int, x: int) -> int:
  l = 0
  r = n-1
  res = n
  
  while l<=r:
    m = (l+r) // 2
    print(m)
    
    if arr[m] >= x:
      res = m
      r = m-1
    elif arr[m] <= x:
      l = m+1 
  return res
       
arr = [1,2,2,3,3,5]
n = 6
x = 2

print(lowerBound(arr, n, 7))
