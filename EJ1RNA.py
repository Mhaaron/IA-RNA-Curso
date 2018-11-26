# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:12:12 2018

@author: Mercado-Pc
"""

import numpy as np
import scipy.io
import matplotlib.pyplot as plt

iris = scipy.io.loadmat("iris.mat")

caracteristicas = iris["meas"]
especies = iris["species"]

#------- 1.1 ---------------
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

#graficamos longitud del sepalo
print("Longitud del sépalo: ")
plt.figure(3)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[1:50,2],color="b")
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[51:100,2],color="r")
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[101:150,2],color="y")
plt.ylabel('Longitud de Sépalo (cm)')
plt.show()

#graficamos anchura del sepalo
print("Anchura del sépalo: ")
plt.figure(4)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[1:50,3],color="b")
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[51:100,3],color="r")
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[101:150,3],color="y")
plt.ylabel('Anchura de Sépalo (cm)')
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