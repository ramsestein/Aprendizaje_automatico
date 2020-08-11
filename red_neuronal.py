#------------------------------------------------------------
#    --------------------------
#    | Red Neuronal en Python |
#    --------------------------
#------------------------------------------------------------
#Importamos las librerias necesarias
#------------------------------------------------------------

import math
import random
#import pyoo

#------------------------------------------------------------
#Funciones de la neurona
#------------------------------------------------------------

def valores_ramdom_w(n):
	#Random de valores w de las neuronas
	for i in range(len(n)):
		if i = 0:
			pass
		else:
			for m in range (1,n[i]):
				for j in range (1,n[i+1]):
					w[i][m][j] = random.random()
	return w

def valores_ramdom_u(n):
	#Random de valores  de las neuronas
	for i in range(len(n)):
		if i = 0:
			pass
		else:
			for m in range (1,n[i]):
    			u[i][m] = random.random ()
	return u

def calculo_neuronas(w,u,z,n):
	#Calculo de los valores de neuronas
	#y es a[4][1]
	for r in range(len(n)):
		if r = 0:
			pass
		else:
			for e in range (1,n[r+1]):
				for q in range(len(z)):
					x[r][e] = x[e] + z[q]*w[r][q][e]
				x[r][e] = x[r][e] + u[r][e]
				a[r][e] = (1 - math.e**x[r][e])**-1
	return a

def calculo_funcion_error(s,y):
	err = -(s-y)
	return err

def nueva_w_nivel1(w,a,y,n,alfa,err,z):
	for r in range(1,n[2]):
		for t in range(1,n[3]):
			gamma = gamma + (w[2][r][t]*a[3][t]*(1-a[3][t])*w[3][t][1])
	for i in range(1,n[1]):
		for j in range(1,n[2]):
			w[1][i][j] = w[1][i][j] - alfa*(err*(z[i]*a[2][j]*(1-a[2][j])*gamma*y*(1-y)))
	return w

def nueva_u_nivel1(u,a,y,n,alfa,err,z):
	for r in range(1,n[2]):
		for t in range(1,n[3]):
			gamma = gamma + (w[2][r][t]*a[3][t]*(1-a[3][t])*w[3][t][1])
	for j in range(1,n[2]):
		u[1][j] = u[1][j] - alfa*(err*(a[2][j]*(1-a[2][j])*gamma*y*(1-y)))
	return u

def nueva_w_nivel2(w,a,y,n,alfa,err):
	for i in range(1,n[1]):
		for j in range(1,n[2]):
			w[2][i][j] = w[2][i][j] - alfa*(err*(a[2][i]*a[3][j]*(1-a[3][j])*w[3][j][1]*y*(1-y)))
	return w

def nueva_u_nivel2(u,a,y,n,alfa,err):
	for r in range(1,n[2]):
		for j in range(1,n[2]):
			u[2][j] = u[2][j] - alfa*(err*(a[3][j]*(1-a[3][j])*w[3][j][1]*y*(1-y)))
	return u

def nueva_w_nivel3(w,a,y,n,alfa,err):
	for i in range(1,n[1]):
		for j in range(1,n[2]):
			w[3][i][j] = w[3][i][j] - alfa*(err*(a[3][j]*y*(1-y)))
	return w

def nueva_u_nivel3(u,a,y,n,alfa,err):
	for r in range(1,n[2]):
		for j in range(1,n[2]):
			u[3][j] = u[3][j] - alfa*(err*(y*(1-y)))
	return u

#------------------------------------------------------------
#Inicio de la neurona
#------------------------------------------------------------
#------------------------------------------------------------
#Datos a modificar para cambiar la red
#------------------------------------------------------------

#Valor deseable como resultado
s = 1
#Numero de neuronas por linea
#El valor 0 inicial no se ha de tomar en cuenta
n = [0,5,6,3,1]
#Valor de alfa
alfa = 0.05

#------------------------------------------------------------
#Inicio de constantes globales
#------------------------------------------------------------

z = []
j = 0
w = [[[[[for e in range(0,n[4])]for d in range(0,n[3])]for c in range(0,n[2])]for b in range(0,n[1])]for a in range(0,n)]
u = [[[[[for e1 in range(0,n[4])]for d1 in range(0,n[3])]for c1 in range(0,n[2])]for b1 in range(0,n[1])]for a1 in range(0,n)]
#Iniciamos la comunicacion con OpenOffice
#desktop = pyoo.Desktop("localhost", 2002)
#Abrimos el documento de datos
#doc = desktop.open_spreadsheet(base_datos.ods)

#Lectura de los datos
#sheet = doc.sheets[0]
#while dato = "":
#	dato = sheet[j,0].value
#	j = j + 1
	#Leemos los datos del .ods
#for r in range(0,j-1):
#	for i in range(0,n[1]-1):
#		z[r+1][i+1] = sheet[r,i].value

#-------------------------------------------------------------
#Inicio del codigo de la neurona
#-------------------------------------------------------------

w = valores_ramdom_w(n)
u = valores_ramdom_u(n)
for h in range(1,len(z)-1):
	a = calculo_neuronas(w,u,z[h],n)
	err = calculo_funcion_error(s,a[4][1])
	err_mod = -err/a[4][1]
	while err_mod > 0.05:
		w = nueva_w_nivel3(w,a,a[4][1],n,alfa,err)
		w = nueva_w_nivel2(w,a,a[4][1],n,alfa,err)
		w = nueva_w_nivel1(w,a,a[4][1],n,alfa,err,z[h])
		u = nueva_u_nivel3(u,a,a[4][1],n,alfa,err)
		u = nueva_u_nivel2(u,a,a[4][1],n,alfa,err)
		u = nueva_u_nivel1(u,a,a[4][1],n,alfa,err,z[h])
		a = calculo_neuronas(w,u,z[h])
		err = calculo_funcion_error(s,a[4][1])
		err_mod = -err/a[4][1]