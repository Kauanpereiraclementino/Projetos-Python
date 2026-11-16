import random

#help(random)

baixo=1
alto=100
opçoes =("pedra","papel","tesoura")
cartas=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]


#numero=random.randint(baixo, alto)
#numero=random.random()
#tentativa=random.choice(opçoes)
random.shuffle(cartas)
print(cartas)