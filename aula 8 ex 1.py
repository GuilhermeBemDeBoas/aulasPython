import random
x=int(input("Aposta:"))
v1 = random.randint(1,6)
print("dado 1:",v1)

v2 = random.randint(1,6)
print("dado 2:",v2)
y=v1+v2
if x==y:
    print("Ganhou!")
else:
    print("Perdeu!")

