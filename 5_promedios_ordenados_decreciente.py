import numpy as np
import pandas as pd
from datos_procesados import lista_filtrada

promedios_calculados = lista_filtrada["notas"].apply(np.mean).round(1)#calcular promedios

#hacer un data frame con los promedios
promedios = pd.DataFrame({
    "nombre": lista_filtrada["nombre"],
    "promedio": promedios_calculados    
})

promedios = promedios.sort_values(by="promedio", ascending=False)# ordenar de manera decreciente
promedios = promedios.reset_index(drop=True)# reiniciar los índices
print("\n --- Promedios ordenados de forma decreciente: ---")
print(promedios)