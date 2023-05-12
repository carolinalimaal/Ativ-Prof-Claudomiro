import math
tipo = input("""[1] Decimal -> Binário
[2] Binário -> Decimal
Escolha um conversor: """)
if tipo == '1':
    number = float(input('Digite um número fracionário no sistema decimal: '))
    floatpart, intpart = math.modf(number)
    int_bin_digits = []
    quo = 1
    while quo >= 1:
        Resto = intpart % 2
        int_bin_digits.insert(0, Resto)
        quo = intpart // 2
        intpart = quo
    bin_int = ''.join([str(int(x)) for x in int_bin_digits])
    floatbinarydigits = []
    prod = floatpart
    while prod <= 1:
        prod *= 2
        if prod >= 1:
            floatbinarydigits.append(1)
            prod -= 1
        else:
            floatbinarydigits.append(0)
        if prod == 0:
            break
    binaryfloat = ''.join([str(int(x)) for x in floatbinarydigits])
    finalbinary = bin_int + '.' + binaryfloat
    print(f'O número {number} no sistema binário é: {finalbinary}')

elif tipo == '2':
    number = input('Digite um número fracionário no sistema binário: ')
    intpart, floatpart = number.split('.')
    int_decimal_digits = list(intpart)
    n = len(int_decimal_digits)
    exp1 = 0
    decimalint = 0
    while n > 0:
        prod1 = int(int_decimal_digits[n-1]) * 2**exp1
        n -= 1
        exp1 += 1
        decimalint += prod1
    float_decimal_digits = list(floatpart)
    m = len(float_decimal_digits)
    decimalfloat = 0
    while m > 0:
        prod2 = int(float_decimal_digits[m-1]) * 2**(-m)
        m -= 1
        decimalfloat += prod2
    print(f'O número {number} no sistema decimal é: {decimalint + decimalfloat}')
else:
    print('RESPOSTA INVÁLIDA')
