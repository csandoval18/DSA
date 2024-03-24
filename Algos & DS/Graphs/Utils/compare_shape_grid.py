# In the problem (Number of Distinct Islands) we must compare shapes to determine if they are the same or not

grid = [
#  0 1 2 3 4
  [1,1,0,1,1], # 0
  [1,0,0,0,0], # 1
  [0,0,0,1,1], # 2
  [1,1,0,1,0], # 3
]

# Unique shapes = 2

shape1 = [
#  0  1
  [1, 1], # 0
  [1]     # 1
]

shape2 = [
#  3  4
  [1, 1], # 2
  [1]     # 3
]


# First shape coordinates
#  x y   x y 
# (0,0) (0,1)
# (1,0)
#  x y 

# Second shape coordinates
#  x y   x y 
# (2,3) (2,4)
# (3,3)
#  x y 

#         Base
# (0,0) - (0,0) = (0,0)
# (0,1) - (0,0) = (0,1)
# (1,0) - (0,0) = (1,0)

#         Base
# (2,3) - (2,3) = (0,0)
# (2,4) - (2,3) = (0,1)
# (3,3) - (2,3) = (1,0)

# Notice they give the same output 
# Basically we need to use (curr_x, curr_y) - (reference_x, reference_y) = Shape comparison coordinates.
# We can use a set to maintain the unique shapes found in the matrix
# Keep in mind that we need to have the same starting base location cell of the shape, otherwise the comparsion will not work,
# Once we have traversed the shape we should mark the visited cells of the island as True so the algorithm does not think
# a new island body has been found.
# Follow the same pattern of traversal weather we are using BFS or DFS to find the adjacent cells