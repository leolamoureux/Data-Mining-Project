import os
import pandas as pd
import chardet
import re

base_path = "/Users/leolamoureux/Downloads/BBC_News_Summary2" # replace with the path to the root folder

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def remove_invalid_byte(text):
    pattern = re.compile('[^\x00-\x7f]')
    return pattern.sub('', text)

data = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".txt"):
            # read the text from the file

            with open(os.path.join(root, file), "r", encoding=detect_encoding(os.path.join(root, file)), errors='ignore') as f:
                text = f.read()
                text = remove_invalid_byte(text)

                
            # get the topic from the folder name
            topic = root.split("/")[-1]

            # check if the file is a summary or an article
            if "Summaries" in root:
                summary_num = file.split(".")[0]
                article_file = f"{summary_num}.txt"
                article_path = os.path.join(root.replace("Summaries", "News_Articles"), article_file)
                with open(article_path, "r", encoding=detect_encoding(article_path), errors='ignore') as f:
                    article = f.read()
                    article = remove_invalid_byte(article)
                data.append({"article": article, "summary": text, "topic": topic})

# create the dataframe
df = pd.DataFrame(data)
df.to_csv("BBC_df.csv", index=False)