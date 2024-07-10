import random

# Gera um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Número máximo de tentativas
max_tentativas = 10

print("Bem-vindo ao jogo do Número Secreto!")
print(f"Você tem {max_tentativas} tentativas para adivinhar o número secreto, que está entre 1 e 100.")

# Loop principal do jogo
for tentativa in range(1, max_tentativas + 1):
    # Entrada do palpite do jogador
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativa} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    # Informa o número de tentativas restantes
    tentativas_restantes = max_tentativas - tentativa
    if tentativas_restantes > 0:
        print(f"Você ainda tem {tentativas_restantes} tentativas.")
    else:
        print(f"Você esgotou suas {max_tentativas} tentativas. O número secreto era {numero_secreto}.")
        break

print("Obrigado por jogar!")

# Explicação do Código

# Importamos o módulo random para gerar um número secreto aleatório.

# Utilizamos random.randint(1, 100) para gerar um número secreto entre 1 e 100.

# Definimos max_tentativas como 10.

# Utilizamos um loop for para permitir até 10 tentativas para o jogador.

# Em cada iteração, pedimos ao jogador para inserir um palpite.

# Comparamos o palpite do jogador com o número secreto:
# Se o palpite for igual ao número secreto, o jogador vence e o loop é encerrado.
# Se o palpite for menor que o número secreto, informamos ao jogador que o número secreto é maior.
# Se o palpite for maior que o número secreto, informamos ao jogador que o número secreto é menor.

# Informamos ao jogador quantas tentativas restantes ele ainda tem.

# Se o jogador esgotar todas as tentativas sem adivinhar o número secreto, informamos qual era o número secreto.

# Exibimos uma mensagem de agradecimento ao jogador após o término do jogo.