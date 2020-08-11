from random import random

def recalcularPesos(pesos,ti,xi):
	wj = pesos+0.5*ti*xi
	return wj

def integracion(entradas):
	valor_conteo = len(entradas)
	valor_final = 0
	integrado = []
	#Suaviza la curva del array, aumenta su numero de valores
	while i <= len(entradas):
		if i = len(entradas):
			integrado[i] = entradas[i]
			i++
		else:
			integrado[i] = (entradas[i]+entradas[i+1])/2
			i++
	#Busca el valor mas bajo del array a lo chungo
	for m in range(len(integrado)-1):
		if integrado[m] < integrado[m+1]:
			valor_final = integrado[m]
		else:
			valor_final = integrado[m+1]
	#Divide todos por el minimo valor
	for n in range(len(integrado)):
		integrado[n] = integrado[n]/valor_final
	#Devuelve el array trabajado
	return integrado


def busqueda(entradas,grado):
	integrado = []
	#Las neuronas primero integran la información, suavizan las curvas de datos
	#Reducción a minimo exponente
	integrado = integracion(entradas)
	#Buscamos los puntos de corte porcentuales
	#Buscamos el limite superior de los valores de la array, el inferior es 1
	for m in range(len(integrado)-1):
		if integrado[m] > integrado[m+1]:
			valor_alto = integrado[m]
		else:
			valor_alto = integrado[m+1]
	#Cuando multipliquemos valor_alto por grado podremos dar la sensibilidad a la busqueda
	sensibilidad = valor_alto*grado
	#Separamos los valores ruido de lo que queremos
	for n in range(len(integrado)):
		if integrado[n] < sensibilidad:
			integrado[n] = 0
		else:
			integrado[n] = 1
	return integrado

def aprendizaje(entradas,salidas):
	pesos[]
	#Calcula los pesos aleatorios
	for g in range(len(entradas)):
		pesos[g] = random.random()
		print "peso"
		print pesos[g]
	yi= 0
	i = 0
	while i < len(entradas):
		#Coge los pesos para cada par de valores y se los suma a yi
		for s in range(len(entradas))
			yi = yi + pesos[s]*entradas[s]
		#Usa Perceptron
		if yi >= 0:
			yi = 1
		else:
			yi = 0
		if yi == salidas[i]:
			print "correcto",salidas[i],"=",yi
			print pesos
		else:
			print "incorrecto",salidas[i],"=",yi
			for k in range(len(pesos)):
				pesos[k] = recalcularPesos(pesos[k],salidas[i],entradas[k])
			print pesos
		i = i+1



entradas = [20,15,25,33,42,45,54,67,68,65,120,230,301,320,400,421,420,423,430,410,20,15]
grado = 0.9
salidas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0]
resultado = busqueda(entradas,grado)
aprendizaje(resultado,salidas)


