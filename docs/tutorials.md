# Ejemplo

La integral es la siguiente:
\begin{align}
I = \int_1^3 {\rm{d}}x [x⁶-x²sen(2x)]
\end{align}

Las bibliotecas necesarias para la implementación del código son las siguientes:

```python
from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np
```

La siguiente función calcula los puntos de muestreo y los pesos mediante la implementación de los polinomios de Legedre

```python
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

n1 = gaussxw(1)

n2 = gaussxw(2)

n3 = gaussxw(3)

n4 = gaussxw(4)

n5 = gaussxw(5)
```

La siguiente función escala los puntos de muestreo y los pesos en el intervalo $[1, 3]$.

```python
def gaussxwab(a, b, x, w):

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

n1_r = gaussxwab(1.0, 3.0, n1[0], n1[1])

n2_r = gaussxwab(1.0, 3.0, n2[0], n2[1])

n3_r = gaussxwab(1.0, 3.0, n3[0], n3[1])

n4_r = gaussxwab(1.0, 3.0, n4[0], n4[1])

n5_r = gaussxwab(1.0, 3.0, n5[0], n5[1])
```
La siguiente función evalua la función en los puntos de muestreo que ya están escalados y que se guardaron anteriormente.
```python
def func(varInd):
    return (varInd ** 6) - (varInd ** 2 * (np.sin(2 * varInd)))
```

Por último, se calcula el resultado de la aproximación, mediante `np.sum`, para cada N seleccionado anteriormente y se imprimen todos los resultados.
Se implementa la `np.sum` con la finalidad de reducir el impacto computacional que tendría utilizar `for loops`.

```python
resultN1 = np.sum(n1_r[1] * func(n1_r[0]))
resultN2 = np.sum(n2_r[1] * func(n2_r[0]))
resultN3 = np.sum(n3_r[1] * func(n3_r[0]))
resultN4 = np.sum(n4_r[1] * func(n4_r[0]))
resultN5 = np.sum(n5_r[1] * func(n5_r[0]))

print(resultN1, resultN2, resultN3, resultN4, resultN5)
```

