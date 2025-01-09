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
  # In this solution the added counted substrings are to the left of min(lastSeen) 
  # 1 + min(lastSeen), 1 is added to add the current subarray to count
  def numberOfSubstrings(self, s: str) -> int:
    lastSeen = [-1, -1, -1]
    cnt = 0
    
    for i in range(len(s)):
      lastSeen[ord(s[i]) - ord('a')] = i # Update the last seen index for the current char using ord function to get alphabetic index of chars 'a', 'b', and 'c'
      
      if -1 not in lastSeen: # Check if all chars have been seen 
        # Add 1 for the found subarray and add the index of the min index of the last seen char to add the total count of subarrays that match the condition. 
        # For example if the min last seen char is in index 2 then we can add 2 because there are two elements to the left of that index [(0, 1), 2]
        cnt += (1 + min(lastSeen))
    return cnt
      
      
class SolutionBetterAvoidingOrdFunction:
  def numberOfSubstrings(self, s: str) -> int:
    lastSeen = [-1, -1, -1] # Indices for 'a', 'b', 'c'
    cnt = 0
    
    for i in range(len(s)): 
      if s[i] == 'a': # This is the equivalent of what the ord function is allowing us to do in a shorter code in the solution above, the index is automatically given by substraction from ord('a')
        lastSeen[0] = i
      elif s[i] == 'b':
        lastSeen[1] = i
      elif s[i] == 'c':
        lastSeen[2] = i
      
      if -1 not in lastSeen:
        cnt += (1 + min(lastSeen))
    return cnt
          

class SolutionBetterPreviousPattern: 
  # In this solution using the previous pattern substrings that meet the condition are added from the right pointer 'r' 
  # [len(s) - r] to get every subarray to the right, one is not added in this version since len(s) - r accounts for the current subarray
  def numberOfSubstrings(self, s: str) -> int:
    l, cnt = 0, 0
    K = 3
    hm = {}
    
    for r in range(len(s)):
      hm[s[r]] = hm.get(s[r], 0) + 1 # Update frequency of chars
      
      while len(hm) == K: # When we have all three distinct chars
        cnt += len(s) - r # Count all substring ending at index 'r'
        
        hm[s[l]] -= 1 # Shrink the window
        if hm[s[l]] == 0:
          hm.pop(s[l]) # Remove character from map if count reaches 0
        l += 1 # Move the left pointer
    return cnt 
      
s = "abcabc"
# Output: 10
sol = SolutionBetterAvoidingOrdFunction()
print(sol.numberOfSubstrings(s))