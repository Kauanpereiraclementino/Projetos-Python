principal=0
nota=0
tempo=0

while principal <=0:
    principal=float(input("Digite a quantidade inicial: "))
    if principal <=0:
        print("o valor inicial nao pode ser 0 ou menor ")

while nota <=0:
    nota=float(input("Digite a nota de interese : "))
    if nota <=0:
        print("o valor do interrese nao pode ser 0 ou menor ")     

while tempo <=0:
    tempo=int(input("Digite a quantidade de tempo em anos: "))
    if tempo <=0:
        print("o valor do tempo  nao pode ser 0 ou menor ")           

total=principal*pow((1+nota/100), tempo)

print(f"seu valot total de juros compostos é {round(total , 3)}")
                                              #{total: .2f}   
