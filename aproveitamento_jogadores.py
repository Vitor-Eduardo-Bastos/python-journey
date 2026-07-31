import time

# Lista principal que armazenará todos os jogadores
jogadores = []

# Cadastro dos jogadores
while True:
    print(f'{"=" * 15} CADASTRO DE JOGADORES {"=" * 15}')

    nome = input('Qual é o nome do jogador: ')
    partidas = int(input(f' - Quantas partidas {nome} jogou: '))

    # Lista para armazenar os gols de cada partida
    gols = []

    for c in range(1, partidas + 1):
        gols_feitos = int(input(f' - Quantos gols {nome} fez no jogo {c}: '))
        gols.append(gols_feitos)

    total_gols = sum(gols)

    # Dicionário do jogador
    jogador = {
        'Nome': nome,
        'Partidas': partidas,
        'Gols Feitos': gols,
        'Total de Gols': total_gols
    }

    # Adiciona o jogador à lista principal
    jogadores.append(jogador)

    print()

    continuacao = input('Deseja continuar? [S/N]: ').strip().upper()

    while continuacao not in ['S', 'N']:
        continuacao = input(' - ERRO! Digite somente S ou N: ').strip().upper()

    print()

    if continuacao == 'N':
        break


# Exibição da tabela geral
print(f'{"Cód.":<5}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('-' * 50)

for pos, jogador in enumerate(jogadores):
    print(
        f'{pos:<5}'
        f'{jogador["Nome"]:<15}'
        f'{str(jogador["Gols Feitos"]):<20}'
        f'{jogador["Total de Gols"]:<5}'
    )

print()

# Consulta de detalhes de um jogador
while True:
    codigo = input('Mostrar dados de qual jogador? (999 para parar): ').strip()

    if codigo == '999':
        break

    codigo = int(codigo)

    if codigo >= len(jogadores):
        print('ERRO! Não existe jogador com esse código.\n')
    else:
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogadores[codigo]["Nome"]} --')

        for pos, gols in enumerate(jogadores[codigo]['Gols Feitos']):
            print(f'No jogo {pos + 1} fez {gols} gols.')

        print()

# Encerramento do programa
print('ENCERRANDO...')
time.sleep(2)
print('FINALIZADO COM SUCESSO!')
