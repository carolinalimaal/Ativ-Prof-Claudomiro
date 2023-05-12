a = int(input('Digite [1] ou [0]: '))
b = int(input('Digite [1] ou [0]: '))
c = int(input('Digite [1] ou [0]: '))

if a == 1 and b == 1:
    print('Existe um número par de chaves fechadas.')
elif a == 1 and c == 1:
    print('Existe um número par de chaves fechadas.') 
elif b == 1 and c == 1:
    print('Existe um número par de chaves fechadas.') 
else:
    print('Não existe um número par de chaves fechadas.')