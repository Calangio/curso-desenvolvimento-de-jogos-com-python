import random

# Loop principal do jogo
jogo = True

while jogo:
    # Entrada do jogador
    jogador = input("Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): ").lower()

    # Condição para sair do jogo
    if jogador == 'sair':
        jogo = False
        break

    # Verificação de escolha inválida
    if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
        print("Escolha inválida. Tente novamente.")
        continue

    # Escolha do computador
    computador = random.choice(["pedra", "papel", "tesoura"])

    # Exibição das escolhas
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    # Determinação do vencedor
    if jogador == computador:
        print("Empate")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Computador venceu!")

print("Obrigado por jogar!")

# Explicação do Código

# Importamos o módulo random para permitir que o computador faça uma escolha aleatória entre "pedra", "papel" e "tesoura".

# Utilizamos um loop while que continua até que o jogador escolha sair do jogo.

# Pedimos ao jogador para fazer uma escolha. A entrada é convertida para minúsculas para facilitar a comparação.

# Se o jogador digitar "sair", o loop é encerrado e o jogo termina.


# Se a escolha do jogador não for "pedra", "papel" ou "tesoura", uma mensagem de erro é exibida e o loop recomeça.

# O computador faz uma escolha aleatória entre "pedra", "papel" e "tesoura".

# As escolhas do jogador e do computador são exibidas.

# Usamos uma série de instruções if-elif-else para determinar o vencedor com base nas escolhas do jogador e do computador.
# Se as escolhas forem iguais, é um empate.
# Caso contrário, verificamos as combinações vencedoras para o jogador. Se nenhuma delas for verdadeira, o computador vence.

# Quando o loop é interrompido e uma mensagem de agradecimento é exibida.