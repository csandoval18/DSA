from typing import List

# We start with 1s in the arrays [1,1,0,0] and the left pointer will 
# end at the opposite polarity which is the first 0
# [1,1,0,0] 

def getMinIdx(arr: [int]):
  n = len(arr)
  minVal = float('inf')
  minIdx = 0
  for i in range(n):
    if minIdx < arr[i]:
      minVal = arr[i]
      minIdx = i
  arr.remove(minVal)
  return minIdx
  
def bs(nums: [int]) -> int:
  n = len(nums)
  l, r = 0, n-1

  while l <= r:
    mid = (l + r) // 2

    if nums[mid] < 1:
      r = mid-1
    else:
      l = mid+1

  return l

def kWeakestRowsBSAttempt(mat: [[int]], k: int) -> [int]:
  n = len(mat)
  m = len(mat[0])
  startingZeroIdx = []
  res = []

  for i in range(n):
    startingZeroIdx.append(bs(mat[i]))
  print(startingZeroIdx)
  
  # Can  consize code with lambda
  # min_index, min_value = min(enumerate(my_list), key=lambda x: x[1])
  
  # This doesnt work because I need to find the min indexex k times
  # I tried removing the min and then searching again but this doesnt work since the indexes are affected
  # when I remove the min. I need to store the minIndexes from the binary search not the starting index of 0s
  # or I could use a hm to store the starting idx of 0 and the array's index in the matrix
  for i in range(k):
    res.append(getMinIdx(startingZeroIdx))
  

  return res

# I was returning the position of l not the index of the array as asked

# Thought for optimization
# So I noticed that I need to get the mins so it might be not efficient to
# keep the min values in a try instead of having the index values stored in an arr
# This would decrease the time to find the min since there would be no need to traverse the array
  
def binarySearch(row):
  # Binary search to count the number of 1s in a row
  l, r = 0, len(row)
  while l < r:
    mid = (l + r) // 2
    if row[mid] == 1:
      l = mid+1
    else:
      r = mid
  return l

def kWeakestRows(mat, k):
  # Create a list of tuples with row index and the count of 1s in that row
  rows_with_counts = [(i, binarySearch(row)) for i, row in enumerate(mat)]
  
  # Sort the list of tuples based on the count of 1s
  sorted_rows = sorted(rows_with_counts, key=lambda x: x[1])
  
  # Extract the first K row indices from the sorted list
  result = [row[0] for row in sorted_rows[:k]]
  
  return result

# Example usage:
matrix = [
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 1]
]
k = 3
result = kWeakestRows(matrix, k)
print(result)
