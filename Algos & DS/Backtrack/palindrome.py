# Two poinnters
def recPalindrome(s: str, l: int, r: int) -> bool:
  if l >= r and s[l] == s[r]:
    return True
  
  if s[l] != s[r]:
    return False
  
  return recPalindrome(s, l+1, r-1)
  
def recPalindromev2(s: str, i: int) -> bool:
  if i >= len(s)//2 and s[i] == s[len(s)-1-i]:
    return True
    
  if s[i] != s[len(s)-1-i]:
    return False
  
  return recPalindromev2(s, i+1)

# s = "llllabcddcballll"
s = "dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd"
print(recPalindrome(s, 0, len(s)-1))
print(recPalindromev2(s, 0))


  