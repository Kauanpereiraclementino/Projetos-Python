operador=input("Digite um operador (+) (-) (x) (/) :")

numeroa=float(input("digite o primeiro numero:"))
numerob=float(input("digite o segundo numero:"))


if operador == "+":
    resultado=numeroa + numerob
    print(f"seu resultado é:{round(resultado , 3)} ")
elif operador== "-":
    resultado=numeroa - numerob
    print(f"seu resultado é:{round(resultado , 3)} ")
elif operador == "x":
    resultado=numeroa * numerob
    print(f"seu resultado é:{round(resultado , 3)} ")
elif operador == "/":
     if numerob == 0:
         print("numero digitado invalido")
     else :
         resultado= numeroa / numerob
         print(f"seu resultado é: {round(resultado , 3)}")
else:
    print(f"{operador} nao é um operador valido")         
                       