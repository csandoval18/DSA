def reverseVowels(s: str) -> str:
  l, r = 0, len(s)-1
  vowels = {'a','e','i','o','u','A','E','I','O','U'}
  s_list = list(s)
  
  while l<r:
    if s_list[l] not in vowels:
      l += 1
    if s_list[r] not in vowels:
      r -= 1
    if s_list[r] in vowels and s_list[l] in vowels:
      s_list[r], s_list[l] = s_list[l], s_list[r]
      l += 1
      r -= 1
  
  return "".join(s_list)

s = "hello"
print(reverseVowels(s))