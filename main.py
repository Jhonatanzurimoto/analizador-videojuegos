from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
CSV_PATH = PROJECT_DIR / "Documents" / "videojuegos.csv"
CHART_PATH = PROJECT_DIR / "generos.png"


def load_data():
    read_csv = pd.read_csv(CSV_PATH)

    return read_csv


def inspect_data(df):

    print(df.head())

    print(df.columns)

    print(df.shape[0])

    print(df.isna().sum())


def analyze_genres(df):
    genre_counts = df["genero"].value_counts()
    print(genre_counts)
   
    max_genre = genre_counts.idxmax()
    max_count = genre_counts.max()
    print(f"\nEl género con más juegos es: {max_genre} con {max_count} juegos.")

def answer_own_question(df):
    plataforma_mas_comun= df["plataforma"].mode()[0]
    print(f"\n La plataforma mas comun es : {plataforma_mas_comun}")

def plot_genres(df):
    genre_counts = df["genero"].value_counts()


    bar_plot = genre_counts.plot.bar(title="Distribución de Juegos por Género")
    bar_plot.set_xlabel("Género")
    bar_plot.set_ylabel("Cantidad de juegos")

    plt.savefig(CHART_PATH)
    plt.close()

def main():
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
