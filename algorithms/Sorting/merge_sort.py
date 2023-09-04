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

def merge(left, right):
  res = []
  left_idx, right_idx = 0, 0
  
  while left_idx < len(left) and right_idx < len(right):
    # Append the smaller value to the result array and increase index
    if left[left_idx] < right[right_idx]:
      res.append(left[left_idx])
      l_idx += 1
    else:
      res.append(right[right_idx])
      right_idx += 1
  
  res.extend(left[left_idx:])
  res.extend(right[right:])
  