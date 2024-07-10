# Jogo Pedra, Papel e Tesoura 1
- Desenvolva um programa em Python que simule o jogo de Pedra, Papel e Tesoura. O programa deve permitir que o usuário jogue contra o computador até decidir encerrar o jogo.

## Tópicos trabalhados:
- Entrada e saída de dados: input() e print()
- Estruturas condicionais: if, elif, else
- Estruturas de repetição: while
- Manipulação de strings
- Uso de bibliotecas padrão: random

## Descrição:

### Entrada
- O programa deve solicitar ao usuário que insira sua escolha: pedra, papel ou tesoura. Se o usuário desejar encerrar o jogo, ele deve digitar 'sair'.
```bash
Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): 
```

### Processamento
- O computador deve fazer uma escolha aleatória entre "pedra", "papel" e "tesoura".
- As escolhas do usuário e do computador devem ser comparadas para determinar o vencedor:
  - Pedra vence Tesoura
  - Tesoura vence Papel
  - Papel vence Pedra
  - Se ambos escolherem a mesma opção, o resultado é um empate.

### Saída
O programa deve exibir as escolhas do jogador e do computador, e declarar o resultado da rodada (você venceu, computador venceu, ou empate). O jogo continua até que o usuário digite 'sair'.

### Exemplos:

Exemplo 1

Entrada
```bash
Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): pedra
```

Saída
```bash
Você escolheu: pedra
O computador escolheu: tesoura
Você venceu!
```

Exemplo 2

Entrada
```bash
Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): papel
```

Saída
```bash
Você escolheu: papel
O computador escolheu: pedra
Você venceu!
```

Exemplo 3

Entrada
```bash
Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): tesoura
```

Saída
```bash
Você escolheu: tesoura
O computador escolheu: pedra
Computador venceu!
```

Exemplo 4

Entrada
```bash
Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): sair
```

Saída
```bash
Obrigado por jogar!
```