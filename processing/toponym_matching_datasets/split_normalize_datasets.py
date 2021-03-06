import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# List of tuples, each tuple is a different toponym matching dataset. Tuples are of four elements:
# * Output name of the normalized and split dataset
# * Input name of the dataset
# * Alphabet of the dataset, which at the moment can be:
#   * greek: the dataset will only consist of toponyms containing at least one greek character.
#   * latin: the dataset will only consist of toponyms containing at least one latin character.
#   * empty: the dataset does not filter by alphabet.
datasets = [("wikigaz_el", 'wikigaz/wikigaz_el_dataset.txt', ""),
            ("wikigaz_es", 'wikigaz/wikigaz_es_dataset.txt', ""),
            ("wikigaz_en", 'wikigaz/wikigaz_en_dataset.txt', ""),
            ("ocr", "ocr/ocr_posneg.tsv", ""), 
            ("santos", "santos/dataset-string-similarity.txt", "")]

output_directory = "../../datasets/toponym_matching_datasets/"

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
    
def normalize(output_name, dataset, alphabet):
    if type(dataset) == str:
        df_csv = pd.read_csv(dataset, sep="\t", header=None, error_bad_lines=False)
        df_csv = df_csv.iloc[:,0:3]
        df = pd.DataFrame(df_csv.values, columns = ["Source", "Target", "Match"])
    else:
        df = dataset
    
    # Normalize rows:
    df['Match'] = df['Match'].apply(lambda x: str(x).upper()) # Uppercase Match column
    df.applymap(lambda x: x.strip() if isinstance(x, str) else x) # Strip all strings
    df['Source'].fillna("", inplace = True) # Turn NaN values to empty strings in Source
    df['Target'].fillna("", inplace = True) # Turn NaN values to empty strings in Target
    # Convert empty strings to NaN
    df['Source'].replace(r'^\s\t\n*$', np.nan, inplace=True)
    df['Target'].replace(r'^\s\t\n*$', np.nan, inplace=True)
    df['Source'].replace(" ", np.nan, inplace=True)
    df['Target'].replace(" ", np.nan, inplace=True)
    df['Source'].replace("", np.nan, inplace=True)
    df['Target'].replace("", np.nan, inplace=True)
    # And drop them from the dataframe
    df.dropna(subset=['Source'], inplace=True)
    df.dropna(subset=['Target'], inplace=True)
    print(df.Match.value_counts())
    
    # Drop duplicates (including reverse duplicates)
    df['check_string'] = df.apply(lambda row: ''.join(sorted([row['Source'], row['Target']])), axis=1)
    print(df.Match.value_counts())
    
    duplicates = df[df.duplicated(subset=['check_string'])]
    true_duplicates = duplicates[duplicates["Match"] == "TRUE"]
    false_duplicates = duplicates[duplicates["Match"] == "FALSE"]
    
    df = df.drop_duplicates('check_string')
    df = df.drop(columns=['check_string'])
    
    true_duplicates = true_duplicates.drop(columns=['check_string'])
    false_duplicates = false_duplicates.drop(columns=['check_string'])
    
    true_duplicates_indices = true_duplicates.set_index(["Source"]).index
    false_duplicates_indices = false_duplicates.set_index(["Source"]).index

    df_true = df[df["Match"] == "TRUE"]
    df_false = df[df["Match"] == "FALSE"]

    true_pairs_indices = df_true.set_index(["Source"]).index
    false_pairs_indices = df_false.set_index(["Source"]).index
    
    df_true2drop = df_true[true_pairs_indices.isin(false_duplicates_indices)]
    df_false2drop = df_false[false_pairs_indices.isin(true_duplicates_indices)]
    
    i = 0
    df2drop = pd.DataFrame(columns = ["Source", "Target", "Match"])
    for fd in false_duplicates.Source.to_list():
        i += 1
        try:
            df2drop = df2drop.append(df_true2drop[df_true2drop["Source"] == fd].tail(1))
        except ValueError:
            pass
        if i % 5000 == 0:
            print(i)
            
    i = 0
    for td in true_duplicates.Source.to_list():
        i += 1
        try:
            df2drop = df2drop.append(df_false2drop[df_false2drop["Source"] == td].tail(1))
        except ValueError:
            pass
        if i % 5000 == 0:
            print(i)
    
    df_index = df.set_index(["Source", "Target", "Match"]).index
    df2drop_index = df2drop.set_index(["Source", "Target", "Match"]).index
    
    mask = ~df_index.isin(df2drop_index)
    df = df.loc[mask]
    
    # Force a balanced dataset between TRUE and FALSE classes:
    min_value = min(list(df.Match.value_counts().to_dict().values()))
    df_true_min = df[df["Match"] == "TRUE"].sample(n = min_value)
    df_false_min = df[df["Match"] == "FALSE"].sample(n = min_value)
    df = pd.concat([df_true_min, df_false_min])
    
    # Filter out strings according to in_alphabet function:
    df = df[df.apply(lambda x: in_alphabet(x["Source"], x["Target"], alphabet), axis=1)]
    print(df.Match.value_counts())
    
    # Split the dataframe (0.9 for train and validation, 0.1 for test)
    train = df.reset_index(                  # need to keep the index as a column
        ).groupby('Match'                    # split by "group"
        ).apply(lambda x: x.sample(frac=0.9) # in each group, do the random split
        ).reset_index(drop=True              # index now is group id - reset it
        ).set_index('index')                 # reset the original index
    test = df.drop(train.index)              # now we can subtract it from the rest of data
    train = train.sample(frac=1)
    test = test.sample(frac=1)
    train.to_csv(output_directory + output_name + "_trainval.txt", sep="\t", header=False, index=False)
    test.to_csv(output_directory + output_name + "_test.txt", sep="\t", header=False, index=False)
    print()

for d in datasets:
    normalize(d[0], d[1], d[2])