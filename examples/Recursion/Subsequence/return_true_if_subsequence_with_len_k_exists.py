# k = target

def subsequenceWithSumKExists(arr: [int], target: int, subsequence: [int], idx: int, curr_sum: int) -> bool:
  n = len(arr)
  if idx == n:
    if curr_sum == target:
      print(subsequence)
      return True
  else: 
    return False
  
  subsequence.append(arr[idx])
  curr_sum += arr[idx]
  if subsequenceWithSumKExists(arr, target, subsequence, idx+1, curr_sum) == True:
    return True
  
  subsequence.pop()
  curr_sum -= arr[idx]
  if subsequenceWithSumKExists(arr, target, subsequence, idx+1, curr_sum) == True:
    return True
  
  return False