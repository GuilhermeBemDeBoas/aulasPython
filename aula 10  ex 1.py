x=int(input("Numero de dias no hospital:"))
y=input("tipo de quarto(particular,semi-particular,coletivo):")
w=input("usou WI-Fi(sim ou nao):")
t=input("usou TV(sim ou nao):")
if y=="particular" or y=="Particular" or y=="PARTICULAR":
    d=360*x
elif y=="Semi-particular" or y=="semi-particular" or y=="SEMI-PARTICULAR":
    d=210*x
elif y=="coletivo" or y=="COLETIVO" or y=="Coletivo":
    d=185*x
else:
    d=0
if w=="sim" or w=="SIM" or w=="Sim":
    wifi=3.00
else:
    wifi=0.00
if t=="sim" or t=="SIM" or w=="Sim":
    tv=4.00
else:
    tv=0.00
print("\nHostpital Comunitario")
print("Numero de dias no hospital:",x)
print("Tipo de quarto:         ",y)
print("Diaris:..................R$",format(d,"10.2f"))
print("WIFI:....................R$",format(wifi,"10.2f"))
print("TV a cabo:...............R$",format(tv,"10.2f"))
print("Total:...................R$",format(d+wifi+tv,"10.2f"))

