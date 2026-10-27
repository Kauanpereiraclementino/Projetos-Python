name=input("digite seu nome : ")

 

if  len(name) >= 12:
    print("O nome é grande demais ")
elif not name.find(" ") == -1:
    print("nao pode conter espaço no nome ")
elif not name.isalpha():
    print("Nao pode conter numeros ")
else :
    print(F"bem vindo {name}: ")


