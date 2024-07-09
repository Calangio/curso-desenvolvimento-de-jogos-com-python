#desafio: construindo menu com inputs do usuário
#40-len(item)+6
prato1=input("\ndigite o nome do prato: ")
valor1=float(input("digite o valor do prato 1: "))

prato2=input("digite o nome do prato: ")
valor2=float(input("digite o valor do prato 2: "))

prato3=input("digite o nome do prato: ")
valor3=float(input("digite o valor do prato 3: "))

print("\n")
print("cardápio menu".center(40, "="))
print(f"{prato1}".title()+".".center(40-((len(prato1))+len(str(valor1))+4),".")+f"{valor1:.2f}"+" R$")
print(f"{prato2}".title()+".".center(40-((len(prato2))+len(str(valor2))+4),".")+f"{valor2:.2f}"+" R$")
print(f"{prato3}".title()+".".center(40-((len(prato3))+len(str(valor3))+4),".")+f"{valor3:.2f}"+" R$")
print("".center(40, "="), "\n")