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



# def merge_sort(arr):
#   if len(arr) <= 1:
#     return arr
  
#   # Divide the array into two halves
#   m = len(arr) // 2
#   l = arr[:m]
#   r = arr[m:]
  
#   # Recursively sort both halves
#   l = merge_sort(l)
#   r = merge_sort(r)
  
#   #  Merge the sorted halves
#   return merge(l, r)

# def merge(left, right):
#   res = []
#   left_idx, right_idx = 0, 0
  
#   while left_idx < len(left) and right_idx < len(right):
#     # Append the smaller value to the result array and increase index
#     if left[left_idx] < right[right_idx]:
#       res.append(left[left_idx])
#       l_idx += 1
#     else:
#       res.append(right[right_idx])
#       right_idx += 1
  
#   res.extend(left[left_idx:])
#   res.extend(right[right:])
  

def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if l >= r: return
    
    m = (l+r) // 2
    
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

    
def merge(arr, left, mid, right):
  tmp = []
  p1 = 0
  p2 = mid+1
  # start at index 0 and m+1 since that would be the start of the split right array
  # arr = [3,1,2,4,1,5,2,6,4]
  #        l       m r
  
  while p1 <= mid and p2 <= right:
    if arr[p1] < arr[p2]:
      tmp.append(arr[p1])
      p1 += 1
    else:
      tmp.append(arr[p2])
      p2 += 1
  
  while p1 < len(arr):
    tmp.append(arr[p1])
    p1 += 1

  while p2 <  len(arr):
    tmp.append(arr[p2])
    p2 += 1
  
  for i in range(left, right):
    arr[i] = [i - left]
  
arr = [3,1,2,4,1,5,2,6,4]
print(mergeSort(arr, 0, len(arr)-1))
