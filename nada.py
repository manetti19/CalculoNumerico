import numpy as np

#A=np.array([[1,2,3],[4,5,6],[7,8,9]])

#D=np.diagonal(A)
#d=np.diag(np.diag(A))
#E=np.triu(A)

#print(d)
#print(D)
#print(E)

#print(np.sin(np.pi/2))

#print(np.arccos(-1))

#print(np.sin(np.radians(48.8566)))



# Valores fornecidos
X = 4285853.505555057
Y = -4019804.5050739734
Z = -2480577.1628146167
a = 6378137.0  # Semi-eixo maior em metros
f = 1 / 298.257223563  # Achatamento
b = a * (1 - f)  # Semi-eixo menor
phi = -20
asd = ((Z * np.sqrt( a**2 * np.cos(phi) **2 + b**2 * np.sin(phi) **2)) / (a * b))

print(asd)