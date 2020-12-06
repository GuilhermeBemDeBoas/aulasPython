h=float(input("digite sua altura: "))
p=float(input("digite seu peso: "))
IMC=p/((h)**2)
if IMC<20:
    print("abaixo do peso")
else:
    if IMC>=20 and IMC<=25:
        print("Peso normal")
    else:
        if IMC>25 and IMC<=30:
            print("Excesso de peso")
        else:
            if IMC>30 and IMC<=35:
                print("Obesidade")
            else:
                print("Obesidade morbida")
