def lengthOfLongestSubstring(s):
  hs = set()
  l = 0
  res = 0
  
  for r in range(len(s)):
    while s[r] in hs:
      hs.remove(s[l])
      l += 1
    
    hs.add(s[r])
    res = max(res, r-l+1)
  return res
  
# Input: s = "abcabcbb"
# Output: 3

# s = "abcabcbb"
s = "pwwkew"
# s = "aab"

print(lengthOfLongestSubstring(s))