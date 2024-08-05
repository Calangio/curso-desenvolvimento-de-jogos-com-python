# Sistema Bancário Básico
- Desenvolva um programa em Python que simule um sistema bancário básico. O programa deve permitir que o usuário crie contas, deposite, retire e verifique o saldo das contas.

## Tópicos trabalhados:
- Entrada e saída de dados: input() e print()
- Estruturas condicionais: if, elif, else
- Estruturas de repetição: while
- Manipulação de variáveis e dicionários

## Descrição:

### Entrada
- O programa deve solicitar ao usuário que insira sua escolha de operação: criar nova conta, depositar, retirar, verificar saldo ou sair.
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
```

### Processamento
- O programa deve permitir as seguintes operações:
  - Criar nova conta: Solicitar o nome do titular e criar uma nova conta com saldo inicial de 0.
  - Depositar: Solicitar o nome do titular e a quantia a ser depositada, verificando se a conta existe e se a quantia é positiva.
  - Retirar: Solicitar o nome do titular e a quantia a ser retirada, verificando se a conta existe e se há saldo suficiente.
  - Verificar saldo: Solicitar o nome do titular e verificar se a conta existe antes de exibir o saldo atual.
  - Sair: Encerrar o programa.

### Saída
O programa deve exibir mensagens confirmando a operação realizada ou informando erros (como conta não encontrada, saldo insuficiente, etc.). Também deve exibir o saldo atual quando solicitado.

### Exemplos:

Exemplo 1

Entrada
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
1
Digite o nome do titular da conta: João
```

Saída
```bash
Conta criada para João.
```

Exemplo 2

Entrada
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
2
Digite o nome do titular da conta: João
Digite a quantia a ser depositada: 100.00
```

Saída
```bash
Depósito de R$100.00 realizado com sucesso.
```

Exemplo 3

Entrada
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
3
Digite o nome do titular da conta: João
Digite a quantia a ser retirada: 50.00
```

Saída
```bash
Saque de R$50.00 realizado com sucesso.
```

Exemplo 4

Entrada
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
4
Digite o nome do titular da conta: João
```

Saída
```bash
Saldo atual: R$50.00
```

Exemplo 5

Entrada
```bash
Escolha uma opção:
1. Criar nova conta
2. Depositar
3. Retirar
4. Verificar saldo
5. Sair
5
```

Saída
```bash
Obrigado por usar o sistema bancário.
```
