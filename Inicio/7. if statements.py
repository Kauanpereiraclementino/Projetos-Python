age=int(input("Digite sua idade:"))

if age >= 18 and age <= 90:
    print("voce pode fazer um cartao de credito!")
elif age < 0:
    print("voce precisa colocar uma idade valida")   
elif    age >= 100:
    print("voce provavelmente esta morto")     
else:
    print("voce nao pode fazer um cartao de credito")    