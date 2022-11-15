# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
# posiadał nieparzystą liczbę jedynek.
import random

def usuwanie(T):
    n = len(T)
    counter1 = 0
    counter2 = 0
    for x1 in range(n-2):
        for x2 in range(x1 + 1, n):
            for y in range(n):
                T1 = [[True] * n for _ in range(n)]
                for i in range(n):
                    T1[i][x1] = False
                    T1[i][x2] = False
                    T1[y][i] = False
                for y in range(n):
                    for x in range(n):
                        if T1[y][x]:
                            counter1 += 1
                            if czy_dwojki(T[y][x]):
                                counter2 += 1
                if counter1 == counter2:
                    print(T1)
                    return True
    return False

def czy_dwojki(n):
    counter = 0
    while n > 0:
        a = n % 2
        if a == 1:
            counter += 1
        n //= 2
    return counter % 2 == 1


T = [[random.randint(0,20) for _ in range(3)] for _ in range(3)]
print(T)
print(usuwanie(T))

for i in range(3, 3):
    print(i)