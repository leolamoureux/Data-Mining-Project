import re
import langdetect
import pandas as pd

def detect_language(text):
    # utiliser une expression régulière pour diviser le texte en phrases
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # initialiser la variable pour stocker le résultat de la détection de langue
    result = {}
    
    # Pour chaque phrase, détecter le langage et mettre à jour le résultat
    for sentence in sentences:
        try:
            language = langdetect.detect(sentence)
            if language in result:
                result[language] += 1
            else:
                result[language] = 1
        except:
            pass
    
    # Trier le résultat par ordre décroissant de fréquence
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    # Retourner le langage le plus fréquent
    return sorted_result[0][0]

# Charger votre dataframe à partir d'un fichier CSV ou d'une autre source de données
df = pd.read_csv("articles.csv")

# Créer une liste de booléens indiquant si chaque tuple doit être conservé ou non
mask = [detect_language(text) == "en" for text in df["text"]]

# Appliquer le masque à votre dataframe
df = df[mask]

# Afficher le nombre de tuples restants
print(len(df))

'''import language_tool_python

def detect_language(text):
  tool = language_tool_python.LanguageTool('en-US')
  matches = tool.check(text)
  language = matches[0].language.locale.language
  return language

text = "The quick brown fox jumps over the lazy dog."
language = detect_language(text)
print(language)  # Output: "en"'''

