# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. 
# In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. 
# For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

# "0100"
# Out: 1

def minOperationsAttempt1(self, s: str) -> int:
  n = len(s)

  if n == 1:
    return 0

  res = 0
  l, r = 0, 1

  while r < n:
    if s[l] == s[r]:
      res += 1
    l += 2
    r += 2
  return res
  
# Remember strings are immutable in python
def minOperationsAttempt2(s: str) -> int:
  arr = list(s)
  n = len(arr)
  if n == 1:
    return 0
    
  res = 0
  for i in range(1, n, 1):
    if arr[i] == arr[i-1]:
      res += 1
      if arr[i] == "1":
        arr[i] = "0"
      else:
        arr[i] = "1"
  return res
        
def minOperations(s: str):
  # Initialize the count of mismatches
  cnt = 0
  
  # Iterate through the str and count mismatches
  for i in range(len(s)):
    # Check if the char at position i matches the expected alternating pattern
    if i%2 == 0:
      expected_char = '0'
    else:
      expected_char = '1'
    
    if s[i] != expected_char:
      cnt += 1
  return cnt//2
  
def minOperations(s: str) -> int:
  change_1 = 0
  curr = True

  for char in s:
    if curr == (char == "0"):
      change_1 += 1
      
    curr = not curr
  return min(change_1, len(s) - change_1)
      
def minOperations(s: str) -> int:
  c0 = 0
  c1 = 0

  for i in range(len(s)):
    if i % 2 == 0: 
      # c0 wants 0, c1 wants 1
      if s[i] == '0':
        c1 += 1
      else:
        c0 += 1
    else:
      # c0 wants 1, c1 wants 0
      if s[i] == '1':
        c1 += 1
      else:
        c0 += 1
  
  return min(c0, c1)
      
s = "10010100"
# 01234567
# 10010100
# Expected 3 got 1
print(minOperations(s))