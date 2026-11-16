import random 

baixo=1
alto=100 
numero=random.randint(baixo,alto)
tentativas=0
is_running=True

print("jogo de advinhaçao em python")

print(f"Digite um numero de {baixo} a {alto}")    


while is_running:
    tentativa=input("digite um numero:")
    if tentativa.isdigit():
       tentativa=int(tentativa)
       tentativas+= 1
       if tentativa < baixo or tentativa > alto:
           print("Numero fora do limite")
           print(f"Digite um numero de {baixo} a {alto}")  
       elif tentativa < numero:
           print("Muito baixo!tente denovo!")
       elif tentativa > numero:
           print("muito alto! tente novamente!")
       else:
           print(F"parabens voce acertou o numero,o numero era {numero}")
           print(f"numero de tentativas {tentativas}") 
           is_running=False           
    else:
        print("tentativa invalida") 
        print(f"Digite um numero de {baixo} a {alto}")     
