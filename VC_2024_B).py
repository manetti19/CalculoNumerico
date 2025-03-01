import numpy as np

# Método da Bisseção
def bisc(f, a, b, TolX=1e-6, TolFun=np.finfo(float).eps, MaxIter=100):
    xx = [0] * MaxIter
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("Devemos ter f(a)f(b) < 0!")

    for k in range(MaxIter):
        xx[k] = (a + b) / 2
        fx = f(xx[k])
        err = (b - a) / 2

        if abs(fx) < TolFun or abs(err) < TolX:
            break
        elif fx * fa > 0:
            a = xx[k]
            fa = fx
        else:
            b = xx[k]

    x = xx[k]

    if k == MaxIter:
        print(f"O melhor resultado em {MaxIter} iterações")

    return x, err, xx




# Função para encontrar o coseno do ângulo horário t

def f(phi):
    # Dados corrigidos
    h1_deg = 38 + 22 / 60 + 32.43 / 3600  # Altura de Canopus
    h2_deg = 35 + 8 / 60 + 28.66 / 3600   # Altura de Sírius
    UT1 = 23 + 4 / 60 + 22.34 / 3600      # Tempo Universal para Canopus
    UT2 = 23 + 15 / 60 + 26.10 / 3600     # Tempo Universal para Sírius
    alpha1 = 6 + 23 / 60 + 33.771 / 3600  # Ascensão Reta de Canopus
    alpha2 = 6 + 44 / 60 + 19.23 / 3600   # Ascensão Reta de Sírius
    delta1_deg = -52 - 40 / 60 - 12 / 3600  # Declinação de Canopus (corrigido)
    delta2_deg = -16 - 41 / 60 - 29.39 / 3600  # Declinação de Sírius
    theta0 = 6 + 22 / 60 + 30.977 / 3600  # Hora sideral

    # Conversões necessárias
    h1_rad = h1_deg*2*np.pi/360
    h2_rad = h2_deg*2*np.pi/360
    delta1_rad = delta1_deg*2*np.pi/360
    delta2_rad = delta2_deg*2*np.pi/360
    phi_rad = phi*2*np.pi/360

    # Cálculo do ângulo horário t
    # Calcular cos t1 e t2

    cos_t1 = (np.sin(h1_rad)-np.sin(delta1_rad)*np.sin(phi))/(np.cos(delta1_rad)*np.cos(phi))
    cos_t2 = (np.sin(h2_rad)-np.sin(delta2_rad)*np.sin(phi))/(np.cos(delta2_rad)*np.cos(phi))

    # Verificar se os valores de cos estão no intervalo [-1, 1]
    cos_t1 = np.clip(cos_t1, -1, 1)
    cos_t2 = np.clip(cos_t2, -1, 1)

    # Calcular t1 e t2 a partir de cos(t)
    t1 = np.arccos(cos_t1)
    t2 = np.arccos(cos_t2)

    # Ajustar para o quadrante correto (as estrelas estão a oeste)
    if np.sin(t1) < 0:
        t1 = -t1
    if np.sin(t2) < 0:
        t2 = -t2

    # Converter t1 e t2 para horas
    t1_h = np.degrees(t1) / 15.0
    t2_h = np.degrees(t2) / 15.0

    return t1_h - t2_h - 1.0027379*(UT1-UT2) + (alpha1 - alpha2)


# Configurações do método da bisseção
a = (-30)*2*np.pi/360  # Intervalo ajustado
b = (-20)*2*np.pi/360  # Intervalo ajustado
Tolx=np.radians(0.000000278)
TolFun=np.radians(0.000000278)
MaxIter = int(np.ceil(np.log2((b - a) / Tolx)))

# Executando o método da bisseção
x, err, xx = bisc(f, a, b, Tolx, TolFun, MaxIter)

# Convertendo a solução para graus
phi_sol = np.degrees(x)


def calculo_lambda(phi):
    # Dados corrigidos
    h1_deg = 38 + 22 / 60 + 32.43 / 3600  # Altura de Canopus
    h2_deg = 35 + 8 / 60 + 28.66 / 3600   # Altura de Sírius
    UT1 = 23 + 4 / 60 + 22.34 / 3600      # Tempo Universal para Canopus
    UT2 = 23 + 15 / 60 + 26.10 / 3600     # Tempo Universal para Sírius
    alpha1 = 6 + 23 / 60 + 33.771 / 3600  # Ascensão Reta de Canopus
    alpha2 = 6 + 44 / 60 + 19.23 / 3600   # Ascensão Reta de Sírius
    delta1_deg = -52 - 40 / 60 - 12 / 3600  # Declinação de Canopus (corrigido)
    delta2_deg = -16 - 41 / 60 - 29.39 / 3600  # Declinação de Sírius
    theta0 = 6 + 22 / 60 + 30.977 / 3600  # Hora sideral

    # Conversões necessárias
    h1_rad = h1_deg*2*np.pi/360
    h2_rad = h2_deg*2*np.pi/360
    delta1_rad = delta1_deg*2*np.pi/360
    delta2_rad = delta2_deg*2*np.pi/360
    phi_rad = phi*2*np.pi/360

    # Cálculo do ângulo horário t
    k = 1.0027379

    # Calcular cos t1 e t2

    cos_t1 = (np.sin(h1_rad)-np.sin(delta1_rad)*np.sin(phi))/(np.cos(delta1_rad)*np.cos(phi))
    cos_t2 = (np.sin(h2_rad)-np.sin(delta2_rad)*np.sin(phi))/(np.cos(delta2_rad)*np.cos(phi))

    # Verificar se os valores de cos estão no intervalo [-1, 1]
    cos_t1 = np.clip(cos_t1, -1, 1)
    cos_t2 = np.clip(cos_t2, -1, 1)

    # Calcular t1 e t2 a partir de cos(t)
    t1 = np.arccos(cos_t1)
    t2 = np.arccos(cos_t2)

    # Ajustar para o quadrante correto (as estrelas estão a oeste)
    if np.sin(t1) < 0:
        t1 = -t1
    if np.sin(t2) < 0:
        t2 = -t2

    # Converter t1 e t2 para horas

    t1_h = np.degrees(t1) / 15.0
    t2_h = np.degrees(t2) / 15.0

    lambd = UT2*k - t2_h + theta0 - alpha2

    return lambd*15
    #quero em degrees

# Função para converter decimal em graus, minutos e segundos
def decimal_para_graus_min_seg(angle):
    graus = int(angle)
    minutos_dec = abs((angle - graus) * 60)
    minutos = int(minutos_dec)
    segundos = (minutos_dec - minutos) * 60
    return graus, minutos, segundos

# Ajustando a latitude para o hemisfério sul
phi_graus, phi_minutos, phi_segundos = decimal_para_graus_min_seg(phi_sol)
latitude_direcao = "Sul" if phi_sol < 0 else "Norte"
# Calculo da Longitude
lambd_sol = calculo_lambda(phi_sol)
lambda_sol = lambd_sol % 360  # Longitude no intervalo [0°, 360°]

# Ajustando a longitude: se > 180, significa Oeste
if lambda_sol > 180:
    lambda_sol = 360 - lambda_sol
    longitude_direcao = "Oeste"
else:
    longitude_direcao = "Leste"
lambd_graus, lambd_minutos, lambd_segundos = decimal_para_graus_min_seg(lambda_sol)

# Imprimindo os resultados
print(f"Latitude (phi): {abs(phi_graus)}° {phi_minutos}' {phi_segundos:.3f}'' {latitude_direcao}")
print(f"Longitude (lambda): {abs(lambd_graus)}° {lambd_minutos}' {lambd_segundos:.3f}'' {longitude_direcao}")
