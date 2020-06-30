# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:29:42 2020

@author: luisg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

"--------------------------------------------------------------------------"
"Leemos los datos del archivo 'xy.csv' y los almacenamos en xy"
xy = pd.read_csv('xy.csv',header=0)


"----------------------------------------------------------------------------------------"

"Buscamos los valores marginales de y y de x para encontrar la PMF"
PMFy = []
PMFx = []
tf = len(xy.iloc[0])  #Tamaño de filas= 22, la cuenta en las filas debe empezar en 1 hasta 21
tc = len(xy.iloc[:,1])  #Tamaño de columna=11, la cuenta en las columnas debe ir desde 0 hasta 10


"La función vmy se encarga de agregar todos los valores marginales de y a la lista my"
def vmy():
    for i in range(1,tf):  
        y = 0
        for e in range(0,tc):
            y =  y + xy.iloc[e][i]
        PMFy.append(y)

"Luego, la función vmx se encarga de encontrar todos los valores marginales de x a la lista mx"
def vmx():
    for i in range(0,tc):  
        x = 0
        for e in range(1,tf):
            x =  x + xy.iloc[i][e]
        PMFx.append(x)

"Llamamos ambas funciones"
vmy()
vmx()

mx = np.linspace(5, 15, num=11, endpoint=True, retstep=False, dtype=int, axis=0)
my = np.linspace(5, 25, num=21, endpoint=True, retstep=False, dtype=int, axis=0)


plt.figure(1)
plt.plot(mx,PMFx)
plt.title('PMF de "X"')
plt.ylabel('Densidad marginal en X')
plt.xlabel('Datos')
plt.show()

plt.figure(2)
plt.plot(my,PMFy)
plt.title('PMF de "Y"')
plt.ylabel('Densidad marginal en Y')
plt.xlabel('Datos')
plt.show()

"-----------------------------------------------------------------------------"
"Definimos la función gaussiana"
def gauss(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
    

"Parametros para la distribución de X y Y"
param,_ = curve_fit(gauss,mx,PMFx,p0=[0,1])
param2,_ = curve_fit(gauss,my,PMFy,p0=[0,1])


print("Los párametros para la distribución de X corresponden a:", param)
print("Los párametros para la distribución de Y corresponden a:", param2)

plt.figure(3)
plt.plot(mx,PMFx)
plt.title("Distribución en X y su curva de ajuste")
plt.ylabel('Densidad marginal en X')
plt.xlabel('Valores de X')
plt.plot(mx,gauss(mx,param[0],param[1]))

plt.figure(4)
plt.plot(my,PMFy)
plt.title("Distribución en Y y su curva de ajuste")
plt.ylabel('Densidad marginal en Y')
plt.xlabel('Valores de Y')
plt.plot(my,gauss(my,param2[0],param2[1]))

"-------------------------------------------------------------------------"
"Punto 3: Correlación, covarianza"
"Leemos los datos del archivo 'xyp.csv' y los almacenamos en xy"
xyp = pd.read_csv('xyp.csv',header=0)

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

print("Correlacion:",correlacion(xyp) )
print("Covarinza:",covarianza(xyp))
print("Coeficiente de pearson:",coeficientepearson(xyp))

"-------------------------------------------"
"Creamos los distintos vectores y se agregan sus valores mediante un recorrido de los datos del archivo xyp.csv"
x = []
y = []
z = []

for i in range(0,231):
    x.append(xyp.iloc[i][0])
    y.append(xyp.iloc[i][1])
    z.append(xyp.iloc[i][2])
    
"--------------------------------------------------------------------------"
"Procedemos a calcular las funciones de densidad marginales en 2D y la de densidad conjunta en 3D"
plt.figure(5)
plt.title("Función de densidad marginal de X")
plt.ylabel('Densidad marginal en X')
plt.xlabel('Valores de X')
plt.plot(mx,gauss(mx,param[0],param[1]))

plt.figure(6)
plt.title("Función de densidad marginal de Y")
plt.ylabel('Densidad marginal en Y')
plt.xlabel('Valores de Y')
plt.plot(my,gauss(my,param2[0],param2[1]))

       
fig = plt.figure(7)
ax = plt.axes(projection="3d")
plt.title("Función de densidad conjunta")
plt.ylabel('Valores de Y')
plt.xlabel('Valores de X')
ax.scatter3D(x,y,z)

