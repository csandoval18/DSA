s = "011101"

# Output: 5

# All poss ways of splitting s into two non-empty-substrings are:

# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

# The score after splitting a string is the number of zeros in the 
# left substring plus the number of ones in the right substring.

# BF
def checkIfExist(arr: [int]) -> bool:
  n = len(arr)
  
  for i in range(n):
    for j in range(i+1, n):
      print(arr[i], end=" ")
      print(arr[j])
      if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
        return True
  return False

# Optimal
def checkIfExistfOP(nums):
  st = set()
  
  for num in arr:
    if num*2 in st or (num%2 == 0 and num // 2 in st):
      return True
    st.add(num)
  return False
    
# Why do need need to check if num is an even #?
# case: arr = [3,1,7,11] 

# arr = [10,2,5,3]
arr = [7,1,14,11]

print(checkIfExist(arr))

    