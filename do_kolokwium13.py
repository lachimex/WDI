def ex12(arr):
    n, i, d = len(arr), 0, 0
    if n == 1:
        return 0
    solutioni, solutiond = 0, 0
    for x in range(1, n-1):
        k = arr[x] - arr[x-1]
        if k > 0:
            if arr[x+1] - arr[x] == k:
                i += 1
            else:
                solutioni = max(solutioni, i+1)
                i, d = 1, 1
        else:
            if arr[x+1] - arr[x] == k:
                d += 1
            else:
                solutiond = max(solutiond, d+1)
                i, d = 1, 1
    solutioni = max(solutioni, i)
    solutiond = max(solutiond, d)
    if solutioni == 0:
        return max(solutiond, d+2)
    elif solutiond == 0:
        return max(solutioni, i+2)
    else:
        solutioni += 1
        solutiond += 1
    return solutioni - solutiond


t = [1, 3, 7, 2, 4]


print(ex12(t))