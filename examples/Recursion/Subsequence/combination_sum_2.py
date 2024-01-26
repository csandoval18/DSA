from typing import List

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
  def findCombinations(candidates: List[int], target: int, idx: int, res: List[List[int]], subsequence: List[int]):
    n = len(candidates)
    if target == 0:
      res.append(subsequence.copy())
      return

    for i in range(idx, n):
      # i > idx = not the first element &&
      # Avoid picking up duplicate combinations
      if i > idx and candidates[i] == candidates[i-1]:
        continue
      
      # this checks if the current num is greater than target. If it is then we can't find a number to 
      # get target to 0. Since the array is sorted we know every number to the right will also not work
      # so we can break
      if candidates[i] > target: 
        break

      subsequence.append(candidates[i])
      findCombinations(candidates, target - candidates[i], i+1, res, subsequence.copy())
      subsequence.pop()

    res = []
    subsequence = []
    candidates.sort()
    findCombinations(candidates, target, 0, res, subsequence)
    return res

candidates = [1,1,2,3,4]
candidates.sort()
target = 4
print(combinationSum2(candidates, target))


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
  def findCombinations(candidates: List[int], target: int, idx: int, res: List[List[int]], subsequence: List[int]):
    n = len(candidates)
    if target == 0:
      res.append(subsequence.copy())
      return

    for i in range(idx, n):
      # i > idx = not the first element &&
      # Avoid picking up duplicate combinations
      if i > idx and candidates[i] == candidates[i-1]:
        continue
      
      # this checks if the current num is greater than target. If it is then we can't find a number to 
      # get target to 0. Since the array is sorted we know every number to the right will also not work
      # so we can break
      if candidates[i] <= target: 
        subsequence.append(candidates[i])
        findCombinations(candidates, target - candidates[i], i+1, res, subsequence.copy())
        subsequence.pop()
      else:
        break

    res = []
    subsequence = []
    candidates.sort()
    findCombinations(candidates, target, 0, res, subsequence)
    return res