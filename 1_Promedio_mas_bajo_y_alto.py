import numpy as np
import pandas as pd
from datos_procesados import lista_filtrada

#calcular el promedio de las notas para cada estudiante y redondear a un decimal
promedios_calculados = lista_filtrada["notas"].apply(np.mean).round(1)

#crear un nuevo DataFrame con los nombres y sus promedios
promedios = pd.DataFrame({
    "nombre": lista_filtrada["nombre"],
    "promedio": promedios_calculados
})

#promedio mas alto
 #encontrar el índice del promedio más alto
indice_maximo = promedios['promedio'].idxmax()
 #obtener la fila con el promedio más alto
promedio_mas_alto = promedios.loc[indice_maximo]

#promedio mas bajo
 #encontrar el índice del promedio más bajo
indice_minimo = promedios['promedio'].idxmin()
 #obtener la fila con el promedio más bajo
promedio_mas_bajo = promedios.loc[indice_minimo]

print(f"🥇 Promedio más alto: {promedio_mas_alto['nombre']} con un {promedio_mas_alto['promedio']}")
print(f"📉 Promedio más bajo: {promedio_mas_bajo['nombre']} con un {promedio_mas_bajo['promedio']}")