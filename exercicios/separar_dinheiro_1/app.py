## valor 188

valor = int(input('Digite o valor para separar: '))

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

print(f'Notas de 100: {nota100}')
print(f'Notas de 50:  {nota50}')
print(f'Notas de 20:  {nota20}')
print(f'Notas de 10:  {nota10}')
print(f'Notas de 5:   {nota5}')
print(f'Notas de 2:   {nota2}')
print(f'Moedas de 1:  {moeda1}')

# Funcionamento do Código
# O valor inserido pelo usuário é dividido sucessivamente pelas denominações de notas e moedas, começando pela maior (100) até a menor (1).
# O operador // (divisão inteira) é utilizado para determinar a quantidade de notas ou moedas de cada denominação.
# O operador % (módulo) é utilizado para calcular o valor restante após a retirada das notas ou moedas da denominação atual.
# Finalmente, o programa exibe a quantidade de cada denominação necessária para compor o valor inserido.