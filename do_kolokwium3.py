# Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def wycinanie(t1, t2):
    n = len(t1)
    for start in range(n+1):
        for end in range(start+1, n+1):
            t1_wycinek = t1[start:end]
            t2_wycinek = t2[start:end]
            print(t1_wycinek)
            print(t2_wycinek)
            suma = 0
            for element in t1_wycinek:
                suma += element
            for element in t2_wycinek:
                suma += element
            print(suma)
            suma_copy = suma
            for i in range (2, int(suma**0.5)+1):
                if is_prime(i) and suma % i == 0:
                    suma //= i
                    if is_prime(suma):
                        return True
                    else:
                        suma = suma_copy
    return False


t1 = [1, 3, 4]
t2 = [7, 8, 8]


print(wycinanie(t1, t2))