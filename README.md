# Tarea3
Antes de comenzar la explicación de este trabajo realizado en lenguaje de programación Python, se mostrarán las librerias que se importaron.
```
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
```

## A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y

Para la solución de esta tarea se comenzó leyendo los archivos "xy.csv" y "xyp.csv" con ayuda de la libreria Pandas. Posterior a esto, se calcularon los valores marginales tanto de X, como de Y; para esto se procedió a crear dos funciones que recorrieran los datos por fila y por culumna, y que además realizaran una sumatoria de cada una, estos valores ya correspondian a los valores marginales de cada X y Y. Estas funciones también se encargaban de almacenar estos valores en las listas "mx" y "my". Ambas funciones se presentan a continuación.

```
def vmy():
    for i in range(1,tf):  
        y = 0
        for e in range(0,tc):
            y =  y + xy.iloc[e][i]
        PMFy.append(y)

def vmx():
    for i in range(0,tc):  
        x = 0
        for e in range(1,tf):
            x =  x + xy.iloc[i][e]
        PMFx.append(x)
```

Una vez obtenidos los datos, se procedió a gráficar los datos para así poder ver su comportamiento. Los resultados fueron los siguientes:

![alt text](https://github.com/luisgm98/Tarea3/blob/master/PMFx.png)

![alt text](https://github.com/luisgm98/Tarea3/blob/master/PMFy.png)

De las imagenes anteriores, se puede observar que debido a su comportamiento, la mejor curva de ajuste es la Gaussiana. Se procedió a calcular los parámetros para la curva de ajuste Gaussiana de X y de Y, haciendo uso de la función _curve_fit_.

```
"Definimos la función gaussiana"
def gauss(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
    

"Parametros para la distribución de X y Y"
param,_ = curve_fit(gauss,mx,PMFx,p0=[0,1])
param2,_ = curve_fit(gauss,my,PMFy,p0=[0,1])
```

Lo anterior nos da como resultado los siguientes parametros:
- σx=3,29944318
- μx=9,90484384
- σy=6,02693794
- μy=15,07946091

Una vez encontrados dichos parámetros se procedió a gráficar la curva de ajuste para X y Y utilizando el siguiente código:

```
plt.figure(3)
plt.plot(mx,PMFx)
plt.title("Distribución en X")
plt.ylabel('Densidad marginal en X')
plt.xlabel('Valores de X')
plt.plot(mx,gauss(mx,param[0],param[1]))

plt.figure(4)
plt.plot(my,PMFy)
plt.title("Distribución en Y")
plt.ylabel('Densidad marginal en Y')
plt.xlabel('Valores de Y')
plt.plot(my,gauss(my,param2[0],param2[1]))
```

Con lo anterior se obtuvieron las siguientes gráficas:

![alt text](https://github.com/luisgm98/Tarea3/blob/master/AjusteX.png)

![alt text](https://github.com/luisgm98/Tarea3/blob/master/AjusteY.png)


##  Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

