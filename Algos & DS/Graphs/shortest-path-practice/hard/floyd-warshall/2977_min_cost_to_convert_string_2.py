from collections import defaultdict
from heapq import heappop, heappush
import heapq
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
		adj = defaultdict(list)
		nodes = set(original + changed)
		
		for u,v,w in zip(original, changed, cost):
			adj[u].append((v, w))
		
		def dijkstra(s: int):
			dist = {node: float('inf') for node in nodes}
			dist[s] = 0
			pq = [(0, s)]
			
			while pq:
				uw, u = heappop(pq)
				
				if uw > dist[u]:
					continue
					
				for v, vw in adj[u]:
					nw = uw + vw
					
					if nw < dist[v]:
						dist[v] = nw
						heappush(pq, (nw, v))
			return dist

		dist_map = {u: dijkstra(u) for u in nodes}
		
		n = len(source)
		# print(len(source), len(original))
		dp = [float('inf')]*(n+1)
		dp[0] = 0
		
		# O(n*m)
		for i in range(1, n+1):
			for node in nodes:
				length = len(node)
				l = max(0, i-length)
				
				src, des = source[l:i], target[l:i]
				
				if source[i-1] == target[i-1]:
					dp[i] = min(dp[i], dp[i-1])
				if src in adj and des in nodes:
					dp[i] = min(dp[i], dp[l] + dist_map[src].get(des, float('inf')))
					
		# print(dp)
		return dp[n-1] if dp[n-1] != float('inf') else -1
		
		
class Solution:
	def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
		adj = defaultdict(lambda: defaultdict(int))
		for i, s in enumerate(original):
			t, c = changed[i], cost[i]
			adj[s][t] = min(adj[s].get(t, c), c)

		def dijkstra(s, t):
			heap = [(0, s)]
			costs = defaultdict(lambda: float('inf'))
			costs[start] = 0
			
			while heap:
				c, v = heappop(heap)
				if v == t:
					return c
				for u in adj[v]:
					newCost = adj[v][u] + c
					if newCost < costs[u]:
						costs[u] = newCost
						heapq.heappush(heap, (costs[u], u))
			return float('inf')

		n = len(source)
		dp = [float('inf')]*(n+1)
		dp[n] = 0
		change_lengths = sorted(set(len(sub) for sub in original))
		originalSet, changedSet = set(original),  set(changed)

		for i in range(n-1, -1, -1):
			if target[i] == source[i]:
				dp[i] = dp[i+1]
			for length in change_lengths:
				start, end = i, i+length

				if end > n:
					break

				srcSub = source[start:end]
				targetSub = target[start:end]

				if srcSub in originalSet and targetSub in changedSet:
					dp[i] = min(dp[i], dijkstra(srcSub, targetSub) + dp[end])

		return dp[0] if dp[0] != float('inf') else -1