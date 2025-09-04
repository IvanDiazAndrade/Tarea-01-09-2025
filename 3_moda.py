import pandas as pd
import numpy as np
from datos_procesados import lista_filtrada

notas = lista_filtrada.explode("notas") #cada nota en una fila
moda = notas["notas"].mode()#calcular moda/s

if len(moda) == 1:
    print(f"La moda (nota mas repetida) es: {moda.iloc[0]}")#si hay una sola moda
else:
    print(f"Las modas (notas mas repetidas) son: {', '.join(map(str, moda.values))}")#si hay más de una moda