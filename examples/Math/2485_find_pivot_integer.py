    def pivotInteger(self, n: int) -> int:
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
            if pref == suff and l < r:
                while l<r:
                    pref += arr[l]
                    suff += arr[r]
                    l += 1
                    r -= 1
                break
            
            if pref == suff:
                break

        if pref == suff:            
            return l
        else:
            return -1