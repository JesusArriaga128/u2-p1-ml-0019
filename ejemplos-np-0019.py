import numpy as np 

califas=np.array([60,70,90])
print("------- ej imprimir califas 1 -------")
print(califas) # Imprime la lista de califas
print(type(califas)) # Muestra el tipo de arreglo 
print("------- ej 0 dimensiones de un array -------")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)
print("------- ej 1 dimension de un array -------")
califas=np.array([60,70,90])
print(califas)
print("Dimension :", califas.ndim)
print("------- ej 2 dimensiones de un array -------")
califas=np.array([
    [60,70,90]
    [50,80,98]
    ]) # un arreglo de dos dimensiones es como una tabla en excel
print(califas)
print("Dimension :", califas.ndim)