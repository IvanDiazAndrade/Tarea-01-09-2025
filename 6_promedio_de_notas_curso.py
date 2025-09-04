import numpy as np
import pandas as pd
from datos_procesados import lista_filtrada

promedios_calculados = lista_filtrada["notas"].apply(np.mean).round(1)#calcular promedios

#hacer un data frame con los promedios
promedio_alumnos = pd.DataFrame({
    "nombre": lista_filtrada["nombre"],
    "promedio": promedios_calculados    
})

promedio_curso = promedio_alumnos["promedio"].mean().round(1)#calcular promedio del curso
print(f"El promedio de notas del curso es de: {promedio_curso}")