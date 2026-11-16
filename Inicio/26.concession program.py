tabela={"pipoca" : 1.00,
        "cachorro quente": 2.00,
        "pretzel gigante":2.00,
        "algodao doce":1.00,
        "refrigerante":1.00,
        "agua":1.00}

carrinho=[]

total=0

print("-----------Menu-----------")
for key,value in tabela.items():
    print(f"{key:5}:{value:.2f}")
print("--------------------------")
    


while True:
  comida=input("Digite qual item voce quer do cardapio(Q para sair):")
  if comida.upper()=="Q":
     break
  elif tabela.get(comida) is not None:
     carrinho.append(comida)
     
print("------- Seu Carrinho ----------") 
for comida in carrinho:
   total +=tabela.get(comida)
   print(comida,end=" ")

print()
print(f"O total da compra é:{total} reais")   