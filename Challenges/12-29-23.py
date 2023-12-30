# 1897. Redistribute Characters to Make All Strings Equal

def makeEqual(words: [str]) -> bool:
  hm = {}
  
  for word in words:
    for char in word:
      hm[char] = hm.get(char, 0) + 1
      
  for char, count in hm.items():
    # Check if the count of the curr char is divisible to all word strings
    if hm[char] % len(words):
      return False
    
  return True