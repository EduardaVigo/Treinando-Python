from typing import MutableMapping
from pyrsistent import b


def divisao(a, b):
    return a // b, a % b

def mmc(a, b):
    mutiplo = a
    while mutiplo % a != 0 and mutiplo % b !=0:
        mutiplo = mutiplo + 1

    return mutiplo

print(mmc(28, 16))

res = divisao(5,3)
print(res)