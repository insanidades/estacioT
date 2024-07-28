saida = ''
def adicao(add1, add2):
    return add1 + add2

def subtracao(sub1, sub2):
    return sub1 - sub2

def multiplicacao(mp1, mp2):
    return mp1 * mp2

def divisao(div1, div2):
    if div2 == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return div1 / div2

def calculadora(n1, n2, operacao):
    if operacao in ['+', 'soma']:
        resultado = adicao(n1, n2)
    elif operacao in ['-', 'subtração']:
        resultado = subtracao(n1, n2)
    elif operacao in ['*', 'multiplicação']:
        resultado = multiplicacao(n1, n2)
    elif operacao in ['/', 'divisão']:
        resultado = divisao(n1, n2)
    else:
        return "Operação inválida. Use '+', '-', '*', '/' ou os nomes 'soma', 'subtração', 'multiplicação', 'divisão' para efetuar a operação."

    return resultado

while saida.lower() != 'n':
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação desejada(+, - ...) ou o nome completo como (soma, adicao...) : ')
        resultado = calculadora(n1, n2, operacao)
        print(f'Resultado da operação: {resultado}')

    except ValueError:
        print('Por favor digite entradas válidas.')

    saida = input("Deseja realizar outra operação? (S/N): ")
    if saida.lower() not in ['s', 'n']:
        print("Resposta inválida. Por favor, digite 'S' para continuar ou 'N' para sair.")
