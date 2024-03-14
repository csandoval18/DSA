def subarrayWithSumK(a, b):
    hm = {}
    hm[0] = 1
    cnt = 0

    for i in range(len(a)):
        xr = xr ^ a[i]
        x = xr ^ b
        if x in hm:
            cnt += hm[x]
        hm[xr] = hm.get(xr, 0) + 1
    return cnt