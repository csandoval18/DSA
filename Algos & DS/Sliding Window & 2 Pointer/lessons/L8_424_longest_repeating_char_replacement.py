class SolutionBF:
  def characterReplacement(self, s: str, k: int) -> int:
    maxFreq, maxLen = 0, 0
    hm = {}
    
    for l in range(len(s)):
      hm = {}
      
      for r in range(l, len(s)):
        hm[s[r]] += 1
        maxNum = max(maxFreq, hm[s[l]])
        
        changes = (r-l+1) - maxFreq
        if changes <= k:
          maxLen = max(maxLen, r-l+1)
        else:
          break
    return maxLen
        
        
class SolutionBetterStriver:
  def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    maxLen, maxFreq = 0, 0
    hm = {}
    
    for r in range(len(s)):
      hm[s[r]] = hm.get(s[r], 0) + 1
      maxFreq = max(maxFreq, hm[ord(s[r]) - ord('A')])
      
      while (r-l + 1) - maxFreq > k:
        hm[ord(s[l]) - ord('A')] -= 1 
        
        for i in range(25):
          maxFreq = max(maxFreq, hm[i])
        l += 1
          
      if (r-l+1) - maxFreq <= k:
        maxLen = max(maxLen, r-l+1)
    return maxLen
    
    
class SolutionBetterGPTFixed:
  def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    maxFreq, maxLen = 0, 0
    hm = {}
    
    for r in range(len(s)):
      hm[s[r]] = hm.get(s[r], 0) + 1
      maxFreq = max(maxFreq, hm[s[r]]) # track the max freq within the window
      
      # If the window size minus the max frequency is greater than K, shrink the window
      if (r-l+1) - maxFreq > k:
        hm[s[l]] -= 1
        l += 1
        
      # Update the max len after adjusting the window
      maxLen = max(maxLen, r-l+1)
    return maxLen
      
      
s = "AABABBA"
k = 2