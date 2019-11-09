slowa = ["jabłko", "czeresnia", "maslo", "jajka"]
liczby = [3, 10, 1, 6]
lista_liczb = [1.12, 121.12, 12.0]
print(list(zip(slowa, liczby)))
print(list(zip(slowa, lista_liczb)))

from itertools import zip_longest
print(list(zip_longest(slowa, lista_liczb)))