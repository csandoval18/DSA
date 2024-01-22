# [3,2,1]
#  0 1 2
def print_subsequences_strivers(arr: [int], i: int, subsequence: [int]) -> None: 
  n = len(arr)
  
  if i >= n:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def print_subsequences(arr, i, subsequence):
  # Base case: if index exceeds the array size, print the subsequence
  n = len(arr)
  if i >= n:
    print(subsequence)
    return
  
  # Include the current element in the subsequence
  print_subsequences(arr, i+1, subsequence + [arr[i]])
  # Exclude the current element from the subsequence
  return print_subsequences(arr, i+1, subsequence)

# Example usage:
arr = [3, 1, 2]
a = print_subsequences(arr, 0, [])
print("a:", a)

print()
print("-----------------------------------------------------------")
print()

def generate_subsequence_sums(arr, current_sum=0, index=0):
  # Base case: when we reach the end of the array
  if index == len(arr):
    print(current_sum)
    return

  # Recursive case 1: Include the current element
  generate_subsequence_sums(arr, current_sum + arr[index], index + 1)

  # Recursive case 2: Exclude the current element
  generate_subsequence_sums(arr, current_sum, index + 1)

# Example usage:
input_array = [1, 2, 3]
generate_subsequence_sums(input_array)

# [3,1,2]
# [3,1]
# [3,2]
# [3]
# [1,2]
# [1]
# [2]
# []

print()
print("-----------------------------------------------------------")
print()

def generate_subsequence_sums(arr):
  n = len(arr)
  
  # Loop to iterate through all possible subsets
  for i in range(2**n):
    current_sum = 0
    
    # Inner loop to check each bit of the binary representation
    for j in range(n):
      if (i >> j) & 1:
        current_sum += arr[j]
    
    print(current_sum)

# Example usage:
input_array = [1, 2, 3]
generate_subsequence_sums(input_array)
