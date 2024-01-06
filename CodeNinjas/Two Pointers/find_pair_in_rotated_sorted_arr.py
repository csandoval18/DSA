# Alice and Bob always loved to play with arrs. Alice took a sorted arr and rotated it clockwise 
# for a certain number of times

# After rotating a sorted arr, Alice gave a num 'K' to Bob and asked him to search for a pair 
# in an arr whose sum is equal to 'K'. 

# Your task is to find out whether there exists a pair in 
# the arr with sum 'K' or not. 

# If there exists a pair then you can return True else return False

def findPairSum(arr: [int], target: int) -> bool:
  def bs(arr, target):
    n = len(arr)
    l, r = 0, n-1
    
    while l<=r:
      m = (l+r)//2
      
      if arr[m] == target:
        return arr[m]
      elif arr[l] <= arr[m]:
        if arr[l] <= target <= arr[m]:
          r = m-1
        else:
          l = m+1
      elif arr[m] <= arr[r]:
        if arr[m] <= target <= arr[r]:
          l = m+1
        else:
          r = m-1
    return -1

  for num in arr:
    neededNum = target-num
    res = bs(arr, neededNum)
    if res == neededNum and res != num:
      return True
  return False
    
target = 4
arr = [5,7,9,1,3]
# target = 2
# arr = [8,10,11,1]
print(findPairSum(arr, target))

# [5,7,9,1,3]
#  L   M   R

# [5,5,5,1,3]
#  L   M   R