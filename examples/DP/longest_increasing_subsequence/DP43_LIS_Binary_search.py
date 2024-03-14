from bisect import bisect_left
from typing import List

# In this method we traverse the array once, and when the subsequence breaks increasing order,
# we use binary search to replace the curr el with the lower bound binary search of that valuee
# This method only works to find the length. The resulting array is not the actual subsequence

def LISBinarySearch(nums: List[int]) -> int:
  # Initialize a temp list to store the increasing subsequence
  n = len(nums)
  tmp = [nums[0]]
  length = 1
  
  for i in range(1, n):
    if tmp[-1] < nums[i]:
      # If nums[i] > the last element of tmp, extend the subsequence
      tmp.append(nums[i])
      length += 1
    else:
      # Use binary search to find the position to replace the element in tmp
      idx = bisect_left(tmp, nums[i], 0, len(tmp))
      tmp[idx] = nums[i]
  return length


import bisect

a = [1, 2, 4, 4, 5]  # Sorted list

# Example 1: Value not present in the list, should be inserted in the middle
value = 3
position = bisect.bisect_left(a, value)
print(position)  # Output: 2

# Example 2: Value matches an existing element, should be inserted before the existing ones
value = 4
position = bisect.bisect_left(a, value)
print(position)  # Output: 2

# Example 3: Value is greater than all elements in the list
value = 6
position = bisect.bisect_left(a, value)
print(position)  # Output: 5

# Example 4: Value is less than all elements in the list
value = 0
position = bisect.bisect_left(a, value)
print(position)  # Output: 0


def LIS_BS(nums: List[int]) -> int:
  n = len(nums)
  tmp = [nums[0]]
  length = 1
  
  for 