# 2024-S1 Quiz 3

## Instrucciones Generales
- El archivo **debe** llamarse **Quiz3.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación iterativa usando **WHILE o FOR**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

## numeroALista(num) (5 puntos)
- La función retornará una lista donde cada una de las posiciones de la lista será para cada uno de los dígitos del número multiplicado por la cantidad de dígitos de **num**
- El parámetro **num** debe ser Entero , puede ser positivo como negativo
- Ejemplo, sea el número 256, tiene un largo de 3 dígitos, por lo tanto, cada dígito de 256 se multiplicará por 3
- Dando como resultado [2 * 3, 5 * 3, 6 * 3] => [6,15,18]

```python
>>> numeroALista(256)
[6,15,18]
>>> numeroALista(2552)
[8, 20, 20, 8]
>>> numeroALista(0)
[0]
>>> numeroALista(-8018)
[-32, 0, -4, -32]
```

## listaMayoresMenores(num) (5 puntos)
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

## aplanarLista(lista) (5 puntos)
- Dado una lista que contenga, numeros o lista, retornar una lista  que solo contenga los valores sin las sublistas
- **lista** debe ser no vacio y sus valores son enteros

```python
>>> aplanarLista([[12,50,80],[2,8,6,7]])
[12,50,80,2,8,6,7]
>>> aplanarLista([[12,50,80],15,0,[2,8,6,7]])
[12,50,80,15,0,2,8,6,7]
>>> aplanarLista([3,6,9,12])
[3,6,9,12]
```

## convertirSubListas(lista) (5 puntos)
- Dado una lista que contenga solo números enteros, retornar una lista en donde los nuúmero estará organizados en sublistas
- La cantidad de sublistas estará determinado por el valor de un número al cuadrado cuyo resultado es más cercano al largo de la lista original
- **lista** debe ser no vacio y sus valores son enteros
- Ejemplo:
  - convertirSubListas([12,50,80,2,8,6,7])
  - Esta lista tiene un largo de 7
  - El resultado de una valor al cuadrado sería 4, es decir 2 ** 2 , es 4 y este es un valor menor a 7 que sería el largo de la lista
  - Por lo tanto el resultado es
  - [[12,50], [80,2]] 

```python
>>> convertirSubListas([12,50,80,2,8,6,7])
[[12,50], [80,2]] 
>>> convertirSubListas([12,50,80,2,10,42,8,6,7])
[[12,50,80], [2,10,42], [8,6,7]] 
```
