num = -1111
A=121      
B=120
idade=13
temperatura=34
operador="Admin"
#print("Positive" if num > 0 else "Negative")

#resultado="igual" if num % 2 == 0 else "sobra"

numero_maximo=A if A > B else B
numero_minimo=A if A < B else B

maior_idade="Adulto" if idade >= 18 else "Menor de idade"
clima="frio" if temperatura < 25 else "Quente"
nivel_de_acess="acesso total" if operador == "Admin" else "acesso de nivel baixo"

print(nivel_de_acess)


print(clima)
print(f"voce é {maior_idade}")
print(numero_maximo)
print(numero_minimo)