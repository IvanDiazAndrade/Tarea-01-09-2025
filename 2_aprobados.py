import pandas as pd
import numpy as np
from datos_procesados import lista_filtrada

lista_notas = np.array(lista_filtrada['notas'].tolist(), dtype=object)#convertir la columna 'notas' en objetos dentro de una lista


resultados_finales = [] #lista contadora de booleanos
for notas_estudiante in lista_notas:
    notas = np.array(notas_estudiante)#pasar las notas a un lista
    comparacion = notas >= 4.0
    ramos_aprobados= np.all(comparacion)#ver si todas las notas son aprobadas
    resultados_finales.append(ramos_aprobados)#agregar el resultado a la lista

cantidad_aprobados = np.sum(resultados_finales)#sumar la lista

print("\nCantidad de estudiantes que aprobaron todas sus materias:", cantidad_aprobados)

