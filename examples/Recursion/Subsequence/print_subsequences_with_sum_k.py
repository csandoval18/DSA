def printSubsequenceWithSumK(arr: [int], target: int, subsequence: [int], i: int, curr_sum: int):
  n = len(arr)
  if i == n:
    if curr_sum == target:
      print(subsequence)
    return

  # Add
  subsequence.append(arr[i])
  curr_sum += arr[i]
  printSubsequenceWithSumK(arr, target, subsequence, i+1, curr_sum)
  
  # Don't add
  curr_sum -= arr[i]
  subsequence.pop()
  printSubsequenceWithSumK(arr, target, subsequence, i+1, curr_sum)
  
  
def printSubsequenceWithSumK(arr: [int], target: int, subsequence: [int], i: int, curr_sum: int):
  n = len(arr)
  if i == n:
    if curr_sum == target:
      print(subsequence)
    return

  # Add
  subsequence.append(arr[i])
  curr_sum += arr[i]
  printSubsequenceWithSumK(arr, target, subsequence, i+1, curr_sum)

  # Don't add
  curr_sum -= arr[i]
  subsequence.pop()
  printSubsequenceWithSumK(arr, target, subsequence, i+1, curr_sum)
    
  
   