from typing import List

def getMinIdx(arr: [int]):
  n = len(arr)
  minVal = float('inf')
  minIdx = 0
  for i in range(n):
    if minIdx < arr[i]:
      minVal = arr[i]
      minIdx = i
  return minIdx

def kWeakestRows(mat: [[int]], k: int) -> [int]:
  n = len(mat)
  m = len(mat[0])
  zeroIdx = []
  res = []

  def binarySearch(nums: [int]) -> int:
    l, r = 0, m-1

    while l <= r:
      mid = (l + r) // 2

      if nums[mid] < 1:
        r = mid-1
      else:
        l = mid+1

    return l

  for i in range(n):
    zeroIdx.append(binarySearch(mat[i]))
  print(zeroIdx)
  
  # Can  consize code with lambda
  # min_index, min_value = min(enumerate(my_list), key=lambda x: x[1])

  return res

# I am returning the position of l not the index of the array as asked


# We start with 1s in the arrays [1,1,0,0] and the left pointer will 
# end at the opposite polarity which is the first 0
# [1,1,0,0] 

# Thought for optimization
# So I noticed that I need to get the mins so it might be not efficient to
# keep the min values in a try instead of having the index values stored in an arr
# This would decrease the time to find the min since there would be no need to traverse the array
  
mat = [
  [1,1,0,0,0],
  [1,1,1,1,0],
  [1,0,0,0,0],
  [1,1,0,0,0],
  [1,1,1,1,1]
]
k = 3

print(kWeakestRows(mat, k))
