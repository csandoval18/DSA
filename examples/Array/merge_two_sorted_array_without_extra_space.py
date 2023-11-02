# Merge Sorted Arrays without extra space

# LC - 88 Similar to this problem, but with the difference that 
# the two arrays should not be merged into a single array, instead they should be sorted 
# within the two arrays

# Brute Force using extra space
def mergeBF(arr1, arr2, n, m):
  # Declare a 3rd array and 2 pointers:
  arr3 = [0] * (n + m)
  left = 0
  right = 0
  i = 0

  # Insert the elements from the 2 arrays
  # into the 3rd array using left and right
  # pointers:
  while left < n and right < m:
    if arr1[left] <= arr2[right]:
      arr3[i] = arr1[left]
      left += 1
    else:
      arr3[i] = arr2[right]
      right += 1
    i += 1

  # If right pointer reaches the end:
  while left < n:
    arr3[i] = arr1[left]
    left += 1
    i += 1

  # If left pointer reaches the end:
  while right < m:
    arr3[i] = arr2[right]
    right += 1
    i += 1

  # Fill back the elements from arr3[]
  # to arr1[] and arr2[]:
  for i in range(n + m):
    if i < n:
      arr1[i] = arr3[i]
    else:
      arr2[i - n] = arr3[i]
  
  return [arr1, arr2]

arr1 = [1,4,8,10]  
arr2 = [2,3,9]
print(mergeBF(arr1, arr2, 4, 3))


# Optimal 1
def mergeOP(arr1, arr2, n, m):
  # Declare 2 pointers
  left = n-1
  right = 0
  
  # Swap the ee
  while left >= 0 and right < m:
    if arr1[left] > arr2[right]:
      arr1[left], arr2[right] = arr2[right], arr1[left]
      left -= 1
      right += 1
    else:
      break
    
  arr1.sort()
  arr2.sort()
  
# Optimal 2 (Using gap method)
def mergeOP2(arr1, arr2, n, m):
  l = n + m
  # Initial gap
  gap = (l//2) + (l%2)
  
  while gap > 0:
    # Place 2 pointers
    left = 0
    right = left + gap
    
    while right < l:
      # Case 1: left in arr1
      # and right in arr 2
      if left < n and right >= n:
        if arr1[left] > arr2[right-n]:
          arr1[left], arr2[right-n] = arr2[right-n], arr1[left]
      # Case 2: both pointers in arr2
      elif left >= n:
        if arr1[left-n] > arr2[right-n]:
          arr1[left-n], arr2[right-n] = arr2[right-n], arr1[left-n]
      # Case 3: both pointer in arr1
      else: 
        if arr1[left] > arr2[right]:
          arr1[left], arr2[right] = arr2[right], arr1[left]
      left += 1
      right += 1
    
    # Break if iteration gap=1 is completed
    if gap == 1:
      break
    # Else calculate new gap 
    gap = (gap // 2) + (gap % 2)
    
        
      
      
  
  
  