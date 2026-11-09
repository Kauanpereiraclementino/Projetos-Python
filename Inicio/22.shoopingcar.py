comidas=[]
preço=[]
total=0

while True:
    comida=input("digite a comida que voce quer (Q para sair):")
    if comida.upper() == "Q":
        break
    else:
        preços= float(input(F"digite o preço da {comida} : $"))
        comidas.append(comida)
        preço.append(preços)

print("----------SEU CARRINHO---------")       

for comida in comidas:
    print(comida,end=" ")

for preços in preço:
    total +=preços

print()
print(f"seu total é : ${total: .2f} ")