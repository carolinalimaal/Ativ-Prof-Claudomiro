binario = input('Digite um número na base binária: ')
bin_reserva = binario
lista = list(binario)
n = len(lista)
i, decimal = 0, 0
while n > 0:
    prod = int(lista[n-1]) * 2**i
    n -= 1
    i += 1
    decimal += prod
print(f'O número binário {bin_reserva} é igual a {decimal} na base decimal')
