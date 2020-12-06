x=int(input("Escreva um número de 3 digitos"))
if x>=100 and x<=999:
    y=x%100
    print(y)
    z=y//10
    print(z)
    if z==0 or z==2 or z==4 or z==6 or z==8:
        print("o número da dezena é par")
    else:
        print("o número da dezena é impar")
else:
    print("o valor não é valido")


