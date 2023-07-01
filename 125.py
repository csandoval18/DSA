def isPalindrome(s):
  s = s.lower()
  s = s.replace(" ", "")
  print(s)
  
  l, r = 0, len(s)
  
  for i in range(0, len(s) // 2):
    if l != r:
      return False
      l += 1
      r -= 1
  return True

print(isPalindrome("A man, a plan, a canal: Panama"))
  
  