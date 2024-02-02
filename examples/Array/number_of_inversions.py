from typing import *
import math

# Inversions = number of pairs of i, j such that i < j and a[i] > a[j]
# A = [5,3,2,1,4]
# (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), and (3,4)

# BF O(n^2)
def numberOfInversionsBF(a: List[int], n) -> int:
  res = 0
  for i in range(n):
    for j in range(i+1, n):
      # a[i], a[j] can be a pair
      if a[i] > a[j]:
        res += 1
  return res
  
  
# Optimal O(n log n)
# Use merge sort, we just need to increment count when a[left > a[right]]
def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # Temporary array
    left = low  # Starting index of left half of arr
    right = mid + 1 # Starting index of right half of arr
    cnt = 0     # Modification 1: cnt variable to count the pairs

    # Storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
      if (arr[left] <= arr[right]):
        temp.append(arr[left])
        left += 1
      else:
        temp.append(arr[right])
        cnt += (mid - left + 1)  # Modification 2 to add the number of elements to the right
        right += 1

    # If elements on the left half are still left
    while (left <= mid):
      temp.append(arr[left])
      left += 1

    # If elements on the right half are still left
    while (right <= high):
      temp.append(arr[right])
      right += 1

    # Transfering all elements from temporary to arr
    for i in range(low, high + 1):
      arr[i] = temp[i - low]

    return cnt   # Modification 3


def mergeSort(arr : List[int], low : int, high : int) -> int:
  cnt = 0
  if low >= high:
    return cnt
  mid = math.floor((low + high) / 2)
  cnt += mergeSort(arr, low, mid)    # left half
  cnt += mergeSort(arr, mid + 1, high)  # right half
  cnt += merge(arr, low, mid, high)  # merging sorted halves
  return cnt


def numberOfInversions(a : List[int], n : int) -> int:
  # Count the number of pairs:
  n = len(a)
  # Count the number of pairs:
  return mergeSort(a, 0, n - 1)
        