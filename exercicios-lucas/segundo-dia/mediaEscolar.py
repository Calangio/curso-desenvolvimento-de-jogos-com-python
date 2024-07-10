# Média escolar

notas = total = 0 # Tipo: int -> Número inteiro.
cond = True # Tipo: bollean -> Verdadeiro ou falso.

# Utilizamos a função input para receber dados do usuário(O valor lido sempre é tratado como string);
nome = input("Olá, informe seu nome: ") # Tipo: string -> texto.

# Estrutura de repetição while
while cond:
    # A função float converte o número lido(String) para decimal
    notas += float(input(f"{nome}, informe sua {total+1}º nota: ")) # Tipo: float -> Número com casas decimais.
    total += 1
    if total == 3:
        media = notas / total
        cond = False

# Verificando condição do aluno conforme sua média
if media >= 7:
    print(f"Parabéns {nome} sua média foi {round(media, 1)} e portanto está aprovado!!")
elif media < 7 and media >= 4:
    print(f"{nome} sua média foi {round(media, 1)} e portanto você está de recuperação!!")
else:
    print(f"{nome} sua média foi {round(media, 1)} e portanto você está reprovado!!")
