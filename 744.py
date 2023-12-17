# Find smallest letter greater than target

# You are given an arr of chars letters that is sorted in non decreasing order
# (increasing order) and a char target. There are at least two different chars
#  in letters.

# Return the smallest char in letters that is lexicographically greater than target.
print(ord("a"))

def nextGreatestLetter(letters: [str], target: str) -> str:
  n = len(letters)
  l, r  = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if letters[m] <= target:
      l = m+1
    else:
      r = m-1
  # If l pointer == to n, then we have reached the end and should 
  # wrap around to the first el since not greater el exists
  if l == n:
    return letters[0]
  else:
    return letters[l]
    
  # or the same below to wrap around the first el
  # return letters[l%n]
  

letters = ["c", "f", "j"]
target = "c"

# Desired output: "c"
print("output:", nextGreatestLetter(letters, target))
  