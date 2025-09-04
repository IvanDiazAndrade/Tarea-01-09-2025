import pandas as pd
import numpy as np

#intentar importar la lista de estudiantes desde el archivo datos_sin_procesar
try:
     #asegúrate de que este archivo exista y contenga la lista "estudiantes"
    from datos_sin_procesar import estudiantes
except ImportError:
    print(" El archivo o la lista no existen.")
else:
     #verificar si la lista está vacía
    if not estudiantes: 
        print("La lista 'estudiantes' está vacía.")
    else:
        #convertir "estudiantes" a DataFrame
        lista_filtrada = pd.DataFrame(estudiantes)