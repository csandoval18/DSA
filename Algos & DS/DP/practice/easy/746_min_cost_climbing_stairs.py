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
        dp = [-1] * (n+1)
        
        def rec(i: int):
            if i <= 1: # Base case: if you're at or before step 0, no cost to pay
                return 0 
        
    

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
        
cost = [10,15,20]
# Output: 15
s = SolutionRecursion()
print(s.minCostClimbingStairs(cost))