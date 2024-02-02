def climbStairs(n):
  # Base case
  if n <= 2:
    return n
  
  # Initialize an array to store the number of ways to reach each step
  # We begin the array with 0 depite not being useful for the solution 
  # to maintain the index = to the step # for consistency purposes
  dp = [0] * (n+1)
  dp[1] = 1 # There is one way to reach the first step
  dp[2] = 2 # There are two ways to reach the second step
  
  # Calculate the number of ways for each step from step 3 to n.
  
  for i in range(3, n+1):
    print("dp:", dp)
    dp[i] = dp[i-1] + dp[i-2]
    print("dp:", dp)
    print("\n")
  
  return dp[n-1]


n = 4
print(climbStairs(n))