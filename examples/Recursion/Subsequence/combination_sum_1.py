# 39. Combination Sum

# Remember that in python lists are mutable, so when you append them to another array you are 
# also appending their reference, so you need to make a copy of the current state of the array
# otherwise the appended data will mutate along with the passed array when it is modified

def finSolution(arr: [int], target: int):
  def findCombination(idx: int, target: int, arr: [int], res: [int], subsequence: [int]):
    if idx == len(arr):
      if target == 0:
        res.append(subsequence.copy())
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
  
    
  
def combinationSum(candidates: [int], target: int):
  def findCombination(candidates: [int], target: int, idx: int, subsequence: [int], res: [[int]]) -> [[int]]:
    n = len(candidates)
    if n == idx:
      if target == 0:
        res.append(subsequence.copy())
      return
    
    if candidates[idx] <= target:
      subsequence.append(candidates[idx])
      findCombination(candidates, target-candidates[idx], idx, subsequence, res)
      subsequence.pop()
    
    findCombination(candidates, target, idx+1, subsequence, res)
  
  res = []
  subsequence = []
  findCombination(candidates, target, 0, subsequence, res)
  return res

arr = [2,3,6,7]
target = 7
print(combinationSum(arr, target))
  