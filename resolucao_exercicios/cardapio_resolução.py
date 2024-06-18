#itens cardápio e seus respectivos preços

item1="pastel"
preco1=2
preco1=float(preco1)

item2="coxinha"
preco2=3
preco2 = float(preco2)

item3="esfirra"
preco3=4
preco3=float(preco3)

item4 = "coca"
preco4 = 7
preco4 = float(preco4)

item5 = "pizza"
preco5 = 20
preco5 = float(preco5)

#utilizando f-string
print("\n")
print("cardápio menu".center(40, "="))
print(f"{item1}".title(), ".".center(25,"."), f"{preco1:.2f}","R$")
print(f"{item2}".title(), ".".center(24,"."), f"{preco2:.2f}","R$")
print(f"{item3}".title(), ".".center(24,"."), f"{preco3:.2f}","R$")
print(f"{item4}".title(), ".".center(27,"."), f"{preco4:.2f}","R$")
print(f"{item5}".title(), ".".center(25,"."), f"{preco5:.2f}","R$")
print("".center(40, "="), "\n")

#utilizando .format()
print("cardápio menu".center(40, "="))
print("{}".title().format(item1)+".".center(27,".")+"{:.2f}".format(preco1)+" R$")
print("{}".title().format(item2)+".".center(26,".")+"{:.2f}".format(preco2)+" R$")
print("{}".title().format(item3)+".".center(26,".")+"{:.2f}".format(preco3)+" R$")
print("{}".title().format(item4)+".".center(29,".")+"{:.2f}".format(preco4)+" R$")
print("{}".title().format(item5)+".".center(27,".")+"{:.2f}".format(preco5)+" R$")
print("".center(40, "="), "\n")

#utilizando %
print("cardápio menu".center(40, "="))
print("%s" %(item1).title() +".".center(28,".")+"%.2f" %(preco1) +"R$")
print("%s" %(item2).title() +".".center(27,".")+"%.2f" %(preco2) +"R$")
print("%s" %(item3).title() +".".center(27,".")+"%.2f" %(preco3) +"R$")
print("%s" %(item4).title() +".".center(30,".")+"%.2f" %(preco4) +"R$")
print("%s" %(item5).title() +".".center(28,".")+"%.2f" %(preco5) +"R$")

#utilizando ''' (strings triplas)
print(
    f"""
    =============cardápio menu=============
    {item1}..........................{preco1:.2f} R$
    {item2}.........................{preco2:.2f} R$
    {item3}.........................{preco3:.2f} R$
    {item4}............................{preco4:.2f} R$
    {item5}..........................{preco5:.2f} R$
    =======================================
    """
)

#desafio: construindo menu com inputs do usuário
#40-len(item)+6
prato1=input("digite o nome do prato: ")
valor1=float(input("digite o valor do prato 1: "))

prato2=input("digite o nome do prato: ")
valor2=float(input("digite o valor do prato 2: "))

prato3=input("digite o nome do prato: ")
valor3=float(input("digite o valor do prato 3: "))


print("cardápio menu".center(40, "="))
print(f"{prato1}".title()+".".center(40-((len(prato1))+len(str(valor1))+4),".")+f"{valor1:.2f}"+" R$")
print(f"{prato2}".title()+".".center(40-((len(prato2))+len(str(valor2))+4),".")+f"{valor2:.2f}"+" R$")
print(f"{prato3}".title()+".".center(40-((len(prato3))+len(str(valor3))+4),".")+f"{valor3:.2f}"+" R$")
print("".center(40, "="), "\n")