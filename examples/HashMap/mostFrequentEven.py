def mostFrequentEven(nums):
  even_count = {}  # A dictionary to store the count of even elements

  # Iterate through the array and count even elements
  for num in nums:
    if num % 2 == 0:
      even_count[num] = even_count.get(num, 0) + 1

  max_count = 0  # Initialize the maximum count
  most_frequent_even = float('inf')  # Initialize the most frequent even element to positive infinity

  # Iterate through the even_count dictionary to find the most frequent even element
  for num, count in even_count.items():
    if count > max_count or (count == max_count and num < most_frequent_even):
      max_count = count
      most_frequent_even = num

  return most_frequent_even


# Example usage:
nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
result = mostFrequentEven(nums)
print(result)  # Output: 4