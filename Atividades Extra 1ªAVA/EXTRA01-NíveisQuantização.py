import math
import itertools
nivel = int(input('Insira o número de níveis de quantização: '))
bits = int(math.log2(nivel))
print(f'O número de bits necessários para {nivel} níveis é: {bits} bits')

print(f'Todas as combinações de {bits} bits são:')
geradorComb = itertools.product((0, 1), repeat=bits)
for comb in geradorComb:
    print(comb)
