import time

# Lista principal que armazenará todos os alunos cadastrados
alunos = []

# Lista auxiliar para armazenar os dados de cada aluno
dado = []

while True:
    print('=' * 15, 'SISTEMA DE BOLETIM', '=' * 15)
    print()

    # Entrada de dados do aluno
    nome = input('Nome do aluno: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))

    # Cálculo da média
    media = (n1 + n2) / 2

    # Adiciona os dados do aluno à lista auxiliar
    dado.append(nome)
    dado.append(n1)
    dado.append(n2)
    dado.append(media)

    # Cria uma cópia da lista auxiliar e armazena na lista principal
    alunos.append(dado[:])

    # Limpa a lista auxiliar para receber os dados do próximo aluno
    dado.clear()

    print()

    # Pergunta se o usuário deseja continuar cadastrando alunos
    continuacao = input('Deseja cadastrar outro aluno? [S/N]: ').strip().upper()

    # Validação da resposta
    while continuacao != 'S' and continuacao != 'N':
        continuacao = input('Entrada inválida. Digite apenas S ou N: ').strip().upper()

    # Encerra os cadastros se o usuário escolher "N"
    if continuacao == 'N':
        break

# Exibição do boletim geral
print()
print('=' * 40)
print('BOLETIM GERAL')
print('=' * 40)

print(f'{"No.":<4}{"NOME":<15}{"MÉDIA"}')

# Mostra a posição, o nome e a média de cada aluno
for pos, aluno in enumerate(alunos):
    print(f'{pos:<4}{aluno[0]:<15}{aluno[3]:.2f}')

# Consulta individual das notas
while True:
    print()

    opc = input(
        'Digite o número do aluno para visualizar suas notas '
        '(ou PARE para encerrar): '
    ).strip().upper()

    # Encerra a consulta
    if opc == 'PARE':
        break

    # Converte a posição digitada para inteiro
    opc = int(opc)

    # Mostra as notas do aluno escolhido
    print(f'\nAluno: {alunos[opc][0]}')
    print(f'Primeira nota: {alunos[opc][1]}')
    print(f'Segunda nota: {alunos[opc][2]}')

# Mensagem de encerramento
print()
print('Encerrando o sistema...')
time.sleep(2)
print('Sistema finalizado com sucesso.')
