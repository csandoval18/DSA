# Merge Sort

# [3,1,2,4,1,5,2,6,4]

#   [3,1,2,4,1]         [5,2,6,4]
#  [3,1,2]  [4,1]     [5,2] [6,4]
# [3,1]  [2]         [5] [2] [6] [4]  
# [1] [3] [2]        

# [1,3] 
# [1,2,3]
# [1,4]
# [1,1,2,3,4]

# Recursive Merge
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  # Divide the array into two halves
  m = len(arr) // 2
  l = arr[:m]
  r = arr[m:]
  
  # Recursively sort both halves
  l = merge_sort(l)
  r = merge_sort(r)
  
  #  Merge the sorted halves
  return merge(l, r)


# Utiliity function to merge 2 arrays in sorted order
def merge(arr1, arr2):
  res = []
  l, r = 0, 0
  
  while l < len(arr1) and right_idx < len(arr2):
    # Append the smaller value to the result array and increase index
    if arr1[l] < arr2[r]:
      res.append(arr1[l])
      l_idx += 1
    else:
      res.append(arr2[])
      right_idx += 1
  
  res.extend(arr1[l:])
  res.extend(arr2[r:])
  