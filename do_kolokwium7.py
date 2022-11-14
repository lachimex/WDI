import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def tab_liczba(x):
    n = int(math.log10(x)) + 1
    t = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        t[i] = x % 10
        x //= 10
    return t


def rotacja(t):
    a = t[0]
    for i in range(1, len(t)):
        t[i-1] = t[i]
    t[-1] = a
    return t


print(rotacja([0, 9, 2]))

def zadanie(n):
    length = int(math.log10(n)) + 1
    n = tab_liczba(n)
    for b in range(2, 17):
        for i in range(length):
            iloczyn = 1
            n = rotacja(n)
            n_copy = 0
            for j in range(len(n)):
                n_copy *= 10
                n_copy += n[j]
            while n_copy != 0:
                iloczyn *= n_copy % b
                n_copy //= b
            if is_prime(iloczyn):
                return b
    return None


print(zadanie(209))

