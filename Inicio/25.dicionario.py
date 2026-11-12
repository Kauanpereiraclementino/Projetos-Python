capitais={"brasil": "Brasilia",
          "India":"New Dehli",
          "China":"Beijing",
          "Russia":"Moscow"}

#print(capitais.get("brasil"))

#if capitais.get("brasil"):
#   print("essa capital existe")
#else:
#    print("essa capital nao existe")    

#capitais.update({"alemanha":"Berlin"})
#capitais.update({"Brasil":"Berlin"})
#capitais.pop("China")
#capitais.popitem()
#capitais.clear()

#keys=capitais.keys()

#for key in capitais.keys():
    #print(key)

#valores=capitais.values()

#for valor in capitais.values():
    #print(valor)

#item=capitais.items()

for key, valor in capitais.items():
    print(f"{key},{valor}")

