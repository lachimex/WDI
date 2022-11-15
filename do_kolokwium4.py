# Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
# M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
# istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
# liczbą spełniającą warunek jest liczba 251.

import math
x = 1202742516

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def generowanie_tablicy(x):
    n = int(math.log10(x))+1
    t = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        t[i] = x%10
        x //= 10
    return t


def rozne_liczby(n):
    t = [False] * 10
    while n != 0:
        if not t[n % 10]:
            t[n % 10] = True
        else:
            return False
        n //= 10
    return True


def obciecie(t):
    n = len(t)
    liczba_max = 0
    for start in range(n):
        for end in range(start + 1, n):
            obciecie = t[start:end]
            liczba = 0
            for j in range(len(obciecie)):
                liczba *= 10
                liczba += obciecie[j]
            if is_prime(liczba) and rozne_liczby(liczba):
                liczba_max = max(liczba_max, liczba)
    return liczba_max



print(obciecie(generowanie_tablicy(x)))