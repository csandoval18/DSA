from typing import List


class SolutionRec:
	def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
		

class SolutionDP:
  def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    if not words or not groups:
      return []
    
    res = [words[0]]
    prev_group = groups[0]

    for i in range(1, len(words)):
      if groups[i] != prev_group:
        res.append(words[i])
        prev_group = groups[i]
    return res

words = ["e","a","b"]
groups = [0,0,1]
# Output: ["e","b"]