from typing import List

'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie 
j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 

Your goal is to maximize the number of your content children and output the maximum number.
ie. return the max content children possible 
'''

class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # if s[i] >= g[i]
    g.sort()
    s.sort()
    i, j = 0, 0
    
    while i < len(g) and j < len(s):
      if s[j] >= g[i]:
        x += 1
      y += 1
    return x

g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]

g = [10,9,8,7]
s = [5,6,7,8]

#         x
# g = 7 8 9 10
# s = 5 6 7 8
#           y
2