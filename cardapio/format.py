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

#utilizando .format()
print("cardápio menu".center(40, "="))
print("{}".title().format(item1)+".".center(27,".")+"{:.2f}".format(preco1)+" R$")
print("{}".title().format(item2)+".".center(26,".")+"{:.2f}".format(preco2)+" R$")
print("{}".title().format(item3)+".".center(26,".")+"{:.2f}".format(preco3)+" R$")
print("{}".title().format(item4)+".".center(29,".")+"{:.2f}".format(preco4)+" R$")
print("{}".title().format(item5)+".".center(27,".")+"{:.2f}".format(preco5)+" R$")
print("".center(40, "="), "\n")