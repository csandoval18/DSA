from typing import List


# Brute force naive approach generating all possible combinations
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      def bt(start: int, path: List[int]):
        # Calculate the sum of the current combation
        curr_sum = sum(path)
        # If the sum equals the target, add the path to the results
        if curr_sum == target:
          # Sort the path to avoid duplicate combinations in different orders
          sorted_ds = tuple(sorted(path))
          res_set.add(sorted_ds)
        # If the sum exceeds the target, stop exploring further
        elif curr_sum > target:
          return
        # Try every candidate starting from the current index
        for i in range(start, len(candidates)):
          bt(i+1, path + [candidates[i]])
          
      res_set = set()
      bt(0, [])
      return [list(comb) for comb in res_set]

class Solution:
  def combinationSum2jo(self, candidates: List[int], target: int) -> List[List[int]]:
    def bt(rem: int, start: int, path: List[int]):
      # If the remaining sum is zero, we've found a valid combination
      if rem == 0:
        res.append(path)
        return
      
      # Explore each candidate starting from the current index `start`
      for i in range(start, len(candidates)):
        # Skip duplicates: ensure we don't pick the same element twice in a row
        if i > start and candidates[i] == candidates[i-1]:
          continue
        # If the current candidate is greater than the remaining sum, stop the loop
        if candidates[i] > rem:
          break
        # Recursively explore further with the current candidate included
        bt(rem-candidates[i], i+1, path+[candidates[i]])
        
        # Backtracking implicitly occurs here as the loop continues to the next iteration
        # The function "backtracks" to explore other possibilities by trying the next candidate
    
    n = len(candidates)
    # Sort candidates in descending order
    candidates.sort()
    # Result list to store all valid combinations
    res = []
    # Start backtracking from the first index
    bt(target, 0, [])
    return res
    
    
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
         candidates.sort()
         res = []

         def dfs(target, start, comb):
             if target < 0:
                 return
             if target == 0:
                 res.append(comb)
                 return
             for i in range(start, len(candidates)):
                 if i > start and candidates[i] == candidates[i-1]:
                     continue
                 if candidates[i] > target:
                     break
                 dfs(target-candidates[i], i+1, comb+[candidates[i]])

         dfs(target, 0, [])
         return res