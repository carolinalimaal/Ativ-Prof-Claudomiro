memory = ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']

def write(address, data):
    memory[address] = data
    print()

def read(address):
    print(memory[address])
    print()

def showAll():
    print('TODOS OS ENDEREÇOS: ')
    for i in range(0, len(memory)):
        print(memory[i])
    print()

address = 0
add = 0
data = 0

while True:
    operacao = input("""[W] GRAVAR
[R] LER
[L] LISTAR TODA A MEMÓRIA
[ ] SAIR
ESCOLHA UMA OPÇÃO:  """)
    print()
    if operacao in 'Ww':
        address = input('INSIRA O ENDEREÇO DE 4 BITS: ')
        address = int(address, 2)
        data = input('INSIRA O DADO DE 8 BITS: ')
        memory[address] = data 
        write(address, data)

    elif operacao in 'Rr':
        address = input('INSIRA O ENDEREÇO DE 4 BITS: ')
        address = int(address, 2)
        read(address)

    elif operacao in 'Ll':
        showAll()
    else:
        print('FECHANDO...')
        break
