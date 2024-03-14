# Using an arr to keep track of index
def pivotInteger(n: int) -> int:
    arr = [i for i in range(1, n+1)]
    l, r = 1, len(arr)-2
    pref, suff = arr[0], arr[len(arr)-1] 

    while l <= r:
        if pref < suff:
            pref += arr[l]
            l += 1
        if pref > suff:
            suff += arr[r]
            r -= 1
        if pref == suff:
            pref += arr[l]
            suff += arr[r]
            l += 1
            r -= 1
        
    if pref == suff:            
        return l
    else:
        return -1

# Space Optimized
def pivotIntegerSO(n: int) -> int:
    pref, suff = 1, n
    l, r = 2, n-1
    
    while l <= r:
        if pref < suff:
            pref += l
            l += 1
        elif pref > suff:
            suff += r
            r -= 1
        else:
            pref += l
            suff += r
            l += 1
            r -= 1

    if pref == suff:
        return l-1
    else:
        return -1

n = 8
print(pivotInteger(n))
print(pivotIntegerSO(n))