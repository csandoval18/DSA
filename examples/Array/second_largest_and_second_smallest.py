def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
        
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
        
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
            
    return [second_large, second_small]
    
    
    
    
def getSecondOrderElements(n, arr):
  def secondSmallest(arr, n):
    if n < 2:
      return -1
    
    small = float('inf')
    second_small = float('inf')
    
    for i in range(len(arr)):
      if arr[i] < small:
        second_small = small
        small = arr[i]

      # We can just check if arr[i] != small too to update just second_small
      # elif small != arr[i] and arr[i] < second_small:
      elif small < arr[i] and arr[i] < second_small:
        second_small = arr[i]
    
    return second_small

  def secondLargest(arr, n):
    if n < 2:
      return -1
    
    largest = float('-inf')
    largest = float('-inf')
    
    for i in range(len(arr)):
      if largest < arr[i]:
        secondLargest = largest
        largest = arr[i]
      # We can just check if arr[i] != small too to update just second_small
      # elif secondLargest < arr[i] and arr[i] != largest:
      elif secondLargest < arr[i] and arr[i] < largest:
        secondLargest = arr[i]

  return [secondLargest[arr, n], secondSmallest[arr, n]]
        