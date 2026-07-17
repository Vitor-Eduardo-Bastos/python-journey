import time

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

escolha = 0

while escolha != 5:
    print('=' * 30)
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] COMPARAR NÚMEROS
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')
    print('=' * 30)

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        soma = n1 + n2
        print(f'Resultado da soma = {soma}')

    elif escolha == 2:
        multiplicacao = n1 * n2
        print(f'Resultado da multiplicação = {multiplicacao}')

    elif escolha == 3:
        if n1 > n2:
            print(f'O primeiro valor é maior que o segundo: {n1} > {n2}')
        elif n1 < n2:
            print(f'O segundo valor é maior que o primeiro: {n2} > {n1}')
        else:
            print(f'Os dois números são iguais: {n1} = {n2}')

    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    else:
        print('Opção inválida. Digite novamente.')

print('Finalizando...')
time.sleep(2)
print('Encerrado')
