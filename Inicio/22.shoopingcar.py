comidas=[]
preços=[]
total=0

while True:
    comida=input("digite a comida que voce quer (Q para sair):")
    if comida.upper() == "Q":
        break
    else:
        preço= float(input(F"digite o preço da {comida} : $"))
        comidas.append(comida)
        preços.append(preço)

print("----------SEU CARRINHO---------")       

for comida in comidas:
    print(comida,end=" ")

for preço in preços:
    total +=preço

print()
print(f"seu total é : ${total: .2f} ")