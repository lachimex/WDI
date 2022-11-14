# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu geometrycznego.


def ex11(t):
    n = len(t)
    ctr = 1
    longest = 0
    q = t[1] / t[0]
    for i in range(n-1):
        if t[i+1] / t[i] == q:
           ctr += 1
           longest = max(ctr, longest)
        else:
            q = t[i+1]/t[i]
            i -= 1
            ctr = 1
    return longest


t = [2, 3, 9, 22, 3, 4, 5, 6]
print(ex11(t))