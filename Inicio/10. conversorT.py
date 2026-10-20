unit = input("Sua temperatura é em celsius ou fahreinheit (c/f) : ")
temp = float(input("Coloque a temperatura : ")) 

if unit =="c":
   temp = round((9 * temp) / 5 + 32, 2 )
   print(F"sua temperatura em fahreinheit é {temp} °F  ") 
elif unit=="f":
   temp=round((temp - 32) * 5/9 , 1)
   print(F"sua temperatura em celsiu é {temp}°c ")
else: 
   print(F"{unit} inserida é invalida ")