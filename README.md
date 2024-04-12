# 2022-S2 Quiz 2

## Instrucciones Generales
- El archivo **debe** llamarse **Quiz2.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación iterativa usando **WHILE o FOR**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

##numeroALista(num) (5 puntos)
- La función retornará una lista donde cada una de las posiciones de la lista será para cada uno de los dígitos del número multiplicado por la cantidad de dígitos de **num**
- El parámetro **num** debe ser Entero , puede ser positivo como negativo

```python
>>> numeroALista(256)
[18, 15, 6]
>>> numeroALista(2552)
[8, 20, 20, 8]
>>> numeroALista(0)
[0]
>>> numeroALista(-8018)
["-", 32, 4, 0, 32]
```

##listaMayoresMenores(num) (5 puntos)
- Separar los dígitos de un número en dos listas, una para solo los dígitos mayores a 4 y la otra lista para los menores a 5
- **num** debe ser entero y mayor a 0

```python
>>> listaMayoresMenores(256)
[[2], [5, 6]]
>>> listaMayoresMenores(2552)
[[2, 2], [5, 5]]
>>> listaMayoresMenores("25.52")
"Error: Tipo de dato no permitido "
```
