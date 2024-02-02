class Solution(object):
  def isIsomorphic(self, s, t):
    hm = {}
    rev = {}
    
    for i in range(len(t)):
      if s[i] not in hm and t[i] not in rev:
        hm[s[i]] = t[i]
        rev[t[i]] = s[i]
      else:
        return False
    return True

s = "egg"
t = "add"

ans = Solution()
print(ans.isIsomorphic(s, t))


def isIsomorphic(s, t):
  if len(s) != len(t):
    return False
  
  hm = {}
  rev = {}
  
  for i in range(len(s)):
    char_s, char_t = s[i], t[i]
    
    # Check mapping from s to t
    if char_s in hm:
      if hm[char_s] != char_t:
        return False
    else:
      hm[char_s] = char_t
    
    # Check mapping from t to s
    if char_t in rev:
      if rev[char_t] != char_s:
          return False
    else:
      rev[char_t] = char_s
  return True