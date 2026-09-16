resposta=input("voce gostaria de comer ? (y/n): ")
name=input("digite seu nome: ")
for_sale=True

if for_sale:
    print("esse item esta em promoçao ")
else:
    print("este item nao esta em promoçao")

if name == "":
    print("voce nao digitou nada")
else:
    print(f"olar {name}:")

if resposta == "y":
    print("pegue alguma comida ")
else:
    print("entao fique com fome")
