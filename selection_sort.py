#selection sort
def selection_sort(t):
    n = len(t)
    for i in range(n):
        min = i
        for j in range(i, n):
            if t[j] < t[min]:
                min = j
        t[i], t[min] = t[min], t[i]
    return t


t = [4, 3, 7, 3, 12, 4, 23]
print(selection_sort(t))
