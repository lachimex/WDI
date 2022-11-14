# Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie innego napisu o długości
# co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest tablica
# T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
T = ["AAAB", "ABCABC", "ABAABA"]


def isMulti(napis):
    n = len(napis)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            kandydat = napis[:i]
            for j in range(0, n, i):
                kandydat2 = napis[j:j + i]
                if kandydat2 != kandydat:
                    break
            else:
                return True


def multi(T):
    longest = 0
    for napis in T:
        if isMulti(napis):
            longest = max(longest, len(napis))
    return longest


print(multi(T))