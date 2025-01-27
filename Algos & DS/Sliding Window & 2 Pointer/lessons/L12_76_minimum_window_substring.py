from collections import defaultdict


class SolutionBF: # TC: O(N^2) | SC: O(256)
  def minWindow(self, s: str, t: str) -> str:
    n, m = len(s), len(t)
    sIndex = -1 # Starting index of the result substring
    minLen = float('inf') # Length of the minimum substring
    hm = {} # Create a hashmap to store the frequency of characters in t
    
    for char in t: # Pre-insert map with characters of t
      hm[char] = hm.get(char, 0) + 1
    
    for l in range(n):
      for r in range(l, n):
        cnt = 0 # Count of matched chars
        # Check if the current character in s is in t
        if s[r] in hm and hm[s[r]] > 0:
          cnt += 1
          hm[s[r]] -= 1
          
        # If all characters in t are matched
        if cnt == m:
          if (r-l+1) < minLen: # Update the minimum substring length and starting index
            minLen = r-l+1
            sIndex = l
            break # No need to check further for this starting index
            
    # Return the result substring or an empty string if no valid window is found
    return s[sIndex:sIndex + minLen] if sIndex != -1 else ""


class SolutionBetter: # TC: O(2N) | SC: O(256)
  def minWindow(self, s: str, t: str) -> str:
    n, m = len(s), len(t)
    hm = {}
    l, sIndex = 0, -1
    minLen = float('inf')
    cnt = 0
    
    for c in t: # Pre-insert char frequencies of t into the map
      hm[c] = hm.get(c, 0) + 1
    
    for r in range(n):
      if hm.get(s[r], 0) > 0:
        cnt += 1
      hm[s[r]] = hm.get(s[r], 0) - 1
      
      while cnt == m:
        if r - l + 1 < minLen:
          minLen = r - l + 1
          sIndex = l
        
        hm[s[l]] = hm.get(s[l], 0) + 1
        if hm[s[l]] > 0:
          cnt -= 1
        l += 1
  
    return "" if sIndex == -1 else s[sIndex: sIndex + minLen]


class SolutionDefaultDict: # TC: O(2N) | SC: O(256)
  def minWindow(self, s: str, t: str) -> str:
    n, m = len(s), len(t)
    minLen, sIndex = float('inf'), -1
    l, cnt = 0, 0
    hm = defaultdict(int) # Remember we declare the type of the value not the key when using defaultdict
    
    for c in t:
      hm[c] += 1
    
    for r in range(n):
      if s[r] in hm and hm[s[r]] > 0:
        cnt += 1
      hm[s[r]] -= 1
    
      while cnt == m: # Shrink window when the count has reached the size of string t, meaning we have found all the chars required
        if r-l+1 < minLen: # Check if the matched window is smaller than the smallest found so far
          minLen = r-l+1 # Update minLen with the new window size
          sIndex = l # Update the starting index of the new minLen window match with its starting index => l pointer
        
        hm[s[l]] += 1 # Remove the leftmost char from the window and update count and l pointer
        if s[l] in hm and hm[s[l]] > 0:
          cnt -= 1
        l += 1
    return "" if sIndex == -1 else s[sIndex: sIndex + minLen]

s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"

s = "a"
t = "a"
# Output: "a"

s = "a"
t = "aa"
# Output: ""

sol = SolutionDefaultDict()
print(sol.minWindow(s, t))