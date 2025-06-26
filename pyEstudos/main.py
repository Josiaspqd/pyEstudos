import time
import math


def Soma():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite outro número:'))
    soma = num1 + num2
    print(f'A soma entre {num1} + {num2} é igual a: {soma}')


def Subtracao():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite outro número:'))
    soma = num1 - num2
    print(f'A soma entre {num1} - {num2} é igual a: {soma}')

def Multiplicação():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite outro número:'))
    soma = num1 * num2
    print(f'A Multiplicação entre {num1} * {num2} é igual a: {soma}')



def Divisão():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite outro número:'))
    div = num1 / num2
    print(f'A Divisão entre {num1} / {num2} é igual a {div}')


def RaizQuadrada():
    num1 = int(input('Digite um número:'))
    raiz = math.sqrt(num1)
    print(f'A Raiz Quadrada de {num1} é: {raiz}')




def Fibonacci():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite outro número:'))
    soma = num1 + num2
    print(f'A soma entre {num1} + {num2} é igual a {soma}')





while True:
    print('**Calculadora**')
    print('1 - Soma:')
    print('2 - Multiplicação:')
    print('3 - Divisão:')
    print('4 - Subtração:')
    print('5 - Raiz Quadrada:')

    opcao = int(input('Selecione uma opção:'))
    if opcao == 1:
        Soma()
        time.sleep(3)
        print('_________________________________________________')
    elif opcao == 2 :
        Multiplicação()
        time.sleep(3)
        print('_________________________________________________')
    elif opcao == 3:
        Divisão()
        time.sleep(3)
        print('_________________________________________________')
    elif opcao == 4:
        Subtracao()
        time.sleep(3)
        print('_________________________________________________')
    elif opcao == 5:
        RaizQuadrada()
        time.sleep(3)
        print('_________________________________________________')

    


