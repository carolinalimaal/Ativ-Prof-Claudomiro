#Exercício eletrocálvulas
while True:
    botao = int(input("""Botão
[1] ON
[0] OFF
Escolha uma opção: """))
    sensor = int(input("Informe o estado atual do sensor de nível máximo: "))
    print('----------------------------------')

    
    if botao == 1 and sensor == 0:
        print("""Eletroválvula de entrada de líquido está ativa.
Tanque está enchendo...""")
        print('----------------------------------\n')
    elif botao == 1 and sensor == 1:
        print('O tanque está no seu nível máximo. Eletroválvula de entrada de líquido foi desativada.')
        print('----------------------------------\n')
    elif botao == 0 and sensor == 1:
        print("""O tanque está no seu nível máximo. Eletroválvula de escoamento de líquido está ativa.
Tanque está esvaziando...""")
        print('----------------------------------\n')
    else: 
        print("""O tanque não está mais no seu nível máximo. Eletroválvula de escoamento de líquido está ativa.
Tanque está esvaziando...""")
        print('----------------------------------\n')
