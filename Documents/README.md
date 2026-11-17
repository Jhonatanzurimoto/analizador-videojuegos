# Analizador de videojuegos

## ¿Qué hace?

Este proyecto sirve para practicar el análisis de datos con Python. Lee un archivo CSV con información de videojuegos y permitirá explorar sus datos, detectar valores vacíos y resumirlos con una gráfica.

## Datos

- **Archivo:** `Documents/videojuegos.csv`
- **Origen:** datos ficticios preparados para este ejercicio; no representan ventas ni puntuaciones reales.
- **Columnas:** `id`, `titulo`, `genero`, `plataforma`, `anio`, `puntuacion`, `ventas_millones`, `desarrollador`.

Primeras cinco filas:
   id           titulo      genero   plataforma  anio  puntuacion  ventas_millones    desarrollador
0   1   Shadow Circuit      Accion           PC  2021         8.4              1.2        Nova Byte
1   2   Islas de Papel    Aventura       Switch  2020         8.9              2.7  Mar Azul Studio
2   3   Pixel Strikers    Deportes  PlayStation  2022         7.6              1.8     Arcade Forge
3   4      Cafe Nebula  Simulacion           PC  2023         8.1              0.9      Lumen Games
4   5  Reinos Perdidos         RPG         Xbox  2019         9.2              4.1        Iron Leaf

Columnas:
Index(['id', 'titulo', 'genero', 'plataforma', 'anio', 'puntuacion',
       'ventas_millones', 'desarrollador'],
      dtype='str')

Cantidad de filas:
100

Valores vacíos por columna:
id                 0
titulo             0
genero             0
plataforma         0
anio               0
puntuacion         4
ventas_millones    2
desarrollador      6
dtype: int64
genero
Aventura         22
Rompecabezas     17
Simulacion       12
RPG              10
Mundo abierto    10
Accion            8
Carreras          8
Estrategia        8
Deportes          5
Name: count, dtype: int64

El género con más juegos es: Aventura con 22 juegos.

 La plataforma mas comun es : Xbox
