'''
* Function ord()
  The ord() function gives the number order of a character based on its
  Unicode code point. This can be thought of as its unique identifier in the Unicode
  system, which is a standardized way to represent text characters.

For example:
- For lowercase English letters, the order starts at 'a' (97) and goes to 'z' (122).
- For uppercase English letters, it starts with 'A' (65) and goes to 'Z' (90)
- For digits, it starts with '0' (48) and goes to '9' (57).
'''

# Use cases:

# 1. Get the Unicode Code Point of a Character
# print(ord('a'))  # Output: 97
# print(ord('z'))  # Output: 122
# print(ord('A'))  # Output: 65
# print(ord('1'))  # Output: 49
# print(ord('$'))  # Output: 36

# 2. Difference Between Characters
# print(ord('b') - ord('a'))  # Output: 1
# print(ord('z') - ord('a'))  # Output: 25

# 3. Non-ASCII Characters
# # print(ord('ñ'))   # Output: 241
# print(ord('😀'))  # Output: 128512

'''
* Function chr()
  The chr()
'''