from collections import defaultdict, deque
from typing import List

def topoSort(self, V, adj):
  indegree = [0] * V
  for i in range(V):
    for it in adj[i]:
      indegree[it] += 1

  q = deque()
  for i in range(V):
    if indegree[i] == 0:
      q.append(i)

  topo = []
  while q:
    node = q.popleft()
    topo.append(node)

    for it in adj[node]:
      indegree[it] -= 1
      if indegree[it] == 0:
        q.append(it)

  return topo

def findOrder(self, dict, N, K):
  adj = [[] for _ in range(K)]
  for i in range(N - 1):
    s1, s2 = dict[i], dict[i + 1]
    len_ = min(len(s1), len(s2))
    for ptr in range(len_):
      if s1[ptr] != s2[ptr]:
        adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
        break

  topo = self.topoSort(K, adj)
  ans = ""
  for it in topo:
    ans += chr(it + ord('a'))
  return ans

  
# Follow up:
# When is the order not possible?

# 1. When the larger string is above the shorter string, ex:
# Not possible   Possible
# s1 = "abcd"    s1 = "abc"
# s2 = "abc"     s2 = "abcd"

# 2. When there is a cyclic dependency, ex:
# abc
# bat
# ade

# Notice how the 'a' order is not consistant: a -> b -> a