# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 12:07:01 2018

@author: Mercado-Pc
"""

import numpy as np
import scipy.io
import matplotlib.pyplot as plt

iris = scipy.io.loadmat("iris.mat")

caracteristicas = iris["meas"]
especies = iris["species"]

#graficamos longitud del petalo
print("Longitud del pétalo: ")
plt.figure(1)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[1:50,0],color="b")
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[51:100,0],color="r")
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[101:150,0],color="y")
plt.ylabel('Longitud de Pétalo (cm)')
plt.show()

#graficamos anchura del petalo
print("Anchura del pétalo: ")
plt.figure(2)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[1:50,1],color="b")
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[51:100,1],color="r")
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[101:150,1],color="y")
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

#graficamos longitud y anchura, estas dos caracteristicas diferencian mejor 
#los tres tipos de flores
print("Longitud y anchura del pétalo: ")
plt.figure(5)
plt.scatter(caracteristicas[1:50,0],caracteristicas[1:50,1],color="b")
plt.scatter(caracteristicas[51:100,0],caracteristicas[51:100,1],color="r")
plt.scatter(caracteristicas[101:150,0],caracteristicas[101:150,1],color="y")
plt.xlabel("Longitud del Pétalo (cm)")
plt.ylabel("Anchura del Pétalo (cm)")


# graficamos las dos características que más sirven para diferenciar las especies de flores.
print("Longitud y anchura del pétalo: ")
plt.figure(6)
plt.scatter(caracteristicas[1:50,0],caracteristicas[1:50,1], color="b")
plt.scatter(caracteristicas[51:100,0],caracteristicas[51:100,1], color="r")
plt.scatter(caracteristicas[101:150,0],caracteristicas[101:150,1], color="y")
plt.xlabel("Longitud del Pétalo (cm)")
plt.ylabel("Anchura del Pétalo (cm)")


x = [[caracteristicas[:,0]],[caracteristicas[:,1]]]

# obtenemos las características globales promedio
xprom = np.mean(x,0)
# extraemos las caracteristicas globales promedio de nuestros datos
x = x - xprom*np.ones((150,1))


plt.scatter(x[1:50,0],x[1:50,1], color="b")
plt.scatter(x[51:100,0],x[51:100,1], color="r")
plt.scatter(x[101:150,0],x[101:150,1], color="y")
plt.xlabel("Longitud del Pétalo (cm)")
plt.ylabel("Anchura del Pétalo (cm)")
plt.grid("on")
#
plt.scatter(x[1:50,0],x[1:50,1],alpha=0.25,color="b")
plt.scatter(x[51:100,0],x[51:100,1],alpha=0.25,color="r")
plt.scatter(x[101:150,0],x[101:150,1],alpha=0.25,color="y")
plt.xlabel("Longitud del Pétalo (cm)")
plt.ylabel("Anchura del Pétalo (cm)")
plt.grid("on")

prom_1 = np.mean(x[1:50,:],0)
prom_2 = np.mean(x[51:100,:],0)
prom_3 = np.mean(x[101:150,:],0)

 #graficamos los vectores
plt.quiver(prom_1[0,0],prom_1[1,0],angles="xy", scale_units="xy", scale=1, color="b")
plt.quiver(prom_2[0,0],prom_2[1,0],angles="xy", scale_units="xy", scale=1, color="r")
plt.quiver(prom_3[0,0],prom_3[1,0],angles="xy", scale_units="xy", scale=1, color="g")

# extraemos los datos de esta ilera en una variable nueva
x_muestra = x[1:140,:]

# calculamos el producto interno de esta muestra con cada uno de los vectores promedio
prod_1 = x_muestra*prom_1
prod_2 = x_muestra*prom_2
prod_3 = x_muestra*prom_3

# imprimimos los resultados
print("el producto interno del vector muestra con de los vectores promedio correspondientes a las especies de plantas son: \n")
print("\n setosa ", prod_1)
print("\n versicolor ", prod_2)
print("\n virginica ", prod_3)
print("\n\ny la especie correcta del vector muestra es: \n")
print("\n ", especies[1:140,:])