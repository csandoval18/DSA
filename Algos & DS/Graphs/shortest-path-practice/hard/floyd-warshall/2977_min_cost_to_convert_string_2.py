from typing import List

# You are given 0 indexed string source and target, both of length n
# and consisting of lowercase Ennglish chars. You are also given two 0-indexed
# string arrays original and changed, and an integer array cost, where cost[i]
# represents the cost of converting the string original[i] to the string changed[i]

class Solution:
	def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
		n = len(source)
		INF = float('inf')
		
		# Number of different lowercase English letters
		NUM_LETTERS = 26
		# Create a cost matrix initialized to INF
		dist = [[INF] * NUM_LETTERS for _ in range(NUM_LETTERS)]
		
		# Initialize the diagonal to 0 (cost to transform a character to itself)
		for i in range(NUM_LETTERS):
			dist[i][i] = 0
		# Populate the cost matrix with the given transformation costs
		for o, c, z in zip(original, changed, cost):
			dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], z)
		# Floyd-Warshall algorithm to find the shortest paths between all pairs of nodes
		for k in range(NUM_LETTERS):
			for i in range(NUM_LETTERS):
				for j in range(NUM_LETTERS):
					if dist[i][k] < INF and dist[k][j] < INF:
						dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
		
		# Calculate the minimum cost to transform source to target
		total_cost = 0
		for s_char, t_char in zip(source, target):
			s_idx = ord(s_char) - ord('a')
			t_idx = ord(t_char) - ord('a')
			if dist[s_idx][t_idx] == INF:
				return -1
			total_cost += dist[s_idx][t_idx]
		
		return total_cost
        
class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Construct a directed conversion graph using defaultdict
        graph = defaultdict(list)
        nodes = set(original + changed)
        for u, v, w in zip(original, changed, cost):
            graph[u].append((v, w))

        # Precompute Dijkstra's algorithm results for all nodes
        def dijkstra(s):
            dist = {node: float("inf") for node in nodes}
            dist[s] = 0
            queue = [(0, s)]
            while queue:
                d, node = heappop(queue)
                if d > dist[node]:
                    continue
                for v, w in graph[node]:
                    new_dist = d + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heappush(queue, (new_dist, v))
            return dist

        dist_map = {node: dijkstra(node) for node in nodes}

        # Main DP loop
        n = len(source)
        print(len(source), len(original))
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # this check is O(n*m)
        for i in range(1, n + 1):
            for node in nodes:
                length = len(node)
                l = max(0, i-length)

                src, des = source[l:i], target[l:i]

                if source[i-1] == target[i-1]:
                    dp[i] = min(dp[i], dp[i-1])
                if src in graph and des in nodes:
                    dp[i] = min(dp[i], dp[l] + dist_map[src].get(des, float("inf")))
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1