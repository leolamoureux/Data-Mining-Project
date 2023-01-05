import time
import langdetect
import pandas as pd

def detect_language(text):
    return langdetect.detect(text)

if __name__ == "__main__":
    # Obtenir le temps courant avant l'exécution du script
    start_time = time.perf_counter()

    df = pd.read_csv('articles.csv')
    print("Nombre d'inputs avant suppression des textes non anglais : " + str(len(df)))
    
    # créer une liste vide qui contiendra les indices des lignes à supprimer
    indexes_to_delete = []

    # parcourir chaque ligne du dataframe
    for index, row in df.iterrows():

        lang = detect_language(row['text'][0:200])
        # si la valeur de l'attribut 'text' commence par un 'm'
        if lang != 'en':
        # ajouter l'index de cette ligne à la liste des indices à supprimer
            indexes_to_delete.append(index)

    # supprimer les lignes du dataframe en utilisant la liste des indices à supprimer
    df.drop(indexes_to_delete, inplace=True)

    print("Nombre d'inputs après suppression des textes non anglais : " + str(len(df)))

    # Obtenir le temps courant après l'exécution du script
    end_time = time.perf_counter()

    # Calculer le temps d'exécution en secondes
    elapsed_time = end_time - start_time
    print("Temps d'exécution :", elapsed_time, "secondes")