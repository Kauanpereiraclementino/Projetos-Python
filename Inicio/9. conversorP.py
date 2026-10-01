peso=float(input("digite seu peso: "))
medida=input("quilos ou gramas (Q ou G):")

if medida == "Q":
    peso =peso * 2.205
    medida = "lbs."
    print(f"Seu peso é :  {round(peso, 4)} {medida}") 
elif medida =="G":
    peso = peso / 2.205    
    medida = "kgs"
    print(f"Seu peso é :  {round(peso, 4)} {medida}") 
else:
    print(f"{medida} nao é valida")


 