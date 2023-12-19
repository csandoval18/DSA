# Find non repeating number in the given arr

def singleNonDuplicate(arr: [int]) -> int:
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if m%2 == 1:
      m -= 1
    elif arr[m] == arr[m+1]:
      l = m+2
    else:
      r = m-1
  return -1
  
# arr = [1,1,3,5,5]
arr = [1,1,4,4,15]
print(singleNonDuplicate(arr))
  
# L     M     R
# 1 1 2 2 4 5 5
# 0 1 2 3 4 5 6

# 1 2
# 0 1

# if 2 < 2


# 1,1,4,4,15
# L   M   R

