# Merge Sort

# Can be used to count inversions in an array
# inversions are: For i & j < size of an array if i < j 
# then you have to find pair (a[i], a[j]) such that a[i] > a[j]

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
  
  

def mergeSort(arr: [int], l: int, r: int):
  # Write Your Code Here
  if l >= r: return
  
  m = (l+r) // 2
  
  mergeSort(arr, l, m)
  mergeSort(arr, m+1, r)
  merge(arr, l, m, r)
    
def merge(arr, l, m, r):
  left_arr = arr[l:m+1]
  right_arr = arr[m+1:r+1]
  j = k = 0
  i = l

  while j < len(left_arr) and k < len(right_arr):
    if left_arr[j] <= right_arr[k]:
      arr[i] = left_arr[j]
      i += 1
    else:
      arr[i] = right_arr[k]
      j += 1
    k += 1

  while j < len(left_arr):
    arr[i] = left_arr[j]
    j += 1
    i += 1

  while k < len(right_arr):
    arr[i] = right_arr[k]
    k += 1
    i += 1

arr = [3,1,2,4,1,5,2,6,4]
mergeSort(arr, 0, len(arr)-1)
print(arr)


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    left_arr = arr[l:m+1]
    right_arr = arr[m+1:r+1]
    i = j = 0
    k = l
    tmp = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            tmp.append(left_arr[i])
            i += 1
        else:
            tmp.append(right_arr[j])
            j += 1
        k += 1

    while i < len(left_arr):
        tmp.append(left_arr[i])
        i += 1
        k += 1

    while j < len(right_arr):
        tmp.append(right_arr[j])
        j += 1
        k += 1

    arr[l:r+1] = tmp
