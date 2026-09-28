#!/usr/bin/env python

""""Calcula integrales mediante el método de cuadratura Gaussiana.

El módulo contiene las siguientes funciones:

- `gaussxw(N)`: Calcula los puntos de muestreo y los pesos.
- `gaussxwab(a, b, x, w)`: Escala los puntos de muestreo y los pesos según el intervalo de integración.
- `func(varInd)`: Evalua la función en los puntos de muestreo escalados.
"""

from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """Utilizando la biblioteca numpy se pueden evaluar los pesos y los puntos de muestreo para utilizar la cuadratura Gaussiana con polinomios de Legendre

    Parámetro:
    -----------
    N : número entero
        Único argumento

    Return
    -----------
    salida : array con números de tipo flotante.
        Devuelve los puntos de muestreo y los pesos en formato de array.

    Ejemplo
    ----------
    >>> import numpy as np

    >>> gaussxw(4) # doctest: +ELLIPSIS
    (array([-0.8611..., -0.3399...,  0.3399...,  0.8611...]), array([0.3478..., 0.6521..., 0.6521..., 0.3478...]))
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """Escala los puntos y pesos en el intervalo de integración correspondiente

    Parámetros:
    ------------
    a : número flotante
        Primer argumento

    b : número flotante
        Segundo argumento

    x : número flotante. Primer elemento del array obtenido al evaluar la función gaussxw
        Tercer argumento

    w : número flotante. Segundo elemento del array obtenido al evaluar la función gaussxwi
        Cuarto argumento

    Return
    -----------
    salida : Dos arrays con números de tipo flotante.
        Devuelve los puntos de muestreo y los pesos escalados en el intervalo de integración correspodiente en formato de array.

   Ejemplo
   -----------
   >>> import numpy as np

   >>> n4 = (np.array([-0.86113631, -0.33998104, 0.33998104, 0.86113631]), np.array([0.34785485, 0.65214515, 0.65214515, 0.34785485]))

   >>> n4_0 = n4[0]

   >>> n4_1 = n4[1]

   >>> gaussxwab(1.0, 3.0, n4_0, n4_1)  # doctest: +ELLIPSIS
   (array([1.1388..., 1.6600..., 2.3399..., 2.8611...]), array([0.3478..., 0.6521..., 0.6521..., 0.3478...]))
   """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def func(varInd):
    """Evalúa la función que se va a integrar en los puntos de muestreo calculados anteriormente

    Parámetros:
    ------------
    varInd : número flotante. Primer elemento del array de puntos de muestreo escalados.
             Único argumento.

    Return
    -----------
    salida : número flotante.
        Devuelve una aproximación de la integral depediendo del N que se haya seleccionado.

   Ejemplo
   ------------
   >>> import numpy as np

   >>> n4_r = (np.array([1.13886369, 1.66001896, 2.33998104, 2.86113631]), np.array([0.34785485, 0.65214515, 0.65214515, 0.34785485]))

   >>> n4_r0 = np.array([1.13886369, 1.66001896, 2.33998104, 2.86113631])

   >>> func(n4_r0) # doctest: +ELLIPSIS
   array([  1.1956...,  21.4147..., 169.6351..., 552.9237...])
   """
    return (varInd ** 6) - (varInd ** 2 * (np.sin(2 * varInd)))

