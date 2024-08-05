# main.py

from contas import criar_conta, depositar, retirar, verificar_saldo
from menu import exibir_menu

def main():
    while True:
        exibir_menu()
        
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titular = input("Digite o nome do titular da conta: ")
            sucesso, mensagem = criar_conta(titular)
            print(mensagem)

        elif opcao == 2:
            titular = input("Digite o nome do titular da conta: ")
            quantia = float(input("Digite a quantia a ser depositada: "))
            sucesso, mensagem = depositar(titular, quantia)
            print(mensagem)

        elif opcao == 3:
            titular = input("Digite o nome do titular da conta: ")
            quantia = float(input("Digite a quantia a ser retirada: "))
            sucesso, mensagem = retirar(titular, quantia)
            print(mensagem)

        elif opcao == 4:
            titular = input("Digite o nome do titular da conta: ")
            sucesso, mensagem = verificar_saldo(titular)
            print(mensagem)

        elif opcao == 5:
            print("Obrigado por usar o sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
