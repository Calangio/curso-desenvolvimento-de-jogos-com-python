#menu simples de jogo

print('''
======== nome do jogo =========
| [1] play                    |  
| [2] tabela de classificação | 
| [3] instruções              | 
| [4] créditos                |   
| [0] sair                    |
===============================
''')


while True:
    
    op_selecionada=input("digite uma das opções listadas: ");

    if(op_selecionada=="1"):
        print("jogo iniciado\n");
    elif(op_selecionada=="2"):
        print("aqui funcionará nosso tabela de classificações\n");
    elif(op_selecionada=="3"):
        print("aqui ficará as instruções de como jogar seu jogo\n");
    elif(op_selecionada=="4"):
        print("aqui você creditará o(s) desenvolvedor(es)\n");
    elif(op_selecionada=="0"):
        break
    else:
        continue

