# Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy,
# przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach
# import random
# n = int(input())
# t = [0] * n
# for i in range(n):
#     a = random.randint(1, 99)
#     while a % 2 == 0:
#         a = random.randint(1, 99)
#     t[i] = a

t = [53, 17, 41, 39, 61, 41, 39, 63, 5, 29]
print(t)


def arytm_dodatnia(t):
    n = len(t)
    longest = 0
    ctr = 1
    r = t[1] - t[0]
    for i in range(n-1):
        if 0 < r == t[i + 1] - t[i]:
            ctr += 1
            longest = max(longest, ctr)
        else:
            r = t[i+1] - t[i]
            ctr = 1
    return longest


def arytm_ujem(t):
    n = len(t)
    longest = 0
    ctr = 1
    r = t[1] - t[0]
    for i in range(n-1):
        if 0 > r == t[i + 1] - t[i]:
            ctr += 1
            longest = max(longest, ctr)
        else:
            r = t[i+1] - t[i]
            i -= 1
            ctr = 1
    return longest


print(arytm_ujem(t))
print(arytm_dodatnia(t))


def ex12(t):
    return arytm_dodatnia(t) - arytm_ujem(t)
print(ex12(t))