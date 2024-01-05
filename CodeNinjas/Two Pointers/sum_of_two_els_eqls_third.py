def findTriplet(arr: [int], n: int) -> [int]:
  arr.sort()
  
  for i in range(n-1,-1,-1):
    j, k = 0, i-1
    
    while j<k:
      curr_sum = arr[j] + arr[k]
      if curr_sum == arr[i]:
        return [arr[i], arr[j], arr[k]]
      elif curr_sum < arr[i]:
        j += 1
      else:
        k -= 1
  return []


arr = [10,5,5,6,2]
# 10,5,5,6,2
#  j     k i

print(findTriplet(arr, len(arr)))