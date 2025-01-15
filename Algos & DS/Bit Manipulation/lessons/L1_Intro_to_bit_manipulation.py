def convertToBinary(n: int) -> str:
  res = ""
  
  while n != 0:
    if n % 2 == 0:
      res += '0'
    else:
      res += '1'
    n = n // 2
  return res[::-1]

def convertToBinary2(n: int) -> str:
  res = ""
  
  while n != 0:
    # Error in lesson video, if we set n % 2 == 1, then we have to manually push 1 
    # at the end since the loop will end before the last 1 is added.
    if n % 2 == 1: 
      res += '1'
    else:
      res += '0'
    n //= 2
  return res[::-1]
  
n = 13
# Output: (1101)
print(convertToBinary(n))
print(convertToBinary2(n))

def convertToDecimal(s: str) -> int:
  n = len(s)
  p2 = 1
  num = 0
  
  for i in range(n-1, -1, -1):
    if s[i] == '1':
      num += p2
    p2 *= 2
    
  return num

def convertToDecimal2(s: str) -> int:
  n = len(s)
  res = 0
  
  for i in range(n-1, -1, -1):
    res += int(s[i]) * (2**(n-1-i))
  return res
  
s = "1101"
print(convertToDecimal(s))

# One's complement
# 13 = (1101) => flip => (0010)

# Two's complement 
# 1. One's complement 
# 2. Add ones to the binary sequence

# 0 0 1 0 + 
# 0 0 0 1
# _______
# 0 0 1 1 = Two's complement

