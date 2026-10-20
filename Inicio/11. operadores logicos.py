
#OR 

temp = 25
esta_chovendo=False

if temp > 35 or temp < 0 or esta_chovendo:
    print("O evento de lado de fora esta cancelado")
else:
    print("o evento vai continuar")



#AND

temp=28
esta_ensolarado=False

if temp >= 35 and esta_ensolarado:
    print("esta quente la fora")
    print("e esta ensolarado")
elif temp <= 0 and esta_ensolarado:
    print("esta frio la fora ")
    print("e esta ensolarado")
elif 25 > temp > 0 and esta_ensolarado:
     print("esta morno la fora ")
     print("e esta ensolarado")
elif temp >= 28 and not esta_ensolarado:
    print("esta quente la fora")
    print("e esta nublado")
elif temp <= 0 and not esta_ensolarado:
    print("esta frio la fora ")
    print("e esta nublado")
elif 25 > temp > 0 and not esta_ensolarado:
     print("esta morno la fora ")
     print("e esta nublado")