questoes=("quantos elementos tem na tabela periodida?: ",
          "qual animal tem o maior ovo? :",
          "qual o gas mais abundante na atmosfera?: ",
          "quantos ossos tem no corpo humano?: ",
          "qual o planeta do sistema solar mais quente? : ")

opçoes=(("A.224","B.300","C.118","D.119"),
        ("A.Avestruz","B.Galinha","C.Ornitorrico","D.Cobra"),
        ("A.hydrogenio","B.Oxigenio","C. Gas carbonico","D.Nitrogenio"),
        ("A. 230","B. 179","C.206","D.300"),
        ("A.Jupiter","B.Saturno","C.Marte ","D.Venus"))

respostas=("C","A","D","C","D")
tentativas=[]
pontuaçao=0
numero_questao=0    


for questao in questoes:
    print("-----------")
    print(questao)
    for opçao in opçoes[numero_questao]:
        print(opçao)

    tentativa=input("escolha uma das opçoes (A,B,C,D) ").upper()
    tentativas.append(tentativa)
    if tentativa == respostas[numero_questao]:
        pontuaçao += 1
        print("voce pontuo")
    else:
         print("voce nao pontuou")
         print(f"{respostas[numero_questao]} é a resposta correta ")
    numero_questao +=1  

print("-----------")
print(" RESULTADOS ")  
print("-----------")

print("respostas",end=" ")
for resposta in respostas:
    print(resposta,end=" ")
print()  

print("tentativas", end=" ")
for tentativa in tentativas:
    print(tentativa, end=" ")
print() 

print("-------------")
#if pontuaçao <=1:
   #print(F"Voce é mto burro kkkkkkkkkkkkkkkkkk fez {pontuaçao} pontos")
#else: 
    #print(f"Parabens voce fez {pontuaçao} pontos")

pontuaçao=int(pontuaçao /len(questoes) *100)
print(f"Parabens voce fez {pontuaçao} pontos")
    
    