from typing import List

'''
Find max len subarray with at most 2 different numbers.
'''

class SolutionBF: # TC: O(n^2) | SC: O(3) => Storing no more than 3 items in map 
  def totalFruit(self, fruits: List[int]) -> int:
    for i in range(len(fruits)):
      st = set()
      
      for j in  range(i, len(fruits)):
        st.add(fruits[i])
        if len(st) <= 2:
          maxLen = max(maxLen, j-i+1)
        else:
          break
    return maxLen
    
    
class SolutionBetter: # TC: O(N+N) => O(2N) | SC:  O(3)
  def totalFruit(self, fruits: List[int]) -> int:
    l, maxLen = 0, 0
    K = 2
    hm = {}
    
    for r in range(len(fruits)):
      hm[fruits[r]] = hm.get(0, fruits[r]) + 1
      
      if len(hm) > K:
        while len(hm) > K: # Shrink window when there is 3 items in the dict
          hm[fruits[l]] -= 1 # Decrement the current element at pointer l
          
          if hm[fruits[l]] == 0: # If the removed element's count is 0 in the dict, then 
            hm.pop(fruits[l]) # remove the element from the dict to get the dict len back to two
          l += 1  # Increment the l pointer

      if len(hm) <= K:
        maxLen = max(maxLen, r-l+1)
    return maxLen


class SolutionOP: # TC: O(N) | SC:  O(3) => O(1)
  def totalFruit(self, fruits: List[int]) -> int:
    l, maxLen = 0, 0
    K = 2
    hm = {}
    
    for r in range(len(fruits)):
      hm[fruits[r]] = hm.get(fruits[r], 0) + 1
      
      if len(hm) > K:
        hm[fruits[l]] -= 1
        
        if hm[fruits[l]] == 0:
          hm.pop(fruits[l])
        l += 1
      
      if len(hm) <= K:
        maxLen = max(maxLen, r-l+1)
    return maxLen


fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees

fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

s = SolutionBetter()
print(s.totalFruit(fruits))
