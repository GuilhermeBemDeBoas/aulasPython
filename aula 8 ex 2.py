import random
x=input("escolher par ou impar:")
if x=="par":
    y=int(input("escolha um numero de 1-5:"))
    v1=random.randint(1,5)
    print("jogador 2 jogou",v1)
    if (y+v1)%2==0:
         print("voce ganhou")
    else:
        print("voce perdeu")
else:
    y=int(input("escolha um numero de 1-5:"))
    v1=random.randint(1,5)
    print("jogador 2 jogou",v1)
    if (y+v1)%2==0:
            print("voce perdeu")
    else:
            print("voce ganhou")




      
