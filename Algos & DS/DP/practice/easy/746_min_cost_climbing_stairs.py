from typing import List


class SolutionRecursion:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		n = len(cost)
		
		def rec(i: int):
			# Base case: if you're at or beyond the last step, no cost to pay anymore
			if i >= n:
				return 0
			# Recursive case: take the current step and move to the next step
			return cost[i] + min(rec(i+1), rec(i+2))
		# You can start from either step 0 or step 1
		return min(rec(0), rec(1))
		
	
class SolutionMemoizationDict:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		dp = {}
		# Base cases:
		def rec(i: int):
			if i < 0: 				
				return 0
			if i == 0 or i == 1:
				return cost[i]

			dp[i] = min(rec[i-1], rec(i-2) + cost[i])
			
		n = len(cost)
		return min(dp(n-1), dp(n-2))

class SolutionMemoizationArray:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		dp = [-1]*n
		# Base cases:
		def rec(i: int):
			if i < 0: # Index i is exahausted
				return 0
			if i == 0 or i == 1: # First or second steps are reached
				return cost[i]

			dp[i] = min(rec[i-1], rec(i-2) + cost[i])
			
		n = len(cost)
		return min(dp(n-1), dp(n-2))


class SolutionMemoization:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		dp = {}
		# Base cases:
		def rec(i: int):
			if i < 0: # i is exahausted
				return 0
			if i == 0 or i == 1:
				return cost[i]
			
			# Memoization
			if i in dp:
				return dp[i]

			dp[i] = min(rec(i-1), rec(i-2)) + cost[i]
			return dp[i]
		n = len(cost)
		return min(rec(n-1), rec(n-2))
		
		
class SolutionSpaceOptimized:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		n = len(cost)
		if n == 0:
			return 0
		if n == 1:
			return cost[0]
		
		# Initialize the first two steps
		first = cost[0]
		second = cost[1]
		
		# Calculate the min cost using only two variables
		for i in range(2, n):
			curr = cost[i] + min(first, second)
			first = second
			second = curr
				
		return min(first, second)
        
cost = [10,15,20]
# Output: 15
s = SolutionRecursion()
print(s.minCostClimbingStairs(cost))