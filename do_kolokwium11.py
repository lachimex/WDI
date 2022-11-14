# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu rosnącego


def ex09(t):
    n = len(t)
    longest = 0
    ctr = 1
    for i in range(n-1):
        if t[i+1] - t[i] > 0:
            ctr += 1
            longest = max(longest, ctr)
        else:
            ctr = 1
    return longest


t = [1, 2, 4, 5, 6, 3, 4, 9, 43, 45, 47]

print(ex09(t))