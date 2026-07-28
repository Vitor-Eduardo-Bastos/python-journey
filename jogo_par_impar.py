import random

vitorias = 0

print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 30)

while True:
    num_jogador = int(input('Digite um número: '))

    escolha = input('PAR OU ÍMPAR? [P/I]: ').strip().upper()

    while escolha not in ['P', 'I']:
        print('Escolha inválida! Digite apenas P ou I.')
        escolha = input('PAR OU ÍMPAR? [P/I]: ').strip().upper()

    print('=' * 50)

    num_maquina = random.randint(0, 10)
    soma = num_jogador + num_maquina

    print(f'Você jogou {num_jogador} e a máquina jogou {num_maquina}.')

    if soma % 2 == 0:
        print(f'A soma foi {soma}. Resultado: PAR.')
    else:
        print(f'A soma foi {soma}. Resultado: ÍMPAR.')

    print('=' * 50)
    
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você ganhou esta rodada!')
            vitorias += 1
        else:
            print('Você perdeu esta rodada!')
            break

    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você ganhou esta rodada!')
            vitorias += 1
        else:
            print('Você perdeu esta rodada!')
            break

    print('=' * 50)

print(f'Fim de jogo! Você conquistou {vitorias} vitória(s) consecutiva(s).')
