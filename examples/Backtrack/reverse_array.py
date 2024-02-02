def reverse_array(arr):
    if len(arr) <= 1:
      return arr  # Base case: an array with 0 or 1 element is already reversed

    # Recursive step: reverse the subarray excluding the first element,
    # then append the first element at the end.
    # arr[i:] = [4,3,2,1] + arr[0] = [5] => [4,3,2,1,5]
    return reverse_array(arr[1:]) + [arr[0]]

# Example usage:
original_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(original_array)
print(reversed_array)  # Output: [5, 4, 3, 2, 1]


def reverse_array_recursive(arr, left, right):
    if left >= right:
      return  # Base case: nothing to reverse
    
    # Swap the elements at the left and right indices
    arr[left], arr[right] = arr[right], arr[left]

    # Recursive step: move the left index forward and the right index backward
    # Return not needed it seems
    return reverse_array_recursive(arr, left + 1, right - 1)

# Example usage:
original_array = [1, 2, 3, 4, 5]
reverse_array_recursive(original_array, 0, len(original_array) - 1)
print(original_array)  # Output: [5, 4, 3, 2, 1]
