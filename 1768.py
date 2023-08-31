def mergeAlternately(word1, word2):
  res = ""
  w1Len = len(word1)
  w2Len = len(word2)
  maxLen = max(w1Len, w2Len)
  res = ""
  
  for i in range(maxLen):
    print(i)
    # i in range of both words non inclusive to cut off at last index
    if i < w1Len and i < w2Len:
      res += word1[i]
      res += word2[i]
    # i in range of word1 but past word2
    
    # (i >= w2Len) is the same as (i > w2Len-1) since you need to cut off at the last index not last length #
    elif i < w1Len and i >= w2Len:
    # elif i < w1Len and i > w2Len-1:
      res += word1[i:w1Len]
      return res
    # i in range of word2  but past word1
    elif i < w2Len and i >= w1Len:
      res += word2[i:w2Len]
      return res
  return res
  
word1 = "ab"
word2 = "pqrs"
  
print(mergeAlternately(word1, word2))