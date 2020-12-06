x=float(input("insira o primiero valor:"))
y=float(input("insira o segundo valor:"))
if x>y:
    if y<0:
        print(x-(y*(-1)))
    else:
        print(x-y)
else:
    if x<0:
        print(y-(x*(-1)))
    else:
        print(y-x)
