#name=input("digite seu nome:")
#while name =="":
    #print("voce nao digitou seu nome")
   # name=input("digite seu nome")
#print(f"bem vindo! {name}")   
#####################################
#idade=int(input("digite sua idade "))
#while idade <= 0:
    #print("Idade nao pode ser negativa ou 0" )
    #idade=float(input("digite sua idade "))
#print(F"voce tem {idade} anos de idade")    
#####################################
#comida=input("coloque uma comida que voce gosta (Q/q para sair):")
#while not comida =="Q":
    #print(f"voce gosta de {comida}")
    #comida=input("coloque outra comida que voce gosta (Q para sair):")

#print("faz o L otario")    
#####################################

numero=int(input("digite um numero entre 1 e 10 :"))

while numero < 1 or numero > 10:
    print(f"{numero} nao é valido ")
    numero=int(input("digite um numero entre 1 e 10 :"))

print(f"seu numero é {numero}")    


