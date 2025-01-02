class SolutionBF: # TC: O(N^2) | SC: O(1)
    def numberOfSubstrings(self, s: str) -> int:
      cnt = 0
      
      for i in range(len(s)):
        hm = {}
        for j in range(i, len(s)):
          hm[s[j] - 'a'] = hm.get(s[j] - 'a', 0) + 1
          
          if hm[0] + hm[1] + hm[2] == 3:
            cnt += 1
      return cnt
      
      
class SolutionBetter:
    def numberOfSubstrings(self, s: str) -> int:
      cnt = 0
      
      for i in range(len(s)):
        hm = {}
        for j in range(i, len(s)):
          hm[s[j] - 'a'] = hm.get(s[j] - 'a', 0) + 1
          
          if hm[0] + hm[1] + hm[2] == 3:
            cnt = cnt + (len(s)-j)
            break
      return cnt
      