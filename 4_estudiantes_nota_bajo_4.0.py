import pandas as pd
import numpy as np
from datos_procesados import lista_filtrada

#convertir la columna 'notas' en un array de numpy
lista_notas = np.array(lista_filtrada['notas'].tolist(), dtype=object)

#verificar si cada estudiante tiene al menos una nota bajo 4.0
resultados_finales = []
for notas_estudiante in lista_notas:
    #convertir las notas del estudiante en un array de numpy
    notas = np.array(notas_estudiante)
    #comparar si alguna nota es menor a 4.0
    comparacion = notas < 4.0
    #verificar si alguna nota es True (menor a 4.0)
    tiene_nota_bajo_4 = np.any(comparacion)
    #agregar el resultado a la lista de resultados finales
    resultados_finales.append(tiene_nota_bajo_4)
estudiantes_con_nota_baja = np.array(resultados_finales)


#calcular el porcentaje de estudiantes con al menos una nota bajo 4.0
cantidad_de_estudiantes_reprobados = np.sum(estudiantes_con_nota_baja)

#calcular total de estudiantes
total_estudiantes = len(lista_filtrada)

#calcular porcentaje de estudiantes reprobados
porcentaje = (cantidad_de_estudiantes_reprobados / total_estudiantes) * 100

print(f"Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje.round(1)}%")