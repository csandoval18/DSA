# 0 = red, 1 = white, 2 = blue

# Brute force: 
# Use sorting alrogrithm = O(n log n)


# Better approach:
# O(2n)
# Get 0s, 1s, and 2s counts from first n loop,
# then edit original array with counts

# Remember to add counts ranges when updating og arr, for example
#  0 1 2 3 4 5
# [0,0,1,1,2,2]
#   l0| l1| l2| 


def sortColors(nums):
  count0 = 0
  count1 = 0
  count2 = 0
  
  for num in nums:
    if num == 0:
      count0 += 1
    if num == 1:
      count1 += 1
    if num == 2:
      count2 += 1
  
  i = 0
  while i < count0:
    nums[i] = 0
    i += 1
    
  while i < count0 + count1:
    nums[i] = 1
    i += 1
  
  while i < count0 + count1 + count2:
    nums[i] = 2
    i += 1
  
  return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))


# Optimal Solution:
# O(n) 
# 0   low-1 low   mid-1 mid             high high+1    n-1
# |       | |         | |                  | |           |
# 0 0 0 0 0 1 1 1 1 1 1 0s/1s/2s (unordered) 2 2 2 2 2 2 2


def sort_colors(nums: [int]) -> [int]: 
  low = 0
  mid = 0
  high = len(nums)-1
  
  while mid <= high:
    if mid == 0:
      # swap mid to low
      low, mid = mid, low
      
      