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