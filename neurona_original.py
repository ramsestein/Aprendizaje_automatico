import random

def recalcularPesos(pesos,ti,xi):
	wj = pesos+0.5*ti*xi
	return wj
  
def pesosAleatorios(pesos):
	for i in range(len(pesos)):
		pesos[i] = random.random()
		print "peso"
		print pesos[i]

def aprendizaje(entradas,salidas,pesos):
	pesosAleatorios(pesos)
	yi= 0
	i = 0
	while i < len(entradas):
		yi = pesos[0]*entradas[0] + pesos[1]*entradas[1] + pesos[2]*entradas[2] + pesos[3]*entradas[3]
		if yi >= 0:
			yi = 1
		else:
			yi = -1
		if yi == salidas[i]:
			print "correcto",salidas[i],"=",yi
			for m in range(len(pesos)):
				pesos[m] = recalcularPesos(pesos[m],salidas[i],entradas[m])
				print pesos[m]
		else:
			print "incorrecto",salidas[i],"=",yi
			for k in range(len(pesos)):
				pesos[k] = recalcularPesos(pesos[k],salidas[i],entradas[k])
				print pesos[k]
		i = i+1






salidas = [1,-1,-1,-1]
entradas = [1,-4,-1,9]
pesos = [0,0,0,0]
aprendizaje(entradas,salidas,pesos)


