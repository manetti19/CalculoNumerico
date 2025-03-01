import math
import matplotlib.pyplot as plt

a=0

def arctg(x,n): # x eh o valor do arctg que vc quer     e n eh quantos termos da serie de taylor vc quer
    R=0
    for i in range(n):
        termo = ((-1)**(i)) * (x**(2*i + 1)) / (2*i + 1) # serie de taylor
        R += termo
    return R

def greg(n):
    return 4*arctg(1,n)

def mac(n):
    return 4*arctg(1/5,n) - 4*arctg(1/239,n)

def hut(n):
    return 4*arctg(1/2,n) + 4*arctg(1/3,n)

def cla(n):
    return 8*arctg(1/3,n) + 4*arctg(1/7,n)

def das(n):
    return 4*arctg(1/2,n) + 4*arctg(1/5,n) + 4*arctg(1/8,n)

while a==0:
    print('1: Gregory')
    print('2: Machin')
    print('3: Hutton')
    print('4: Clausen')
    print('5: Dase')
    u=int(input('Qual método?'))
    if u not in [1,2,3,4,5]:
        print('Opção inválida.')
    else: a=1

b=int(input('Quantos termos?'))

X=list(range(b))
Y=[]

for v in range (b):
    if u==1:
       pi=greg(v)
    elif u==2:
        pi=mac(v)
    elif u==3:
        pi=hut(v)
    elif u==4:
        pi=cla(v)
    elif u==5:
        pi=das(v)
    Y.append(math.pi-pi)

plt.plot(X,Y) 
plt.title('Gráfico')
plt.xlabel('n')
plt.ylabel('Diferença')
plt.show()