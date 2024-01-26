def finSolution(arr: [int], target: int):
  def findCombination(idx: int, target: int, arr: [int], res, subsequence):
    if idx == len(arr):
      if target == 0:
        res.append(subsequence)
      return
    
    # Pick up the element
    if arr[idx] <= target:
      # Add curr num 
      subsequence.append(arr[idx])
      # Recursive call with same index but updated target to recheck if a same number use would work
      findCombination(idx, target-arr[idx], arr, res, subsequence)
      subsequence.pop()
      
    # Dont pick up the element and move on to the next num
    findCombination(idx+1, target, arr, res, subsequence)
    
  res = []
  subsequence = []
  findCombination(0, target, arr, res, subsequence)
  return res
  
    
  