# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.


def ex10(t):
    n = len(t)
    r = t[1] - t[0]
    ctr = 1
    longest = 0
    for i in range(n-1):
        if t[i+1] - t[i] == r:
            ctr += 1
            longest = max(longest, ctr)
        else:
            r = t[i+1] - t[i]
            i -= 1
            ctr = 1
    return longest


t = [7, 6, 7, 9, 3, 4, 8, 2, 15]
print(ex10(t))