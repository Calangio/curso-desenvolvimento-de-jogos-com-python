
# Média notas

# Utilizamos a função input para receber dados do usuário(O valor lido sempre é tratado como string);
# A função float converte o número lido para decimal
n1 = float(input("Informe sua primeira nota: ")) 
n2 = float(input("Informe sua segunda nota: "))
n3 = float(input("Informe sua terceira nota: "))

# Imprime a média das notas
print(f"Sua média é: {(n1+n2+n3)/3}")
print("----------------------------")

# Média salarial

salario1 = float(input("Informe o primeiro salário: ")) 
salario2 = float(input("Informe o segundo salário: ")) 
salario3 = float(input("Informe o terceiro salário: "))

media = (salario1+salario2+salario3)/3

# Imprime a média dos salarios informados.
print(f"A média salarial é: {media}")

