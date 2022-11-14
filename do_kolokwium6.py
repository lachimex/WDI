def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True


def zadanie1(t):
    liczba_max = 0
    n = len(t)
    for i in range(n):
        iloczyn = 1
        liczba = t[i]
        for j in range(i-1, -1, -1):
            if is_prime(t[j]):
                iloczyn *= t[j]
        if liczba == iloczyn:
            if liczba > liczba_max:
                index_max = i
                liczba_max = liczba
    if liczba_max == 0:
        return None
    else:
        return index_max


t = [2, 3, 5, 4, 7, 210]
print(zadanie1(t))
