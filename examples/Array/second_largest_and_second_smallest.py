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
      elif secondLargest < arr[i] and arr[i] < largest:
        secondLargest = arr[i]

  return [secondLargest[arr, n], secondSmallest[arr, n]]
        