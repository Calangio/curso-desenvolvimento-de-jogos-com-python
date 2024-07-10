# Contador progressivo ou regressivo

# Utilizamos a função input para receber dados do usuário(O valor lido sempre é tratado como string);
# A função int converte o número lido(String) para inteiro
numero = int(input("Informe o número inicial: ")) # Tipo: int -> Número inteiro.
ordem = input("Digite (R) para contagem regressiva ou (P) contagem progressiva: ").upper() # Tipo: string -> texto.
auxiliar = 0 # Tipo: int -> Número inteiro.
condicao = True # Tipo: bollean -> Verdadeiro ou falso.

# Estrutura de repetição while
while condicao:
  if ordem == "R":
    print(numero)
    numero -= 1
    if numero < 0:
      condicao = False
  elif ordem == "P":
    print(auxiliar)
    auxiliar += 1
    if numero < auxiliar:
      condicao = False
  else:
    print("Opção inválida. Tente novamente.")
    ordem = input("Digite (R) para contagem regressiva ou (P) contagem progressiva: ").upper()
