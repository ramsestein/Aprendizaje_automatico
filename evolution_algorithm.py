import random

def individual(min, max,largo,modelo):
    #Crea el individuo aleatorio
    return[random.randint(min, max) for i in range(largo)]
 
def crearPoblacion(num,largo,modelo,rango_min,rango_max):
    #Crea la poblacion con individuos aleatorios
    return [individual(rango_min,rango_max,largo,modelo) for i in range(num)]
 
def calcularFitness(individual,modelo):
    #Puntos fitness por comparacion con modelo 
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
 
    return fitness
 
def selection_and_reproduction(population,modelo,pressure,largo):
    #Igual a selection_and_control, cambiando el fitness
    puntuados = [ (calcularFitness(i,modelo), i) for i in population] 
    puntuados = [i[1] for i in sorted(puntuados)] 
    population = puntuados
    selected =  puntuados[(len(puntuados)-pressure):]
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1) 
        padre = random.sample(selected, 2)
        population[i][:punto] = padre[0][:punto]
        population[i][punto:] = padre[1][punto:]
 
    return population 

def selection_and_control(population,modelo,pressure,largo):
    puntuados = [ (fitnessNormas(i,modelo), i) for i in population] 
    puntuados = [i[1] for i in sorted(puntuados)] #Ordena los pares ordenados y se queda solo con el array de valores
    population = puntuados
    #Selecciona los 'n' individuos del final, donde n 'pressure'
    selected =  puntuados[(len(puntuados)-pressure):] 
 
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1) #Punto Crossover
        padre = random.sample(selected, 2) #Se eligen dos padres
        population[i][:punto] = padre[0][:punto]#Se ejecuta el crossover
        population[i][punto:] = padre[1][punto:]
 
    return population
 
def mutation(population,mutation_chance,largo,pressure):
    for i in range(len(population)-pressure):
        if random.random() != mutation_chance: 
            punto = random.randint(1,largo-1) #Se elige un punto al azar
            nuevo_valor = random.randint(1,9)
 
            #Mira que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1,9)
 
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
 
    return population 
 
def newControl (modelo,rango_min,rango_max,num,pressure,mutation_chance,ciclos):
        #Funcion que devuelve valores que cumplan con las variables preestablecidas	
        #Recoge todas las variables
	largo = len(modelo)
	#Crea la poblacion
	population = crearPoblacion(num,largo,modelo,rango_min,rango_max)
	for i in range(ciclos):
    		population = selection_and_control(population,modelo,pressure,largo)
    		population = mutation(population,mutation_chance,largo,pressure)
 	return population

def fitnessNormas(individual,modelo):
    #Puntos fitness basados en el cumplimiento o incumplimiento de una serie de premisas preestablecidas
    fitness = 0


    #Aqui debe incluirse el codigo de las normas que deben cumplirse
    #Aunque solo sean dos valores a estudio, como el siguiente codigo, se debe repetir varias veces en la misma array en diferentes partes de la misma (curiosamente al igual que el codigo genetico real) pues permite mejor asentamiento de las mutaciones y da estabilidad a los ciclos
    if ((individual[13]*5) + individual[14] >= 15) and ((individual[13]*5) + individual[14] <= 17):
	fitness += 1
    if ((individual[13]*4) + individual[14] >= 12) and ((individual[13]*4) + individual[14] <= 14):
	fitness += 1
    if ((individual[13]*3) + individual[14] >= 9) and ((individual[13]*3) + individual[14] <= 11):
	fitness += 1
    if ((individual[13]*2) + individual[14] >= 6) and ((individual[13]*2) + individual[14] <= 8):
	fitness += 1
    if (individual[13] + individual[14] >= 4) and (individual[13] + individual[14] <= 6):
	fitness += 1


    if ((individual[9]*5) + individual[10] >= 15) and ((individual[9]*5) + individual[10] <= 17):
	fitness += 1
    if ((individual[9]*4) + individual[10] >= 12) and ((individual[9]*4) + individual[10] <= 14):
	fitness += 1
    if ((individual[9]*3) + individual[10] >= 9) and ((individual[9]*3) + individual[10] <= 11):
	fitness += 1
    if ((individual[9]*2) + individual[10] >= 6) and ((individual[9]*2) + individual[10] <= 8):
	fitness += 1
    if (individual[9] + individual[10] >= 4) and (individual[9] + individual[10] <= 6):
	fitness += 1


    if ((individual[5]*5) + individual[6] >= 15) and ((individual[5]*5) + individual[6] <= 17):
	fitness += 1
    if ((individual[5]*4) + individual[6] >= 12) and ((individual[5]*4) + individual[6] <= 14):
	fitness += 1
    if ((individual[5]*3) + individual[6] >= 9) and ((individual[5]*3) + individual[6] <= 11):
	fitness += 1
    if ((individual[5]*2) + individual[6] >= 6) and ((individual[5]*2) + individual[6] <= 8):
	fitness += 1
    if (individual[5] + individual[6] >= 4) and (individual[5] + individual[6] <= 6):
	fitness += 1


    if ((individual[1]*5) + individual[2] >= 15) and ((individual[1]*5) + individual[2] <= 17):
	fitness += 1
    if ((individual[1]*4) + individual[2] >= 12) and ((individual[1]*4) + individual[2] <= 14):
	fitness += 1
    if ((individual[1]*3) + individual[2] >= 9) and ((individual[1]*3) + individual[2] <= 11):
	fitness += 1
    if ((individual[1]*2) + individual[2] >= 6) and ((individual[1]*2) + individual[2] <= 8):
	fitness += 1
    if (individual[1] + individual[2] >= 4) and (individual[1] + individual[2] <= 6):
	fitness += 1


    #Codigo insertado de normas hasta aqui
    return fitness






#Codigo de ejecucion
array = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
resultado = []

resultado = newControl(array,1,9,15,4,0.4,1000000)


print("Poblacion Inicial:")
print(array)
print("Poblacion Final:")
print(resultado)

