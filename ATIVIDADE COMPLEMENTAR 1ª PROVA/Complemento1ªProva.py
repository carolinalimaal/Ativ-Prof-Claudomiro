def and_gate(input1, input2):
    if input1 == 1 and input2 == 1:
        return 1
    else:
        return 0

def and_gate3(input1, input2, input3):
    if input1 == 1 and input2 == 1 and input3 == 1:
        return 1
    else:
        return 0
    
def or_gate(input1, input2):
    if input1 == 0 and input2 == 0:
        return 0
    else:
        return 1
    
def not_gate(input):
    if input == 1:
        return 0
    else:
        return 1

def xor_gate(input1, input2):
    if input1 != input2:
        return 1
    else:
        return 0

def somador_subtrator(B,A):
    if select_key == 1:
        invA = 1
    else:
        invA = 0
    and1 = and_gate3(and_gate(F1, F2), A, B)
    xor1 = xor_gate(B,A)
    and2 = and_gate3(and_gate(F1, F2), xor1, select_key)
    xor2 = xor_gate(select_key, xor1) 
    carry = or_gate(and1, and2)  
    sum = and_gate(xor2, and_gate(F1, F2))
    print(f'RESULTADO: {sum}')
    print(f'VAI-UM: {carry}')


#Teste porta AND = 0 mata a porta
print('AND 00 ->', and_gate(0,0))
print('AND 01 ->', and_gate(0,1))
print('AND 10 ->', and_gate(1,0))
print('AND 11 ->', and_gate(1,1),'\n')

#Teste porta OR = 1 ativa a porta
print('OR 00 ->', or_gate(0,0))
print('OR 01 ->', or_gate(0,1))
print('OR 10 ->', or_gate(1,0))
print('OR 11 ->', or_gate(1,1),'\n')

#Teste porta NOT
print('NOT 0 ->', not_gate(0))
print('NOT 1 ->', not_gate(1),'\n')

#Teste porta XOR = entradas diferentes ativam a porta
print('XOR 00 ->', xor_gate(0,0))
print('XOR 01 ->', xor_gate(0,1))
print('XOR 10 ->', xor_gate(1,0))
print('XOR 11 ->', xor_gate(1,1),'\n')

#Entradas Decodificador (F1 F2)
print("""OPERAÇÕES DISPONÍVEIS:
[00] LÓGICA AND
[01] LÓGICA OR
[10] LÓGICA NOT
[11] SOMADOR/SUBTRATOR:""")
F1, F2 = int(input('F1: ')),  int(input('F2: '))

#Saídas Decodificador
if and_gate(not_gate(F1), not_gate(F2)): 
    A, B, invA  = int(input('A: ')), int(input('B: ')), int(input('INV-A: ')) # Entradas para operações:
    if invA == 1: #Configuração INV A
        A = not_gate(A)
    print(and_gate(A,B))

if and_gate(not_gate(F1), F2):
    A, B, invA  = int(input('A: ')), int(input('B: ')), int(input('INV-A: ')) # Entradas para operações:
    if invA == 1: #Configuração INV A
        A = not_gate(A)
    print(or_gate(A,B))

if and_gate(F1, not_gate(F2)):
    B = int(input('B: ')) # Entradas para operações:
    print(not_gate(B))

if and_gate(F1, F2):
    select_key = int(input('SELECT_KEY [0]SOMA [1]SUBTRAÇÃO: ')) #Vem-um funciona como o seletor de soma/subtração
    A, B, invA  = int(input('A: ')), int(input('B: ')), int(input('INV-A: ')) # Entradas para operações:
    if invA == 1: #Configuração INV A
        A = not_gate(A)
    somador_subtrator(B, A)
