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