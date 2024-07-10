# Solicita ao usuário que insira um valor inteiro
valor = int(input('Digite o valor para separar: '))

# Inicializa variáveis para armazenar a quantidade de cada denominação
nota100 = valor // 100
valor = valor % 100

nota50 = valor // 50
valor = valor % 50

nota20 = valor // 20
valor = valor % 20

nota10 = valor // 10
valor = valor % 10

nota5 = valor // 5
valor = valor % 5

nota2 = valor // 2
valor = valor % 2

moeda1 = valor

# Exibe a quantidade de cada denominação necessária para compor o valor inserido
print(f'Notas de 100: {nota100}')
print(f'Notas de 50:  {nota50}')
print(f'Notas de 20:  {nota20}')
print(f'Notas de 10:  {nota10}')
print(f'Notas de 5:   {nota5}')
print(f'Notas de 2:   {nota2}')
print(f'Moedas de 1:  {moeda1}')

# Funcionamento do Código
# 1. O valor inserido pelo usuário é dividido sucessivamente pelas denominações de notas e moedas, começando pela maior (100) até a menor (1).
# 2. O operador // (divisão inteira) é utilizado para determinar a quantidade de notas ou moedas de cada denominação.
# 3. O operador % (módulo) é utilizado para calcular o valor restante após a retirada das notas ou moedas da denominação atual.
# 4. Finalmente, o programa exibe a quantidade de cada denominação necessária para compor o valor inserido.
