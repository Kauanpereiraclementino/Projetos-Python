#def aniversario(nome , idade ):
 #   print(F"feliz aniversario para {nome}")
  #  print(f"voce esta velho ,tem {idade} anos ")
   # print()



#aniversario("kauan",20)
#aniversario("geovanna",23)   
#aniversario("Maria",21) 

def fatura(nome_usuario,quantidade,data):
    print(f"Ola {nome_usuario}")
    print(f"sua carteira é {quantidade:.2f} o vencimendo é dia {data}")

fatura("kauan2",24.56,"20/10/68")

#return usado no final da funçao para retornar a chamada 

def add(x,y):
    z=x+y
    return z 


def subtraçao(x,y):
    z=x-y
    return z 

def multiplicaçao(x,y):
    z=x*y
    return z 
 
def divisao(x,y):
    if y == 0:
        print("numero invalido 0")
    else:
        z=x/y        
    return z 


print(multiplicaçao(10,2))
print(divisao(1,1))


def criar_nome(primeiro,ultimo): 
    primeiro=primeiro.capitalize()
    ultimo=ultimo.capitalize()
    return primeiro + " " + ultimo

nome_completo=criar_nome("kauan","pereira" )    

print(nome_completo)






