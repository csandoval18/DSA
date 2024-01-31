# 91. Decode Ways

def numDecodings(s: str) -> int:
  if not s or s[0] == '0':
    return 0
  
  n = len(s)
  dp = [0] * (n+1)
  dp[0] = 1
  dp[1] = 1 # For a single-digit string, there is only one way to decode
  
  for i in range(2, n+1):
    # Check if the single digit is valid
    if 1 <= int(s[i-1]) <= 9:
      dp[i] += dp[i-1]
    
    # Check if the two digits form a valid number (between 10 and 26)
    two_digits = int(s[i-2:i])
    # Extracting a substring of length 2 from the input string s starting 
    # from the (i-2)th index up to (but not including) the ith index. 
    # This substring represents a two-digit number.
    if 10 <= two_digits <= 26:
      dp[i] += dp[i-2]
    
  return dp[n]