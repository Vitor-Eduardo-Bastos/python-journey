# Lista que armazenará todas as pessoas cadastradas
pessoas = []

while True:
    print(f'{"=" * 15} CADASTRO DE PESSOAS {"=" * 15}')

    # Entrada de dados
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()

    # Validação do sexo
    while sexo != 'M' and sexo != 'F':
        sexo = input('ERRO! Digite somente M ou F: ').strip().upper()

    idade = int(input('Digite sua idade: '))

    print()

    continuacao = input('Deseja continuar? [S/N]: ').strip().upper()

    # Validação da continuação
    while continuacao != 'S' and continuacao != 'N':
        continuacao = input('ERRO! Digite somente S ou N: ').strip().upper()

    # Criação do dicionário da pessoa
    pessoa = {
        'Nome': nome,
        'Sexo': sexo,
        'Idade': idade
    }

    # Adiciona a pessoa à lista principal
    pessoas.append(pessoa)

    # Encerra o cadastro
    if continuacao == 'N':
        break

# Exibe a quantidade total de pessoas cadastradas
print()
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')

# Calcula a média das idades
total_idade = 0

for pessoa in pessoas:
    total_idade += pessoa['Idade']

media = total_idade / len(pessoas)

print(f'A média de idade das pessoas cadastradas é de {media:.1f} anos.\n')

# Lista de mulheres cadastradas
mulheres_cadastradas = []

for pessoa in pessoas:
    if pessoa['Sexo'] == 'F':
        mulheres_cadastradas.append(pessoa['Nome'])

print(f'Tivemos {len(mulheres_cadastradas)} mulheres cadastradas:')

for nome in mulheres_cadastradas:
    print(f'• {nome}')

# Lista de pessoas acima da média de idade
print()

acima_media = []

for pessoa in pessoas:
    if pessoa['Idade'] > media:
        acima_media.append(pessoa['Nome'])

print(f'Tivemos {len(acima_media)} pessoas acima da média de idade:')

for nome in acima_media:
    print(f'• {nome}')
