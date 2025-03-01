import matplotlib.pyplot as plt
import math

u = 0

def arctg(x,n): 
    k = 0 
    res = float(0)
    for k in range (n+1): 
        res += ((-1)**k * x**(2*k + 1)) / (2*k + 1)
        k = k +1
    return res
def pi1(i): 
    return (arctg(1,i))
def pi2(i): 
    return (4*arctg(1/5,i) - arctg(1/239,i))
def pi3(i):
    return (arctg(1/2,i) + arctg(1/3,i))
def pi4(i): 
    return (2*arctg(1/3,i) + arctg(1/7,i))
def pi5(i):
    return (arctg(1/2,i) + arctg(1/5,i) + arctg(1/8,i))
def menu():
    print('1: Gregory')
    print('2: Macchin')
    print('3: Hutton')
    print('4: Clausen')
    print('5: Dase')
    u = int(input('Escolha o método: '))
    if u not in [1,2,3,4,5]:
        print('Opção inválida!')
        return menu()
    return u

u = menu()

b = int(input('Termos no gráfico '))

X = [i for i in range (b+1)]
Y = []

for v in range (b+1):
    pi = float(0)
    if u == 1: 
        pi = pi1(v)
    elif u== 2: 
        pi = pi2(v)
    elif u== 3: 
        pi = pi3(v)
    elif u== 4: 
        pi = pi4(v)
    elif u== 5: 
        pi = pi5(v)
    Y.append((math.atan(1)-pi)/(math.atan(1)))
plt.plot(X,Y) 
plt.title('Gráfico')
plt.xlabel('n')
plt.ylabel('Erro aproximado')
plt.show()



