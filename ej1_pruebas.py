#%%
from ej1 import suma, resta, generar_lista_al_azar, primer_minimo_menor_que, factorial

#%% a- descomentar las siguientes líneas y correr el código
v1 = 5
v2 = 16
resultado = suma(v1, v2)
print(f"El resultado de la suma entre {v1} y {v2} es: {resultado}")

#%% b- descomentar las siguientes líneas y correr el código
resultado = resta(v1, v2)
print(f"El resultado de a {v1} restarle {v2} es: {resultado}")

#%% c- descomentar las siguientes líneas y correr el código
resultado = factorial(0)
print(f"El resultado de calcular el factorial de 0 es: {resultado}")

# %% d- descomentar las siguientes líneas y correr el código
l1 = generar_lista_al_azar(10, 42)
print(f"Lista generada aleatoriamente: {l1}")
resultado = primer_minimo_menor_que(5, l1)
print(f"El primer mínimo menor a 5 de la lista es: {resultado}")

l2 = generar_lista_al_azar(10, 1)
print(f"Lista generada aleatoriamente: {l2}")
resultado = primer_minimo_menor_que(5, l2)
print(f"El primer mínimo menor a 5 de la lista es: {resultado}")

l3 = generar_lista_al_azar(10)
print(f"Lista generada aleatoriamente: {l3}")
resultado = primer_minimo_menor_que(5, l3)
print(f"El primer mínimo menor a 5 de la lista es: {resultado}")

l4 = [54, 18, 13, 7, 15]
print(f"Lista original: {l4}")
resultado = primer_minimo_menor_que(10, l4)
print(f"El primer mínimo menor a 10 de la lista es: {resultado}")

resultado = primer_minimo_menor_que(5, l4)
print(f"El primer mínimo menor a 5 de la lista es: {resultado}")


#%% e- descomentar las siguientes líneas y correr el código
for i in range(10):
    resultado = factorial(i)
    print(f"El resultado de calcular el factorial de {i} es: {resultado}")


