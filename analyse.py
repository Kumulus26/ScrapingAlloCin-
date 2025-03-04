import pandas as pd
import matplotlib.pyplot as plt

def analyse_film_data():
    df = pd.read_excel("data/AlloCiné_Classement_Film.xlsx")

    df["Durée (min)"] = pd.to_numeric(df["Durée (min)"], errors='coerce')

    df.dropna(subset=["Durée (min)"], inplace=True)

    plt.figure(figsize=(10, 5))
    plt.hist(df["Durée (min)"], bins=15, edgecolor="black")
    plt.xlabel("Durée en minutes")
    plt.ylabel("Nombre de films")
    plt.title("Distribution des durées des films")

    plt.savefig("data/histogramme_duree.png")
    plt.show(block=True)