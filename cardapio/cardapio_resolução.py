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
