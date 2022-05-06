def divisao(a, b):
    return a // b, a % b

def mmc(a, b):
    multiplo = a
    while multiplo % a != 0 or multiplo % b != 0:
        multiplo = multiplo + 1
    
    return multiplo

print(mmc(28, 16))
    
res = divisao(5,3)
print(res)
