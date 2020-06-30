# Tarea3
Antes de comenzar la explicación de este trabajo realizado en lenguaje de programación Python, se mostrarán las librerias que se importaron.
```
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
```


Para la solución de esta tarea se comenzó leyendo los archivos "xy.csv" y "xyp.csv" con ayuda de la libreria Pandas. Posterior a esto, se calcularon los valores marginales tanto de X, como de Y; para esto se procedió a crear dos funciones que recorrieran los datos por fila y por culumna, y que además realizaran una sumatoria de cada una, estos valores ya correspondian a los valores marginales de cada X y Y. Estas funciones también se encargaban de almacenar estos valores en las listas "mx" y "my". Luego se procedió a graficar dichos valores para así poder observar su 

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

![alt text](https://github.com/luisgm98/Tarea3/blob/master/PMFx.png)

![alt text](https://github.com/luisgm98/Tarea3/blob/master/PMFy.png)
