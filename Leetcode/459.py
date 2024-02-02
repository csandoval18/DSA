class Solution(object):
  def repeatedSubstringPattern(self, s):
    substring = ""
    
    for char in s:
      substring += char
      tmp = substring
      print("substring:", substring)
      
      while len(s) > len(tmp):
        tmp += substring
        print("tmp:", tmp)
        
        if tmp == s:
          return True
    return False

s = "abab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))

