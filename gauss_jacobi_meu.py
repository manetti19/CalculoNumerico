import numpy as np

def gauss_jacobi(A, b, x0, tol, max_iterations):
    D=np.diag(np.diag(A))
    E= - (np.triu(A) - D) 
    F= - (np.tril(A) - D)
    invD=np.linalg.inv(D)
    L=np.dot(invD, E)
    U=np.dot(invD, F)
    
    xk = x0.copy()
    
    for iteration in range(max_iterations):
        x = np.dot((L + U), xk) + np.dot(invD, b)

        # Verifica a convergência
        if np.max(x-xk) < tol:
            print(f'Convergência alcançada após {iteration + 1} iterações.')
            return x

        xk = x.copy()

    print('Número máximo de iterações alcançado.')
    return x

# Exemplo de uso
A = np.array([[4, -1, 1, 0],
              [-1, 4, 1, 1],
              [0, 2, 6, -1],
              [1, 0, -1, 5]])

b = np.array([15, 10, 13, 12])
x0 = np.zeros_like(b)

# Calcula a solução usando o método de Gauss-Jacobi
solution = gauss_jacobi(A, b, x0, 1e-5, 100)
print('Solução:')
print(solution)
