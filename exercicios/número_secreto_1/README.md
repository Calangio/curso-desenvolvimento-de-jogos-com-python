# Jogo do Número Secreto
- Desenvolva um programa em Python que simule o jogo do número secreto. O programa deve permitir que o usuário tente adivinhar o número secreto em até 10 tentativas.

## Tópicos trabalhados:
- Entrada e saída de dados: input() e print()
- Estruturas condicionais: if, elif, else
- Estruturas de repetição: for
- Manipulação de strings
- Uso de bibliotecas padrão: random

## Descrição:

### Entrada
- O programa deve solicitar ao usuário que insira seu palpite para o número secreto.
```bash
Digite seu palpite:
```

### Processamento
- O número secreto deve ser gerado aleatoriamente entre 1 e 100.
- O jogador tem até 10 tentativas para adivinhar o número secreto.
- O programa deve comparar o palpite do jogador com o número secreto e fornecer dicas:
  - Se o palpite for menor que o número secreto, deve informar que o número secreto é maior.
  - Se o palpite for maior que o número secreto, deve informar que o número secreto é menor.
  - Se o palpite estiver correto, o jogador vence.
- Se o jogador não adivinhar o número secreto dentro do número de tentativas, ele perde e o jogo termina.

### Saída
O programa deve exibir o resultado de cada palpite (maior, menor ou correto) e informar ao jogador quantas tentativas restam. Quando o jogo terminar, deve exibir uma mensagem de agradecimento e o número secreto, se o jogador não tiver adivinhado.

### Exemplos:

Exemplo 1

Entrada
```bash
Tentativa 1: Digite seu palpite: 50
```

Saída
```bash
O número secreto é maior.
Você ainda tem 9 tentativas.
```

Exemplo 2

Entrada
```bash
Tentativa 5: Digite seu palpite: 75
```

Saída
```bash
O número secreto é menor.
Você ainda tem 5 tentativas.
```

Exemplo 3

Entrada
```bash
Tentativa 8: Digite seu palpite: 88
```

Saída
```bash
Parabéns! Você adivinhou o número secreto 88 em 8 tentativas.
```

Exemplo 4

Entrada
```bash
Tentativa 10: Digite seu palpite: 90
```

Saída
```bash
O número secreto é menor.
Você esgotou suas 10 tentativas. O número secreto era 42.
Obrigado por jogar!
```