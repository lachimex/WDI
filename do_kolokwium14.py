# Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci indeks
# największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
# mniejszych od niej lub None, jeżeli taka liczba nie istnieje.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def zadanie(t):
    n = len(t)
    greatest = 0
    index_greatest = 0
    for i in range(n):
        iloczyn = 1
        for j in range(i):
            if is_prime(t[j]):
                iloczyn *= t[j]
        if iloczyn == t[i]:
            if t[i] > greatest:
                greatest = t[i]
                index_greatest = i
    if index_greatest != 0:
        return index_greatest
    else:
        return None


t = [1, 2, 3, 4, 7, 4]
print(zadanie(t))