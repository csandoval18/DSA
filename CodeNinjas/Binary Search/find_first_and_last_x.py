# Find first and last position of element in sorted arr

# [1,2,4,4,5]
# x = 4
# Out: 2 3


def searchRangeFirst(arr: [int], x: int) -> [int]:
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] < x:
      l = m+1
    else:
      r = m-1
  return l

# Output: 2
# Notice how it find 4 then goes to the next index kind of like going 
# to the next polarity. This function can be used to get the last occurence
# by substracting 1

def searchRangeLast(arr: [int], x: int) -> [int]:
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] <= x:
      l = m+1
    else:
      r = m-1
  return l-1
  
# Output: 4
# Notice how it find 4 then goes to the next index kind of like going 
# to the next polarity. This function can be used to get the last occurence
# by substracting 1

nums = [1,2,4,4,5]
x = 4
print(searchRangeLast(nums, x))