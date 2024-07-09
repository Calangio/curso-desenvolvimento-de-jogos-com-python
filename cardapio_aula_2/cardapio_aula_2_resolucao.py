#atribuição de itens disponíveis:
item1="Pastel";
preco1=2;

item2="Coxinha";
preco2=3;

item3="Esfirra";
preco3=4;

item4="coca";
preco4=7;

item5="Pizza";
preco5=20;

#exibindo cardápio:
print(
    f"""
    =============cardápio menu=================
    [1] {item1}..........................R$ {preco1:.2f} 
    [2] {item2}.........................R$ {preco2:.2f} 
    [3] {item3}.........................R$ {preco3:.2f} 
    [4] {item4}............................R$ {preco4:.2f} 
    [5] {item5}..........................R$ {preco5:.2f} 
    ===========================================
    """
)

#variáveis de controle:
pedido="";
valorTotal=0;


#simulação de pedido:
while True:

    continuar="y";
    while(continuar=="y"):
        item=int(input("selecione uma das opções do cardápio: "));


        while(item>5 or item<1):
            item=int(input("digite um item válido do cardápio: "));

        if item==1:
            pedido+="+ Pastel (2.00)\n";
            valorTotal+=preco1;
        elif item==2:
            pedido+="+ coxinha (3.00)\n";
            valorTotal+=preco2;
        elif item==3:
            pedido+="+ esfirra (4.00)\n";
            valorTotal+=preco3;
        elif item==4:
            pedido+="+ coca (7.00)\n";
            valorTotal+=preco4;
        elif item==5:
            pedido+="+ Pizza (20.00)\n";
            valorTotal+=preco5;

        continuar=input("deseja continuar com o pedido (y, n): ");

        while(continuar!="y" and continuar!="n"):
            continuar=input("deseja continuar com o pedido (y, n): ");

    if continuar=="n":
        pedido+="==================\n"
        pedido+=f"total = {valorTotal:.2f}\n";
        break;


print("\n"+"Recibo".center(18));
print("==================")
print(pedido);

