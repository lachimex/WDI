# Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory cyfr
# występujące w liczbie są identyczne. Na przykład:
# 13 = 31 i 23 = 113
# 18 = 102 i 33 = 201
# 107 = 1223 i 57 = 321
# Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca
# długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.

def zamiana_4(n):
    liczba = 0
    i = 0
    while n > 0:
        liczba += (n % 4) * 10**i
        i += 1
        n //= 4
    return liczba

def cztero_zgodne(a, b):
    a_4 = zamiana_4(a)
    b_4 = zamiana_4(b)
    t1 = [False] * 4
    t2 = [False] * 4
    while a_4 != 0:
        t1[a_4 % 10] = True
        a_4 //= 10
    while b_4 != 0:
        t2[b_4 % 10] = True
        b_4 //= 10
    return t1 == t2


def zadanie(t):
    n = len(t)
    counter = 1
    longest = 0
    for i in range(n):
        for j in range(i + 1, n):
            if cztero_zgodne(t[i], t[j]):
                counter += 1
        longest = max(longest, counter)
        counter = 1
    return longest


t = [13, 24, 53, 25] #[31, 120, 121]
print(zadanie(t))