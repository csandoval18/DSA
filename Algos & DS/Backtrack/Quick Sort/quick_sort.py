import random


def quick_sort(arr: [int]) -> [int]:
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
  
def quickSort(arr: [int]) -> [int]:
  if len(arr) <= 1:
    return arr
  
  pivot_idx = random.randint(0, len(arr)-1)
  pivot = arr[pivot_idx]
  
  lesser = []
  greater = []
  
  for i, element in enumerate(arr):
    if i == pivot_idx:
      continue
    if element <= pivot:
      lesser.append(element)
    else:
      greater.append(element)
      
  return quickSort(lesser) + [pivot] + quickSort(greater)



def quicksort(arr: [int], left, right):
  if left < right:
    # Partition the array and get the pivot index
    pivot_idx = partition(arr, left, right)
    
    # Recursively sort the sub-arrays
    quicksort(arr, left, pivot_idx)
    quicksort(arr, pivot_idx+1, right)
  
  def partition(arr: [int], left: int, right: int):
    # Choose a random pivot
    pivot_idx = random.randint(left, right-1)
    pivot = arr[pivot_idx]
    
    # Swap the pivot to the end
    arr[pivot_idx], arr[right-1] = arr[right-1], arr[pivot_idx]
    
    # Initialize pointers
    i = left-1 # i points to the last element less than or equal to the pivot
    
    # Iterate through the array to rearrange elements
    for j in range(left, right-1):
      if arr[j] <= pivot:
        # Swap elements to maintain the partition
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot back to its correct position
    arr[i+1], arr[right-1] = arr[right-1], arr[i+1]
    # Return the pivot index
    return i+1