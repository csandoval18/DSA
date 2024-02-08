from typing import List

# Greedy fails => try all possible ways
# try all possible ways => recursion
# 1. Express every possible problem terms of idx
# 2. Do changes on that idx 
# 3. Find the max 

# Memoization
def ninjaTraining(n: int, points: List[List[int]]) -> int:
  def helper(day: int, last: int, dp: List[List[int]]) -> int:
    # Check if the result for this day and last activity is already computed.
    if dp[day][last] != -1:
      return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    if day == 0:
      cmax = 0
      for task in range(3):
        if task != last:
          cmax = max(cmax, points[0][task])
      dp[day][last] = cmax
      return dp[day][last]

    cmax = 0
    # Iterate through all activities for the current day.
    for task in range(3):
      if task != last:
        # Calculate the total points for the current day's activity and recursively call for the previous day.
        activity = points[day][task] + helper(day - 1, task, dp)
        cmax = max(cmax, activity)

    # Store the maximum points in the DP table and return it.
    dp[day][last] = cmax
    return dp[day][last]
    
  # Initialize a DP table to store the computed results.
  dp = [[-1 for j in range(4)] for i in range(n)]
  # Start the recursive function from the last day with no previous activity.
  return helper(n - 1, 3, dp)

points = [[10, 40, 70],
          [20, 50, 80],
          [30, 60, 90]]
n = len(points)

print(ninjaTraining(n, points))

# Tabulation (Bottom Up)
# 1. Declare similar size dp array
# 2. For index case in 2d dp
# In index 0 last can be 0, 1, or 2

def ninjaTrainingTabulation(n: int, points: List[List[int]]) -> int:
  # Initialize dp table with dimensions (n*4) to store the max points
  dp = [[0 for j in range(4)] for i in range(n)]
  
  # Initialize the dp table for the day 0 with base cases
  dp[0][0] = max(points[0][1], points[0][2]) # Task 1
  dp[0][1] = max(points[0][0], points[0][2]) # Task 2
  dp[0][2] = max(points[0][0], points[0][1]) # Task 3
  dp[0][3] = max(points[0][0], points[0][1], points[0][2]) # All the tasks
  
  # Loop through the days starting from the second day
  for day in range(1, n):
    for last in range(4):
      dp[day][last] = 0 # Initialize the max points for the curr day and last activity
      for task in range(3):
        if task != last:
          # Calc the total points for the curr day's ativity and the prev day's max points
          activity = points[day][task] + dp[day-1][task]
          dp[day][last] = max(dp[day][last], activity)
          
  return dp[n-1][3]

print(ninjaTrainingTabulation(n, points))

# Space Optimize 
# You only need one row (arr) that keep track of the last pick the previous data is irrelevant
def ninjaTrainingSO(n: int, points: List[List[int]]) -> int:
  # Initialize a list 'prev' to store the max points for each possible last activity on the prev day
  prev = [0]*4
  
  # Initialize through the days starting from the second day.
  prev[0] = max(points[0][1], points[0][2])
  prev[1] = max(points[0][0], points[0][2])
  prev[2] = max(points[0][0], points[0][1])
  prev[3] = max(points[0][0], points[0][1], points[0][2])
