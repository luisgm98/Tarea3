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

Para esta parte, sabemos que que la función de densidad conjunta al asumir independencia corresponde a la siguiente: 

![alt text](https://github.com/luisgm98/Tarea3/blob/master/densidadconj.PNG)

Por lo tanto, al sustituir las funciones por las funciones Gaussianas evaluadas en los parametros de X y Y encontrados anteriormente, obtenemos la siguiente función de densidad conjunta:
![alt text](https://github.com/luisgm98/Tarea3/blob/master/densidadconjunta.PNG)

##  Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

Para esta sección, utilizamos los datos obtenidos del archivo "xyp" y se procedió a crear las siguientes funciones, las cuales se encargan de calcular la correlación, covarianza y el coeficiente de correlación.
```
"Para la correlación creamos la siguiente función"
def correlacion(xyp):
    suma = 0
    for i in range(0,231):
        mult = 1
        for e in range(0,3):
            mult = mult*xyp.iloc[i][e]  
        suma += mult
    return suma
  
"Para la covarianza creamos la siguiente función"
def covarianza(xyp):
    suma2 = 0
    for i in range(0,231):
        suma2 += (xyp.iloc[i][0]-param[0])*(xyp.iloc[i][1]-param2[0])*xyp.iloc[i][2]        
    return suma2

"Creamos la función coeficientePearson"
def coeficientepearson(xyp):
    suma3 = 0
    for i in range(0,231):
        suma3 += (xyp.iloc[i][0]-param[0])*(xyp.iloc[i][1]-param2[0])/(param[1]*param2[1])*xyp.iloc[i][2]
    return suma3
```
Lo anterior nos da como resultado los siguientes valores:
- Correlacion: 149.54281000000012. Este valor nos indica el grado en que dos o más variables se encuentran asociadas linealmente, por lo tanto, este valor obtenido nos indica que X y Y estan altamente asociadas linealmente.
- Covarinza: 0.06669157081830895. El valor de la covarianza nos indica si las variables son independientes o no estan correlacionadas, esto en caso de que sea igual a cero. En este ejemplo podemos ver que la covarianza se puede aproximar como 0, lo cual nos indica que X y Y son variables independientes, lo cual coincide con lo asumido en el segundo enunciado.
- Coeficiente de pearson: 0.0033537723017496544. Este valor, al igual que la covarianza, puede ser aproximado como 0, lo cual nos indica que no existe ninguna asociación entre la variable X y Y.

##  Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).



