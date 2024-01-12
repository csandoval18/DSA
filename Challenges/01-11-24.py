# 1704. Determine if String Halves Are Alike

# len(s) = even length
# Split the str into 2 halves of equal len and let "a" be the first half and "b" be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
# Notice that s contains uppercase and lowercase letters.

# Return true if "a" and "b" are alike. Otherwise, return false

def halvesAreAlike(s: str) -> bool:
  div = len(s)//2
  a = s[:div]
  b = s[div:]
  vowels = {'a','e','i','o','u','A','E','I','O','U'}
  
  a_vowel_cnt = 0
  b_vowel_cnt = 0
  for char in a:
    if char in vowels:
      a_vowel_cnt += 1
  for char in b:
    if char in vowels:
      b_vowel_cnt += 1
  
  if a_vowel_cnt == b_vowel_cnt:
    return True
  else:
    return False

s = "book"
print(s[:len(s)//2])
print(s[len(s)//2:])
print(halvesAreAlike(s))
  