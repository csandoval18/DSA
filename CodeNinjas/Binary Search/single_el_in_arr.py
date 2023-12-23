# Find non repeating number in the given arr
# Basically the approach to solve this with binary search is to
# use the indexes and check if they are even or not at arr[m]
# Since every el number but the target is repeating they should occur 
# twice in an even index and in uneven index

def singleNonDuplicate(arr: [int]) -> int:
  n = len(arr)
  l, r = 0, n-1
  
  while l<r:
    m = (l+r)//2
    
    # If m is uneven move m back 1 to even index
    if m%2 == 1:
      m -= 1
    # Now we are in an even idx position that would be the start of 
    # a couple of repeating num els
    # 1 1 2 2 3 3
    # 0 1 2 3 4 5
    # Notice how new numbers begin in even indexes
    # Since we are checking the element in front we can skip both
    # when moving the left pointer so l = m+2
    elif arr[m] == arr[m+1]:
      l = m+2
    else:
      r = m-1
  return arr[l]
  
arr = [1,1,3,5,5]
# arr = [1,1,4,4,15]
print(singleNonDuplicate(arr))
  
# L     M     R
# 1 1 2 2 4 5 5
# 0 1 2 3 4 5 6

# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6

# L     M     R
# 1 1 2 2 4 5 5
# 0 1 2 3 4 5 6

# L   M       R
# 1 1 2 2 4 5 5
# 0 1 2 3 4 5 6

# L   M       R
# 1 1 2 2 4 5 5
# a[m] == a[m+1] | 2 == 2: True


# -----------------------------------------------

# L   M   R
# 1,1,4,4,15
# 0 1 2 3 4 

def singleNonDuplicate1(arr):
  l, r = 0, len(arr)-1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] == arr[m+1]:
      # if m is an even num move left pointer
      if m%2 == 0:
        l = m+1
      else:
        r = m-1
    else:
      r = m
  return arr[l]
        
        

def getSingleElement(arr : List[int]) -> int:
  l, r = 0, len(arr)-1

  while l<r:
    m = l + (r - l) // 2

    # Check if the single element is on the left or right
    if m % 2 == 1:
      m -= 1

    # Adjust the search space based on whether the single element is on the left or right
    if arr[m] == arr[m+1]:
      l = m+2
    else:
      r = m

  return arr[l]
  