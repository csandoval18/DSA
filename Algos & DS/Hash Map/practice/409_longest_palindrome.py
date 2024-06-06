from typing import Counter

def longestPalindrome(s: str) -> int:
  counter = Counter(s)
  L = 0 
  odd_found = False
  
  for cnt in counter.values():
    L += (cnt // 2) * 2

def longestPalindromeS(s: str) -> int:
  hm = Counter(s)
  L = 0
  odd_found = False
  
  for count in hm.values():
    L += (count // 2) * 2 # Calculation gives largest even number <= to count
    
    if count % 2 == 1:
      odd_found = True
  
  if odd_found:
    L += 1 
  
  return L

s = "abccccdd"
# len(s) = 8 
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

