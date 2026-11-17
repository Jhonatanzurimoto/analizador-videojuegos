"""Analiza el CSV de videojuegos por etapas."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Nivel 1: Preparar el entorno y las rutas
# La ruta se calcula desde la ubicación de este archivo, así el programa
# funciona aunque ejecutes Python desde otra carpeta.
PROJECT_DIR = Path(__file__).resolve().parent
CSV_PATH = PROJECT_DIR / "Documents" / "videojuegos.csv"
CHART_PATH = PROJECT_DIR / "generos.png"


# Nivel 2: Cargar el CSV
def load_data():
    read_csv = pd.read_csv(CSV_PATH)

    return read_csv


# Nivel 3: Explorar y revisar los datos
def inspect_data(df):
    """Muestra una vista general y revisa datos faltantes."""

    # PASO 3.1 — Primeras cinco filas
    # Escribe aquí una instrucción para mostrar las primeras cinco filas de df.
    # Pista: usa el método .head().
    print("\nPrimeras cinco filas:")
    # Aquí va el código
    print(df.head())
    # PASO 3.2 — Nombres de las columnas
    # Escribe aquí una instrucción para mostrar los nombres de las columnas.
    # Pista: consulta el atributo .columns de df.
    print("\nColumnas:")
    # Aquí va el código
    print(df.columns)
    # PASO 3.3 — Cantidad de filas
    # Escribe aquí una instrucción para mostrar cuántas filas tiene df.
    # Pista: df.shape[0] representa el número de filas.
    print("\nCantidad de filas:")
    # Aquí va el código
    print(df.shape[0])
    # PASO 3.4 — Valores vacíos por columna
    # Escribe aquí una instrucción para contar los valores vacíos de cada columna.
    # Pista: combina .isna() con .sum().
    print("\nValores vacíos por columna:")
    # Aquí va el código
    print(df.isna().sum())


# Nivel 4: Analizar los géneros
def analyze_genres(df):
    """Cuenta juegos por género e identifica el más frecuente."""

    # PASO 4.1 — Cuenta los juegos por género.
    # Escribe aquí el cálculo y guarda el conteo en una variable.
    # Pista: identifica primero qué columna contiene el género.
    # Luego piensa cómo resumir categorías repetidas en una tabla.
    # Aquí va el código
    genre_counts = df["genero"].value_counts()
    # PASO 4.2 — Muestra el conteo que calculaste.
    # Pista: el resultado ya está en una variable. ¿Cómo la mostrarías?
    # Aquí va el código
    print(genre_counts)
    # PASO 4.3 — Muestra el género con más juegos y su cantidad.
    # Pista: compara las cantidades y busca la mayor.
    # ¿Qué categoría corresponde a esa cantidad?
    # Aquí va el código
    max_genre = genre_counts.idxmax()
    max_count = genre_counts.max()
    print(f"\nEl género con más juegos es: {max_genre} con {max_count} juegos.")


# Nivel 5: Responder una pregunta propia
def answer_own_question(df):
    """Responde una segunda pregunta elegida por ti."""

    # PASO 5.1 — Elige una pregunta:
    # A) ¿Cuál es la plataforma más común?
    # B) ¿Cuál es la puntuación máxima?
    # C) ¿Qué año tuvo más lanzamientos?
    # Pista: cada pregunta requiere una operación distinta sobre una columna.

    # PASO 5.2 — Escribe aquí el cálculo para responderla.
    # Pista: decide si necesitas contar repeticiones, encontrar un extremo
    # o contar por año.
    # Aquí va el código
    plataforma_mas_comun= df["plataforma"].mode()[0]

    # PASO 5.3 — Muestra el resultado con un mensaje claro.
    # Pista: incluye en la frase tanto la respuesta como su significado.
    # Aquí va el código
    print(f"\n La plataforma mas comun es : {plataforma_mas_comun}")


# Nivel 6: Crear y guardar la gráfica
def plot_genres(df):
    """Crea y guarda una gráfica de barras con los géneros."""

    # PASO 6.1 — Calcula la frecuencia por género (puedes reutilizar el Nivel 4).
    # Pista: para una gráfica de barras necesitas etiquetas y cantidades.
    # Aquí va el código
    genre_counts = df["genero"].value_counts()

    # PASO 6.2 — Crea una gráfica de barras con título y nombres para los ejes.
    # Pista: decide qué categorías van abajo y qué valor representan las barras.
    # Aquí va el código

    bar_plot = genre_counts.plot.bar(title="Distribución de Juegos por Género")
    bar_plot.set_xlabel("Género")
    bar_plot.set_ylabel("Cantidad de juegos")

    # PASO 6.3 — Guarda la gráfica en CHART_PATH y cierra la figura.
    # Pista: busca en matplotlib cómo guardar una figura usando una ruta.
    # Aquí va el código

    plt.savefig(CHART_PATH)
    plt.close()


# Nivel 7: Ejecutar las etapas en orden
def main():
    """Coordina las etapas del análisis."""
    if not CSV_PATH.exists():
        print(f"No se encontró el archivo CSV: {CSV_PATH}")
        return

    df = load_data()
    if df is None:
        print("Completa load_data() para cargar el CSV.")
        return

    inspect_data(df)
    analyze_genres(df)
    answer_own_question(df)
    plot_genres(df)
    print(f"\nGráfica guardada en: {CHART_PATH}")


if __name__ == "__main__":
    main()
