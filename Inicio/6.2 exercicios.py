import math


raio=float(input("digite o raio do circulo: "))

circuferecia = 2 * math.pi * raio 
area=math.pi* pow(raio, 2)

print(f"A circunferencia do circulo é: {round(circuferecia, 2)}cm")
print(f"A area do circulo é: {round(area , 3)}cm")


A=float(input("Digite o primeiro lado do quadrado:"))
B=float(input("Digite o segundo lado do quadrado:"))

hipotenusa=math.sqrt(pow(A, 2) + pow(B, 2))

print(f"O quadrado da hipotenusa é: {round(hipotenusa , 3)}")