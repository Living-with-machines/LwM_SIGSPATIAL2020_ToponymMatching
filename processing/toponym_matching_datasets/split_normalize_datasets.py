import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def in_alphabet(source, target, alphabet):
    latin_range = re.compile(u'[\u0040-\u007F\u0080-\u00FF\u0100-\u017F\u0180-\u024F]', flags=re.UNICODE)
    greek_range = re.compile(u'[\u0370-\u03FF\u1F00-\u1FFF]', flags=re.UNICODE)
    if alphabet == "latin":
        if re.search(latin_range, source) and re.search(latin_range, target):
            return True
        else:
            return False
    elif alphabet == "greek":
        if re.search(greek_range, source) and re.search(greek_range, target):
            return True
        else:
            return False
    else:
        return True
    
def normalize(output, dataset, alphabet):
    if type(dataset) == str:
        df_csv = pd.read_csv(dataset, sep="\t", header=None, error_bad_lines=False)
        df_csv = df_csv.iloc[:,0:3]
        df = pd.DataFrame(df_csv.values, columns = ["Source", "Target", "Match"])
    else:
        df = dataset
    df['Match'] = df['Match'].apply(lambda x: str(x).upper())
    df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df['Source'].fillna("", inplace = True)
    df['Target'].fillna("", inplace = True)
    df['Source'].replace(r'^\s\t\n*$', np.nan, inplace=True)
    df['Target'].replace(r'^\s\t\n*$', np.nan, inplace=True)
    df['Source'].replace(" ", np.nan, inplace=True)
    df['Target'].replace(" ", np.nan, inplace=True)
    df['Source'].replace("", np.nan, inplace=True)
    df['Target'].replace("", np.nan, inplace=True)
    df.dropna(subset=['Source'], inplace=True)
    df.dropna(subset=['Target'], inplace=True)
    
    df = df[df.apply(lambda x: in_alphabet(x["Source"], x["Target"], alphabet), axis=1)]
    
    train = df.reset_index(                  # need to keep the index as a column
        ).groupby('Match'                    # split by "group"
        ).apply(lambda x: x.sample(frac=0.9) # in each group, do the random split
        ).reset_index(drop=True              # index now is group id - reset it
        ).set_index('index')                 # reset the original index
    test = df.drop(train.index)              # now we can subtract it from the rest of data
    train = train.sample(frac=1)
    test = test.sample(frac=1)
    train.to_csv("../../datasets/toponym_matching_datasets/" + output + "_trainval.txt", sep="\t", header=False, index=False)
    test.to_csv("../../datasets/toponym_matching_datasets/" + output + "_test.txt", sep="\t", header=False, index=False)
    
# List of tuples, each tuple is a different toponym matching dataset. Tuples are of four elements:
# * Output name of the normalized and split dataset
# * Input name of the dataset
# * Alphabet of the dataset, which at the moment can be:
#   * greek: the dataset will only consist of toponyms containing at least one greek character.
#   * latin: the dataset will only consist of toponyms containing at least one latin character.
#   * empty: the dataset does not filter by alphabet.
datasets = [#("wikigaz_es", 'wikigaz/wikigaz_es_dataset.txt', "latin"),
            #("wikigaz_en", 'wikigaz/wikigaz_en_dataset.txt', "latin"),
            ("wikigaz_el", 'wikigaz/wikigaz_el_dataset.txt', "greek"),
            ("ocr", "ocr/ocr_posneg.tsv", "latin"), 
            ("santos", "santos/dataset-string-similarity.txt", "")]

for d in datasets:
    normalize(d[0], d[1], d[2])