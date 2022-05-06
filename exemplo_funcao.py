from pyrsistent import b


def divisao(a, b):
    return a // b, a % b

res = divisao(5,3)
print(res)