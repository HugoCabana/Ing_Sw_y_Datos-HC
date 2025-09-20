# EJERCICIO 5

Para este ejercicio se hicieron algunas funciones nuevas para poder responder preguntas generales sobre todos los parques del dataset dado. Se usó `DictReader` para cargar los datos y `defaultdict` y `Counter` de collections para agrupar y contar más fácil.

## 1. ¿Qué parque tiene más árboles?

Se construye un diccionario donde la clave es el nombre del parque y el valor es una lista con todos sus árboles. Luego, se compara cuántos tiene cada uno y devuelve el/los que más tienen.

```python
def parques_con_mas_arboles(nombre_archivo):
    parques = cargar_todos_los_arboles(nombre_archivo)
    cantidades = {parque: len(lista) for parque, lista in parques.items()}
    max_arboles = max(cantidades.values())
    return [p for p, c in cantidades.items() if c == max_arboles], max_arboles
```

## 2. ¿Qué parque tiene árboles más altos en promedio?

Calculamos el promedio de altura para los árboles de cada parque. Después devuelve el/los que tienen la altura promedio más alta.

```python
def parques_con_arboles_mas_altos_promedio(nombre_archivo):
    parques = cargar_todos_los_arboles(nombre_archivo)
    promedios = {}
    for parque, lista in parques.items():
        alturas = [int(a['altura_tot']) for a in lista if a['altura_tot'].isdigit()]
        if alturas:
            promedios[parque] = sum(alturas) / len(alturas)
    max_prom = max(promedios.values())
    return [p for p, prom in promedios.items() if prom == max_prom], max_prom
```

## 3. ¿Qué parque tiene más variedad de especies?

Usamos un `set` para contar cuántas especies distintas hay en cada parque y devuelve el/los con más variedad.

```python
def parques_con_mas_variedad_especies(nombre_archivo):
    parques = cargar_todos_los_arboles(nombre_archivo)
    variedad = {parque: len(set(a['nombre_com'] for a in lista)) for parque, lista in parques.items()}
    max_variedad = max(variedad.values())
    return [p for p, v in variedad.items() if v == max_variedad], max_variedad
```

## 4. ¿Cuál es la especie más frecuente en toda la ciudad?

Contamos cuántas veces aparece cada especie en todos los parques. La que más aparece es la más frecuente.

```python
def especie_mas_frecuente(nombre_archivo):
    parques = cargar_todos_los_arboles(nombre_archivo)
    contador = Counter()
    for lista in parques.values():
        for arbol in lista:
            contador[arbol['nombre_com']] += 1
    especie, cantidad = contador.most_common(1)[0]
    return especie, cantidad
```

## 5. ¿Cuál es la razón entre especies exóticas y autóctonas?

Contamos cuántos árboles son exóticos y cuántos autóctonos. Después dividimos para obtener la razón.

```python
def razon_exoticas_autocotonas(nombre_archivo):
    parques = cargar_todos_los_arboles(nombre_archivo)
    contador = Counter()
    for lista in parques.values():
        for arbol in lista:
            origen = arbol['origen'].strip().lower()
            if 'exótica' in origen:
                contador['exotica'] += 1
            elif 'autóctona' in origen or 'nativa' in origen:
                contador['autóctona'] += 1
    total_exoticas = contador['exotica']
    total_autoctonas = contador['autóctona']
    if total_autoctonas == 0:
        return float('inf')
    return total_exoticas / total_autoctonas
```
