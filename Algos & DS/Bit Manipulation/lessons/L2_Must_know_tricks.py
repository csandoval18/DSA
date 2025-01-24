# 1. Swap 2 Numbers

'''
a = 5
b = 6

Without bit manipulation this is usually done using a third temporary variable:
tmp = a
a = b
b = tmp

To do this without using a temp variable, we can use the XOR operator

XOR:
- Even num of 1's = 0
- Odd num of 1's = 1

Steps:
1. a = a ^ b
2. b = a ^ b   turns into =>  b = (a ^ b) ^ b = a (b's cancel each other)
3. a = a ^ b   =>   (a ^ b) ^ b a = b
'''



# 2. Check if the i'th bit is set on not

'''
- 2 Methods using the left and right SHIFT operators. (<<, >>)


Using Left SHIFT (<<)

 3  2  1  0
(1, 1, 0, 1) 

Steps:
1. Left SHIFT of 1 by i => (1 << i)
2. Use AND operator with result

- Set Case:

n = 13, i = 2

1 1 0 1
..1 0 0 &
--------
0 1 0 0 => i (2) is set

  
N & (1 << i) != 0:
  i => set
else:
  i => not set


- Unset Case:

n = 13, i = 1

1 1 0 1
1 0 1 0 &
-------
0 0 0 0  => i'th bit unset


Using Right SHIFT (>>)

1. Right SHIFT by i (ignore superpositioned bits)
2. Perform AND between resulting right SHIFT and 1 
3. If the result of the AND opeartion is 1 then the i'th bit is set, else it is unset

- Set Case:

n = 13, i = 2

13 >> 2

1 1 0 1 
0 0 1 1 | 0 1

0 0 1 1 &   Do AND with 1
      1
-------
0 0 0 1 = 1 

If the resultant is = 1, then the number is set, else it is unset


- Unset Case:

n = 13, i = 1

1 1 0 1         13 >> 1
0 1 1 0 | 1

0 1 1 0 &
0 0 0 1
-------
0 0 0 0  = 0

if (N >> i) & 1 == 0:
  i'th bit is unset
else:
  i'th bit is set

'''



# 3. Set the i'th bit

'''
Steps:
1. Left SHIFT 1 by i => (1 << i)
2. Perform  => n OR (left SHIFT result)


- Bit needs to be set case:

n = 9, i = 2

What needs to occur
i = 3 2 1 0    3 2 1 0
    1 0 0 1 => 1 1 0 1
    
1 << 2

0 0 0 1 << 2 = 0 1 0 0

9 OR (0100)

1 0 0 1 |
0 1 0 0
---------
1 1 0 1 = 13

Formula: N | (1 << i)

----------------------------------------------


Bit already set case:

n = 13, i = 2

0 0 0 1 << 2 = 0 1 0 0 

1 1 0 1 |
0 1 0 0
-------
1 1 0 1 = 13

'''



# 4. Clear the i'th bit 

'''
n = 13, i = 2

1 1 0 1

Observation:

So the bit in index 2 has to be set to 0. 

n = 13, i = 2

* If we add ones to every number but the i'th index and use an AND operator the i'th bit is flipped off

1 1 0 1 &
1 0 1 1 
-------
1 0 0 1 => Solution 

Steps:
- Start with 1, it must be moved to the i'th bit to be switch off
- Left SHIFT by 1 by i positions to get the i'th bit 'selected'
- Instead of using an AND operator a NOT operator can be used to switch all 0's => 1's and all 1's to 0's

n & ¬(1 << i)

1 << i
0 0 0 1
0 1 0 0

¬(1 << i)
0 1 0 0
1 0 1 1

n & ¬(1 << i)
1 1 0 1 &
1 0 1 1
-------
1 0 0 1
'''



# 5. Toggle the i'th bit

'''
1. Left shit 1 by i
2. n ^ (1 << i)

n = 13, i = 1

1 << i
0 0 0 1
0 0 1 0

13 ^ (1 << i)
1 1 0 1 ^
0 0 1 0 
-------
1 1 1 1
'''



# 6. Remove the last set bit (rightmost)
'''
n = 12

Examples:

  |
  V
1 1 0 0

1 1 0 0
1 0 0 0 => res

_________________

n = 13

1 1 0 1
1 1 0 0

_________________

n = 16

1 0 0 0 0
0 0 0 0 0

Observation:

n = 16
1 0 0 0 0 

n = 15
0 1 1 1 1

_________________

n = 40
1 0 1 0 0 0

n = 39
1 0 0 1 1 1

_________________

n = 84
1 0 1 0 1 0 0

n = 83
1 0 1 0 0 1 1

Notice how  when we go from (n to n-1), we set the right-most set bit to 0 and every other bit to the right is flipped on

* Formula: n & n-1

Example:

n = 40

1 0 1 0 0 0 &
1 0 0 1 1 1
-----------
1 0 0 0 0 0

n = 84

1 0 1 0 1 0 0 &
1 0 1 0 0 1 1
-------------
1 0 1 0 0 0 0

As shown, the formula N & N-1 flips the right-most set bit
'''



# 7. Check if the number is a power of 2

'''
if n & n-1 == 0:
  True
else:
  False

N & N-1
1 1 0 1 &
1 1 0 0 
-------
1 1 0 0 != 0 => False

1 0 0 0 0 &
0 1 1 1 1
---------
0 0 0 0 0 = 0 => True
'''


# 8. Count the number of set bits

'''
n = 16
1 0 0 0 0 => 1

n = 13
1 1 0 1 => 3

Sol:
13 / 2 = 6 rem 1
 6 / 2 = 3 rem 0 
 3 / 2 = 1 rem 1 
 
 def countSetBits(n: int) -> int:
  cnt = 0
  
  while n > 1:
    if n % 2 == 1:
      cnt += 1
    n //= 2
    
  if n == 1:
    cnt += 1
  return cnt

* Remember: An odd number's right-most bit will always bet 1

=> First Method:

def countSetBitsOperators(n: int) -> int:
  cnt = 0
  
  while n > 1:
    cnt += n & 1
    n = n >> 1
  
  if n == 1:
    cnt += 1
  return cnt

=> Second Method:

def countSetBitsOperators(n: int) -> int:
  cnt = 0 
 
  while n != 0:
    n = n & (n-1)
    cnt += 1
  return cnt
'''

def cntSetBits1(n: int) -> int:
  cnt = 0
  
  while n > 0:
    cnt += n & 1 # Check if the rightmost bit is set (number is uneven)
    n = n >> 1 # Divide by 2
  return cnt
  
def cntSetBits2(n: int) -> int:
  cnt = 0
  
  while n != 0:
    n = n & (n-1)
    cnt += 1
  return cnt
  
n = 13 
# Output: 3
print(cntSetBits1(n))
print(cntSetBits2(n))