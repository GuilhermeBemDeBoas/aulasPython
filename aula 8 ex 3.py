import random
x=input("escolha pedra papel ou tesoura:")
#1="pedra"
#2="papel"
#3="tesoura"
j2=random.randint(1,3)
if j2==1:
    print("pedra")
else:
    if j2==2:
        print("papel")
    else:
        print("tesoura")
if x=="pedra":
    if x=="pedra" and j2 == 1:
        print("empate")
    else:
        if j2==2:
            print("voce perdeu")
        else:
            print("voce ganhou")
else:
    if x=="papel":
        if x=="papel" and j2==1:
            print("voce ganhou")
        else:
            if j2==2:
                print("empate")
            else:
                print("voce perdeu")
    else:
            if x=="tesoura" and j2==1:
                print("voce perdeu")
            else:
                if j2==2:
                    print("voce ganhou")
                else:
                    print("empate")
