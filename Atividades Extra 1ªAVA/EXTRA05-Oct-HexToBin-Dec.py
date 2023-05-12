tipo = input("""[1] Octal -> binário e decimal
[2] Hexadecimal -> binário e decimal
[3] Binário -> Octal
[4] Binário -> Hexadecimal
Escolha um conversor: """)

if tipo == '1':
    oct_num = input('Digite um número na base octal: ')
    oct_bin = {'0':'000', '1':'001', '2':'010', '3':'011','4':'100','5':'101','6':'110','7':'111'}
    bin_num = ''
    for digit in oct_num:
        bin_num += oct_bin[digit]
    binary = list(bin_num)
    n = len(binary)
    exp, decimal = 0, 0
    while n > 0:
        decimal += int(binary[n-1]) * 2**exp
        n -= 1
        exp += 1
    print(f"""OCTAL -> BINÁRIO: {bin_num}
BINÁRIO -> DECIMAL: {decimal}""")

elif tipo == '2':
    hex_num = input('Digite um número na base hexadecimal: ')
    hex_bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','a':'1010','B':'1011','b':'1011','C':'1100','c':'1100','D':'1101','d':'1101','E':'1110','e':'1110','F':'1111','f':'1111'}
    bin_num = ''
    for digit in hex_num:
        bin_num += hex_bin[digit]
    binary = list(bin_num)
    n = len(binary)
    exp, decimal = 0, 0
    while n > 0:
        decimal += int(binary[n-1]) * 2**exp
        exp += 1
        n -= 1
    print(f"""HEXADECIMAL -> BINÁRIO: {bin_num}
BINÁRIO -> DECIMAL: {decimal}""")

elif tipo == '3':
    bin_num = input('Digite um número na base binária: ')
    while len(bin_num) % 3 != 0:
        bin_num = '0' + bin_num 
    agrupamento = [bin_num[i:i+3] for i in range(0, len(bin_num), 3)]
    bin_oct = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
    oct_num = ''
    for grupo in agrupamento:
        oct_num += bin_oct[grupo]
    print(f'BINÁRIO -> OCTAL: {oct_num}')

elif tipo == '4':
    bin_num = input('Digite um número na base binária: ')
    while len(bin_num) % 4 != 0:
        bin_num = '0' + bin_num
    agrupamento = [bin_num[i:i+4] for i in range(0, len(bin_num), 4)]
    bin_num = bin_num.upper
    bin_hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    hex_num = ''
    for grupo in agrupamento:
        hex_num += bin_hex[grupo]
    print(f'BINÁRIO -> HEXADECIMAL: {hex_num}')