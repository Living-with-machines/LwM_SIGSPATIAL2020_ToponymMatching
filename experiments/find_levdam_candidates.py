from pathlib import Path
import pandas as pd
import numpy as np
import time

from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance_ndarray

"""
Find candidates with Levenshtein-Damerau
"""
def fuzzyCandidatesLevDam(toponym, unique_placenames, n, cutoff, stored_levdam):
    toponym = toponym.lower()
    close_altnames = {}
    if not toponym in stored_levdam:
        #cutoff = 1.0 - cutoff # 0.0 means that the sequences are identical, while 1.0 means that they have nothing in common.
        levdist = normalized_damerau_levenshtein_distance_ndarray(toponym.lower(), unique_placenames).tolist()
        zippedl = list(zip(unique_placenames, levdist))
        sortedl = sorted(zippedl, key=lambda x: round(x[1], 4))
        for x in sortedl:
            if x[1] > cutoff:
                break
            close_altnames[x[0]] = round(x[1], 4)
        stored_levdam[toponym] = close_altnames
    else:
        close_altnames = stored_levdam[toponym]
    return [close_altnames], stored_levdam

def find_levdam_candidates(gazetteer, candrank_dataset):
    
    if not Path("levdam_results/" + candrank_dataset + "_" + gazetteer + ".pkl").is_file():
        start_time = time.time()

        df_candidates = pd.read_pickle("../datasets/candidate_ranking_datasets/" + candrank_dataset + ".pkl")
        df_candidates = df_candidates.filter(['toponym'])
        list_ids = df_candidates.index.values

        unique_placenames_array = []
        with open("../datasets/candidate_mentions_sets/" + gazetteer + ".txt") as fr:
            lines = fr.readlines()
            for line in lines:
                x = line.split("\t0\tfalse")[0]
                unique_placenames_array.append(x.lower())

        stored_levdam = {}
        unique_placenames_array = list(set(unique_placenames_array))
        unique_placenames_array = np.array(unique_placenames_array)
        for i, row in df_candidates.iterrows():
            if i % 50 == 0:
                print(i)
            df_candidates.loc[i, 'fuzzyCandidatesLevDam'], stored_levdam = fuzzyCandidatesLevDam(row['toponym'], unique_placenames_array, 0, 0.45, stored_levdam)

        df_candidates.to_pickle("levdam_results/" + candrank_dataset + "_" + gazetteer + ".pkl")

        elapsed = time.time() - start_time
        print("TOTAL TIME: %s" % elapsed)