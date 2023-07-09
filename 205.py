class Solution(object):
  def isIsomorphic(self, s, t):
    hm = {}
    
    for i in range(len(t)):
      if s[i] not in hm:
        hm[t[i]] = s[i]
      else:
        return False
    return True

s = "foo"
t = "bar"

ans = Solution()
print(ans.isIsomorphic(s, t))