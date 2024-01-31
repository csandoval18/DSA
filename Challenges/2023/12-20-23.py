def maxWidthOfVerticalArea(points: [[int]]) -> int:
  # Extract the x-coordintes from the points
  x_coords = [point[1] for point in points]
  
  # Sort the y-coordinates
  x_coords.sort()
  
  # Calculate the max height
  max_height = 0
  for i in range(1, len(x_coords)):
    max_height = max(max_height, x_coords[i]-x_coords[i-1])
  return max_height

points = [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(points))