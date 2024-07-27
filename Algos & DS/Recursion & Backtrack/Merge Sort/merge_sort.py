# Merge sort

# [3,1,2,4,5,2,6,4]
# [3,1,2,4] [5,2,6,4]

from typing import List


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
  n, m = len(arr1), len(arr2)
  i, j = 0,0
  res = []
  
  while i < n and j < m:
    if arr1[i] <= arr2[j]:
      res.append(arr1[i])
      i += 1
    else:
      res.append(arr2[j])
      j += 1
  
  while i < n:
    res.append(arr1[i])
    i += 1
    
  while j < m:
    res.append(arr2[j])
    j += 1
  
  return res

def merge_sort(arr: [int]) -> [int]:
  n = len(arr)
  if n == 1:
    print(arr)
    return arr
  
  m = n//2
  l = arr[:m]
  r = arr[m:]
  
  left = merge_sort(l) 
  right = merge_sort(r)
  
  return merge(left, right)

  

arr1 = [2,4]
arr2 = [1,3,5]

# print(merge(arr1, arr2))
print(merge_sort([1,3,1,9,6,5]))

# Same time complexity, but better space complexity of O(n) instead of the O(n log n) using splicing
def merge_sort_pointers(arr: List[int], l: int, r: int):
  if l == r:
    return
  
  m = (l+r)//2
  merge_sort_pointers(arr, l, m)
  merge_sort_pointers(arr, m+1, r)
  merge(arr, l, m, r)