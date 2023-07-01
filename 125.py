def isPalindrome(s):
  # Removes spaces and non alphanumeric values
  s = ''.join(char.lower() for char in s if char.isalnum())
  l, r = 0, len(s)-1
  print(s)
  print(range(0,(len(s)//2)))
  
  for i in range(0, (len(s) // 2)):
    print(l, r)
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

print(isPalindrome(".,"))
  
def isPalindrome1(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

