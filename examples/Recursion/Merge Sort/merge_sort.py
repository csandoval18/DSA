# Merge sort

# [3,1,2,4,5,2,6,4]
# [3,1,2,4] [5,2,6,4]

def merge_sortArr(arr: [int]) -> [int]:
  def merge(arr1: [int], arr2: [int]) -> [int]:
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
      return arr
    
    m = n//2
    l = arr[:m]
    r = arr[m:]
    
    left = merge_sort(l) 
    right = merge_sort(r)
    
    return merge(left, right)

  return merge_sort(arr)
  

arr1 = [2,4]
arr2 = [1,3,5]

# print(merge(arr1, arr2))
print(merge_sortArr([1,3,1,9,6,5]))