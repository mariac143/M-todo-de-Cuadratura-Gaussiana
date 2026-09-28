# Método de Cuadratura Gaussiana

Consiste en un método que permite calcular el valor de las integrales por medio de la siguiente relación:

$$
\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}
$$

donde:

* $w_k$ son los "pesos"

* $x_k$ son los puntos de muestreo

Este método se caracteriza por lo siguiente:

 * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Lo cual introduce más grados de libertad para la misma discretización en $N$ subregiones.

* Es exacta para un polinomio de orden $(2N - 1)$. Dicho de otra forma, el método de cuadratura gaussiana con $N$ puntos es exacta para cualquier polinomio de grado hasta $(2N - 1)$.

Los puntos de muestreo y los pesos se eligen mediante la siguiente regla:

* $x_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_N(x)$ de orden $N$.

* Los pesos se eligen de tal forma que:
      * $\displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}}$, con $x_k$ que cumple $P_N(x_k)=0$

## Polinomios de Legendre

Los polinomios de Legendre son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Se tiene:
$$
\begin{align}
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}.
\end{align}
$$

Es importante resaltar que los polinomios están definidos en el intervalo $[-1, 1]$.
Y se inician con:
$$
\begin{align}
P_0(x) = 1 \Rightarrow P_1(x) = x,
\end{align}
$$
tal que los siguientes órdenes se generan con la regla de recursividad
$$
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_N(x) -NP_{N-1}(x).
\end{align}
$$

Con la finalidad de simplificar el proceso se utiliza `Scipy` en el código para implementar los polinomios de Legendre. Además, se deben escalar los puntos de muestreo y pesos si se desea trabajar con un intervalo distinto, ya que, como se mencionó anteriormente, solo están definidos en el intervalo $[-1, 1]$. 
