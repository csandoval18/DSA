from typing import List

'''
Find max len subarray with at most 2 different numbers.
'''

class SolutionBF:
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
    
class SolutionOP:
  def totalFruit(self, fruits: List[int]) -> int:
    l, maxLen = 0, 0
    hm = {}
    
    for r in range(len(fruits)):
      while r < len(fruits):
        hm[fruits[r]].get(0, fruits[r]) + 1
        
      
    

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

