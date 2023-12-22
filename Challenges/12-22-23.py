# 1422. Maximum Score After Splitting a String

# Output: 5
# All poss ways of splitting s into two non-empty-substrings are:

# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

# The score after splitting a string is the number of zeros in the 
# left substring plus the number of ones in the right substring.

 
# BF
def maxScore(s: str) -> int:
  n = len(s)
  maxScore = 0
  
  for i in range(1, n):
    l_str = s[:i]
    r_str = s[i:]
    print("left:", s[:i])
    print("right:", s[i:])
    print("\n")
    
    l_score = 0
    r_score = 0
    
    for char in l_str:
      if int(char) == 0:
        l_score += 1
    for char in r_str:
      if int(char) == 1:
        r_score += 1
    
    maxScore = max(maxScore, l_score+r_score)
  
  return maxScore
    

  
s = "1111"
# s = "00"
# print(s[:1])
# print(s[1:])
print(maxScore(s))
