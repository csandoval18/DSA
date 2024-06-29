from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
       indegree = defaultdict(int)
       
        # Step 1: Count the number of roads connected to each city
       for u, v in roads:
        indegree[u] += 1
        indegree[v] += 1
    
        # sorted_adj = sorted(indegree.items(), key=lambda x: -x[1])
        # Step 2: Create a list of tuples (road_count, city)
        city_road_counts = [(indegree[node], node) for node in range(n)]
        
        # Step 3: Sort the list of tuples by indegree in descending order. This way, cities with the highest connection counts come first.
        city_road_counts.sort(reverse=True)
        
        # Step 4: Extract the sorted cities from the sorted list of tuples
        sorted_cities = [node for _, node in city_road_counts]
        
        # Step 5: Assign the highest importance values to the most connected cities
        importance = [0]*n
        curr_importance = n
        
        for city in sorted_cities:
            importance[city] = curr_importance
            curr_importance -= 1
        
        # Step 6: Calculate the total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += importance[a] + importance[b]
        return total_importance