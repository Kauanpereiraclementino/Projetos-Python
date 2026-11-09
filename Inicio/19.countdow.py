import time 

tempo=int(input("digite o tempo em segundos:"))

for x in range(tempo ,0 , -1):
    segundos= x % 60
    minutos= int(x / 60 )% 60
    horas=int(x/ 3600)
    print(F"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)

print("hora de levantar ")    