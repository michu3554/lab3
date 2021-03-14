import math

# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

A = [1 - x for x in range(1, 11, 1)]
print(A)

B = [4 ** i for i in range(8)]
print(B)

C = [x for x in B if x % 2 == 0]
print(C)
