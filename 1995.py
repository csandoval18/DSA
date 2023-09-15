def countQuadruplets(nums):
  n = len(nums)
  count = 0
  
  for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
      target_sum = a + b
      left, right = target_sum + 1, n

      while left <= right:
        c = (left + right) // 2
        d = c - target_sum

        if d >= 1 and d <= n:
          count += 1

        if d < 0:
          left = c + 1
        else:
          right = c - 1

  return count
      

# nums = [3,3,6,4,5]
# nums = [1,2,3,6]
nums = [1,1,1,3,5]
print(countQuadruplets(nums))