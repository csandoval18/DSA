# Merge Sorted Arrays without extra space

# LC - 88 Similar to this problem, but with the difference that 
# the two arrays should not be merged into a single array, instead they should be sorted 
# within the two arrays

# Brute Force using extra space
def mergeWithExtraSpace(arr1: [int], arr2: [int], n: int, m: int):
  arr3 = [0] * (n+m)
  print(arr3)
  left, right = 0, 0
  i = 0
  print(i)
  print(arr3[i])
  
  while left < n  and right < m:
    if arr1[left] <= arr2[right]:
      arr3[i] = arr1[left]
      left += 1
    else:
      arr3 = arr2[right]
      right += 1
    i += 1 
  
  while left < n:
    arr3[i] = arr1[left] 
    left += 1
    i += 1
    
  while right < m:
    arr3[i] = arr2[right] 
    right += 1
    i += 1
  
  # Update original arrays in sorted order
  for i in range(n+m):
    if i < n:
      arr1[i] = arr3[i]
    else:
      # i-n to cancel out n and only traverse through indexes of m range(0, 2)
      arr2[i-n] = arr3[i]
  
  return [arr1, arr2]
  

arr1 = [1,4,8,10]  
arr2 = [2,3,9]
print(mergeWithExtraSpace(arr1, arr2, 3, 3))
    
  