import random

jogadas=("pedra",
         "papel",
         "tesoura")

rodando=True

while rodando:

    player= None
    computador=random.choice(jogadas)     

    
    while player not in jogadas:
        player=input("digite sua jogada(pedra,papel,tesoura):")

    print(f"sua jogada é {player}")
    print(f"a Jogada do computador é {computador}")  


    if player == computador:
        print("isso é um empate ")
    elif player == "pedra" and computador =="tesoura":
        print("voce ganhou")
    elif player =="tesoura" and computador =="papel":
        print("voce perdeu")
    elif player == "papel" and computador =="pedra":
        print("voce ganhou")
    else:
        print("voce perdeu")

    
    if not input("voce quer jogar denovo? (s/n)  ").lower() == "s":
       rodando=False


print("Obrigado por jogar")  


        





        



