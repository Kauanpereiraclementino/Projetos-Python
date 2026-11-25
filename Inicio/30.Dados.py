import random

#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"  
"│         │"
"│         │"
"│         │"
"└─────────┘"


dados_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●    ●  │",
       "│         │",
       "│ ●    ●  │ ",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●    ●  │",
       "│ ●    ●  │",
       "│ ●    ●  │",
       "└─────────┘")             
}


dado=[]

total=0 

numero_dado=int(input("Quantos dados? "))


for da in range(numero_dado):
    dado.append(random.randint(1, 6))  

#for da in range(numero_dado):
 #   for line in dados_art.get(dado[da]):
#        print(line)

for line in range(5):
    for da in dado:
        print(dados_art.get(da)[line], end=" ")
    print()   



for da in dado:
    total += da 

print(f"o seu total é : {total}")    


   