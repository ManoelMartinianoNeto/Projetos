operation = input('''
Por favor digite a operação matemática que você gostaria de executar:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Digite o primeiro numero: '))
number_2 = int(input('Digite o segundo numero: '))

if operation == '+':
    print('{} + {} ='.format(number_1,number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} ='.format(number_1,number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} ='.format(number_1,number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} ='.format(number_1,number_2))
    print(number_1 / number_2)

else:
    print('Você não digitou um operador válido.')
