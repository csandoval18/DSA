# k = target

def findSubsequenceCountsWithSumK(arr: [int], target: int, idx: int, subsequence: [int], curr_sum):
  # if curr_sum > target: # Only works on all positive subsequences
  #   return 0
  n = len(arr)
  if idx == n:
    if curr_sum == target:
      print(subsequence)
      return 1
  else: return 0
  
  subsequence.append(arr[idx])
  curr_sum += arr[idx]
  l = findSubsequenceCountsWithSumK(arr, target, idx+1, subsequence, curr_sum)
  subsequence.pop()
  curr_sum -= arr[idx]
  r = findSubsequenceCountsWithSumK(arr, target, idx+1, subsequence, curr_sum)
  
  return l+r
  

def findSubsequenceCountsWithSumK(arr: [int], target: int, idx: int, curr_sum):
  n = len(arr)
  if idx == n:
    if curr_sum == target:
      return 1
  else: return 0
  
  curr_sum += arr[idx]
  l = findSubsequenceCountsWithSumK(arr, target, idx+1, curr_sum)
  curr_sum -= arr[idx]
  r = findSubsequenceCountsWithSumK(arr, target, idx+1, curr_sum)
  
  return l+r
