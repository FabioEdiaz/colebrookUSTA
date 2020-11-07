# ==============================================================================
# En este archivo vamos a almacenar las diferentes funciones que solucioann la
# ecuación de Colebrook-White
# ==============================================================================

import numpy as np

# ==============================================================================
# Definiendo parámetros de los solvers para homogeneidad en los mismos al
# compararlos
# ==============================================================================
tol = 1e-4
x = 1000
f0 = 0.1
error = 1e4

# ==============================================================================
# Método del punto fijo
# PROBADO Y FUNCIONANDO
# ==============================================================================
def CW_pf(Rey, D, k):

    tol = 1e-4
    x = 1000
    f0 = 0.1
    error = 1e4


    i = 1
    while error > tol:

        f1 = (-2*np.log10((k / D)/3.7 + 2.51 / (Rey * np.sqrt(f0))))**(-2)
        error = abs(f1 - f0) / f0
        f0 = f1
        print ("iteración", i, "raiz aproximada ", f0)
        i += 1

    return f1

# ==============================================================================
# Método de Newton Raphson - simplificado
# PROBADO Y FUNCIONANDO
# ==============================================================================
def CW_NRs(Rey, D, k):

    tol = 1e-4
    x0 = 1000
    err = 1e4
    it = 1

    # Calculo de f(x)
    def g(x):
        return (x + 2 * np.log10((k / D) / 3.7 + (2.51 * x) / (Rey)))

    # Calculo de f'(x)
    def dg(x):
        return 1 + 2.1888442 /((k * Rey / D / 3.7) + 2.51 * x)

    # Iterando para halla solucion
    while err > tol:

        x1 = x0 - g(x0) / dg(x0)
        err = abs(x1 - x0) / x0
        x0 = x1

        f1 = (1 / x0) ** 2
        print ("iteración", it, "raíz aproximada:", f1)
        it += it

    return f1

# ==============================================================================
# Método de Newton Raphson - COMPLICADITO (no probado)
# ==============================================================================

def CW_NRc(Rey, D, k):

    tol = 1e-4
    x0 = 0.1
    err = 1e4
    it = 1

    A = (k / D) / 3.7
    B = 2.52 / Rey
    C = B * (1 / np.log(10))

    def h(x):

        hx = x ** (-1 / 2) + 2 * np.log10(A + B * x ** (-1 / 2))
        print(hx)

        return hx

    def dh(x):

        hpx = -(x ** (-3 / 2)) * (0.5 + C / (A + B * x ** (-1 / 2)))

        print(hpx)

        return hpx


    while err > tol:
        x1 = x0 - h(x0) / dh(x0)
        err = abs(x1 - x0) / x0
        x0 = x1
        print ("iteración", it, "raíz aproximada:", x0)
        it += 1

    return(x1)
