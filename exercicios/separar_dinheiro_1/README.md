# Exercício Separar dinheiro 1
- Desenvolver um programa em Python que receba um valor inteiro e o separe em diferentes denominações de notas e moedas. O programa deve mostrar quantas notas e moedas de cada denominação são necessárias para compor o valor inserido.

## Tópicos trabalhados:

- entrada e saída de dados: `input()` `e print()`
- conversão de tipos de dados
- criação e manipulação de strings
- Operações matemática

## Descrição:

### Entrada
- O programa deve solicitar ao usuário que insira um valor inteiro.
```bash
Digite o valor para separar: 
```
- O `valor` é uma quantidade inteira de dinheiro 

### Processamento
- O valor inserido deve ser dividido nas seguintes denominações: notas de 100, 50, 20, 10, 5, 2 e moedas de 1.
- Para cada denominação, o programa deve calcular quantas notas/moedas são necessárias e atualizar o valor restante a ser dividido.

### Saída
O programa deve exibir a quantidade de notas de cada denominação e moedas de 1 necessárias para compor o valor inserido.

### Exemplos:

Exemplo 1

Entrada
```bash
Digite o valor para separar: 150
```

Saída
```bash
Notas de 100: 1
Notas de 50:  1
Notas de 20:  0
Notas de 10:  0
Notas de 5:   0
Notas de 2:   0
Moedas de 1:  0
```

Exemplo 2

Entrada
```bash
Digite o valor para separar: 1050
```

Saída
```bash
Notas de 100: 10
Notas de 50:  1
Notas de 20:  0
Notas de 10:  0
Notas de 5:   0
Notas de 2:   0
Moedas de 1:  0
```

Exemplo 3

Entrada
```bash
Digite o valor para separar: 188
```

Saída
```bash
Notas de 100: 1
Notas de 50:  1
Notas de 20:  1
Notas de 10:  1
Notas de 5:   1
Notas de 2:   1
Moedas de 1:  1
```