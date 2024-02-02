class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      # populate magazine with possible letters in hm
      letters = {}
      for i, n in enumerate(magazine):
        if n not in letters: 
          letters[n] = 1
        else:
          letters[n] += 1
        
        
      for i in ransomNote:
        if i not in letters or letters[i] <= 0:
          return False
        else: 
          letters[i] -= 1
          
      return True
      
ans = Solution()

ransomNote = "aa"
magazine = "aab"

print(ans.canConstruct(ransomNote, magazine))