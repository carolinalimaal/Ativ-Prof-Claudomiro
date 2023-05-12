memory = ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']

def write(address, data): #Função que define a operação de escrita.
    memory[address] = data #Vai colocar o dado informado no index da lista de acordo com o endereço informado.
    print()

def read(address): #Função que define a operação de leitura.
    print(memory[address]) #Vai buscar o dado que tiver no endereço informado. 
    print()

def showAll(): #Função que define a listagem de todas as células dessa memória  
    print('TODOS OS ENDEREÇOS: ')
    for i in range(0, len(memory)): #Vai percorrer a lista do 1º até o último index dela, obtido pelo 'len(memory)' 
        print(memory[i])
    print()

address = 0
add = 0
data = 0

while True: 
    operacao = input("""[W] GRAVAR 
[R] LER
[L] LISTAR TODA A MEMÓRIA
[S] SAIR
ESCOLHA UMA OPÇÃO:  """)
    print()
    if operacao in 'Ww':
        address = input('INSIRA O ENDEREÇO DE 4 BITS: ')
        address = int(address, 2) #Para tranformar o valor de bnário para decimal 
        data = input('INSIRA O DADO DE 8 BITS: ')
        memory[address] = data #Vai armazenar o novo dado sobre ou antigo
        write(address, data)

    elif operacao in 'Rr':
        address = input('INSIRA O ENDEREÇO DE 4 BITS: ')
        address = int(address, 2) #Para transformaum valor de binário para decimal
        read(address)

    elif operacao in 'Ll':
        showAll()
    else:
        print('FECHANDO...')
        break
