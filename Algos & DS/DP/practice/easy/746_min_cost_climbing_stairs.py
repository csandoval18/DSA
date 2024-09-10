class Solution:
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

class SolutionRecursion:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def minCost(i):
            # Base case: if you're at or beyond the last step, no cost to pay anymore
            if i >= n:
                return 0
            # Recursive case: take the current step and move to the next step
            return cost[i] + min(minCost(i+1), minCost(i+2))
        # You can start from either step 0 or step 1
        return min(minCost(0), minCost(1))
        
cost = [10,15,20]
# Output: 15