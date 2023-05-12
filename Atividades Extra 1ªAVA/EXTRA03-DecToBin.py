num_decimal = int(input('Digite um número na base decimal: '))
num_decimal_reserva = num_decimal
num_binary = ''
while num_decimal > 0:
    num_binary = str(num_decimal % 2) + num_binary
    num_decimal //= 2
print(f'O número {num_decimal_reserva} na base decimal é equivalente a {num_binary} na base binária.')
