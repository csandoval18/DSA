import re

def isPalindrome(s):
  # Step 1: Convert to lowercase and remove non-alphanumeric characters
  s = ''.join(filter(str.isalnum, s)).lower()
  right = len(s)-1
  
  for left in range(len(s) // 2):
    if s[left] != s[right]:
      return False
    right -= 1
  return True

print(isPalindrome("A man, a plan, a canal: Panama"))
  
  