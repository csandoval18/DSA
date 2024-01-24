def printSubsequenceWithSumK(arr: [int], target: int, subsequence: [int], i: int, curr_sum: int):
  n = len(arr)
  if i == n:
    if curr_sum == target:
      print(subsequence)

  subsequence.add(arr[i])
  printSubsequenceWithSumK(arr, target, subsequence, i+1, curr_sum+arr[i])