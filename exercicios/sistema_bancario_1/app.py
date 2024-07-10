# Dicionário para armazenar contas bancárias
contas = {}

# Loop principal do sistema bancário
while True:
    # Exibe o menu de opções
    print("\n--- Sistema Bancário ---")
    print("1. Criar nova conta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Verificar saldo")
    print("5. Sair")
    
    # Obtém a escolha do usuário
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Criar nova conta
        titular = input("Digite o nome do titular da conta: ")
        if titular in contas:
            print("Já existe uma conta com esse titular.")
        else:
            contas[titular] = 0
            print(f"Conta criada para {titular}.")

    elif opcao == 2:
        # Depositar
        titular = input("Digite o nome do titular da conta: ")
        if titular in contas:
            quantia = float(input("Digite a quantia a ser depositada: "))
            if quantia > 0:
                contas[titular] += quantia
                print(f"Depósito de R${quantia:.2f} realizado com sucesso.")
            else:
                print("Quantia de depósito deve ser positiva.")
        else:
            print("Conta não encontrada.")

    elif opcao == 3:
        # Retirar
        titular = input("Digite o nome do titular da conta: ")
        if titular in contas:
            quantia = float(input("Digite a quantia a ser retirada: "))
            if 0 < quantia <= contas[titular]:
                contas[titular] -= quantia
                print(f"Saque de R${quantia:.2f} realizado com sucesso.")
            else:
                print("Saque inválido. Verifique o saldo e a quantia solicitada.")
        else:
            print("Conta não encontrada.")

    elif opcao == 4:
        # Verificar saldo
        titular = input("Digite o nome do titular da conta: ")
        if titular in contas:
            print(f"Saldo atual: R${contas[titular]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == 5:
        # Sair do sistema
        print("Obrigado por usar o sistema bancário.")
        break

    else:
        print("Opção inválida. Tente novamente.")


# Explicação do Código

# Armazena todas as contas bancárias criadas, utilizando o nome do titular como chave e o saldo da conta como valor.

# Utiliza um loop while para exibir o menu de opções e realizar operações bancárias até que o usuário escolha sair (5).

# Exibe as opções do sistema bancário: criar nova conta, depositar, retirar, verificar saldo e sair.

# Criar Nova Conta:
# Solicita o nome do titular e verifica se já existe uma conta com esse nome. Se não existir, cria uma nova conta com saldo inicial de 0.

# Depositar:
# Solicita o nome do titular e a quantia a ser depositada. Verifica se a conta existe e se a quantia é positiva antes de realizar o depósito.

# Retirar:
# Solicita o nome do titular e a quantia a ser retirada. Verifica se a conta existe e se há saldo suficiente para realizar o saque.

# Verificar Saldo:
# Solicita o nome do titular e verifica se a conta existe antes de exibir o saldo atual.

# Sair do Sistema:
# Encerra o loop e exibe uma mensagem de agradecimento.