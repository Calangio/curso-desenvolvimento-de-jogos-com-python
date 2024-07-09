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

#utilizando %
print("cardápio menu".center(40, "="))
print("%s" %(item1).title() +".".center(28,".")+"%.2f" %(preco1) +"R$")
print("%s" %(item2).title() +".".center(27,".")+"%.2f" %(preco2) +"R$")
print("%s" %(item3).title() +".".center(27,".")+"%.2f" %(preco3) +"R$")
print("%s" %(item4).title() +".".center(30,".")+"%.2f" %(preco4) +"R$")
print("%s" %(item5).title() +".".center(28,".")+"%.2f" %(preco5) +"R$")