# nums = [0,1,2,2,4,4,1]

def mostFrequentEven(nums):
  hm = {}

  for num in nums:
    if num % 2 == 0:
      hm[num] = hm.get(num, 0) + 1
      
  max_count = 0
  most_frequent = -1
  
  for num, count in hm.items():
    if count > max_count or (count == max_count and num < most_frequent):
      max_count = count
      most_frequent = num

  return most_frequent