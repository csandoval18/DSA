class SolutionBF: # SC: O(n^2) | SC: O(1)
  def longestKSubstr(self, s: str, k: int) -> int:
    maxLen = 0
    
    for i in range(len(s)):
      hm = {}
      for j in range(i, len(s)):
        hm[s[j]] = hm.get(s[j], 0) + 1
        
        if len(hm) < k:
          maxLen = max(maxLen, j-i+1)
        else:
          break
    return maxLen


class SolutionBetter: # TC: O(2N) | SC: O(256) -> worst case if the string contains all characters
  def longestKSubstr(self, s: str, k: int) -> int:
    l, maxLen = 0, 0
    hm = {}
    
    for r in range(len(s)):
      hm[s[r]] = hm.get(s[r], 0) + 1
      
      while len(hm) > k:
        hm[s[l]] -= 1
        if hm[s[l]] == 0:
          hm.pop(s[l])
        l += 1
      
      if len(hm) <= k:
        maxLen = max(maxLen, r-l+1)
        
    return maxLen


class SolutionOP:
  def longestKSubstr(self, s: str, k: int) -> int:
    l, maxLen = 0, 0
    hm = {}
    
    for r in range(len(s)):
      hm[s[r]] = hm.get(s[r], 0) + 1
      
      if len(hm) > k:
        hm[s[l]] -= 1
        if hm[s[l]] == 0:
          hm.pop(s[l])
        l += 1
      
      if len(hm) <= k:
        maxLen = max(maxLen, r-l+1)
        
    return maxLen
      

s = "aabacbebebe"
k = 3