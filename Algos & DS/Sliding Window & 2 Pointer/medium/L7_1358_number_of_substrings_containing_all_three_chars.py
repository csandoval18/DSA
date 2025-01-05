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
      
      
class SolutionBetter:
    def numberOfSubstrings(self, s: str) -> int:
      lastSeen = [-1, -1, -1]
      cnt = 0
      
      for i in range(len(s)):
        lastSeen[ord(s[i]) - ord('a')] = i # Update the last seen index for the current char
        
        if -1 not in lastSeen: # Check if all chars have been seen 
          # Add 1 for the found subarray and add the index of the min last seen char to add the total count of 
          # subarrays that match the condition. For example if the min is in index 2 then we can add 2 because
          # there are two elements to the left of that index (0, 1, 2)
          cnt += (1 + min(lastSeen)) 
      return cnt

class SolutionBetter2:
    def numberOfSubstrings(self, s: str) -> int:
      l, cnt = 0, 0
      K = 3
      hm = {}
      
      for r in range(len(s)):
        hm[s[r]] = hm.get(hm[s[r]], 0) + 1
        
        while len(hm) > K:
          cnt += len(s) - r
          
          if hm[s[l]] == 0:
            hm.pop(s[l])
      return cnt
      
      
        
          
          

s = 'bacba'
