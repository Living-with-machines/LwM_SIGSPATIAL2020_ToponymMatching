from pathlib import Path
from shutil import copyfile
import pandas as pd
import numpy as np
import unicodedata
from haversine import haversine
import time
import ast
from sklearn.metrics import average_precision_score
import statistics
  
    
"""
Evaluate ranking for MAP
"""    
def find_closest_distance(altname, gscoords):
    """
    This method returns the distance (in kilometers) between the
    candidate location and the gold standard coordinates. In the
    case that a candidate name in the gazetteer can refer to more
    than one entity, we select the entity closest to the gold
    standard coordinates.
    """
    tCoords = [list(k) for k in altname.values]
    distance = 100000 # we instantiate "distance" with an impossibly large distance
    for candCoord in tCoords:
        candDistance = haversine(candCoord, gscoords)
        if candDistance <= distance:
            distance = candDistance
    return distance


def mapeval_candidates(cand_distance, gazetteer, coords, km, maxCands, metrics, lowercase):
    if type(cand_distance) == list:
        cand_distance = cand_distance[0]
        
    candidates_fd = sorted(cand_distance.items(), key=lambda kv: kv[1])[:maxCands]
    highest = 0.0
    try:
        highest = candidates_fd[-1][1]
    except IndexError:
        highest = 0.0
        
    candidates = []
    for c in candidates_fd:
        candidates.append(c[0])
    
    closest_candidates = []
    for cand in candidates:
        if lowercase:
            candcoords = gazetteer[gazetteer["altname"] == unicodedata.normalize('NFKD', str(cand.lower()))][["lat", "lon"]]
        else:
            candcoords = gazetteer[gazetteer["altname"] == unicodedata.normalize('NFKD', str(cand))][["lat", "lon"]]
        closest_candidates.append(find_closest_distance(candcoords, coords))
    
    y_truearray = []
    y_scorearray = []
    for i in range(len(closest_candidates)):
        if closest_candidates[i] <= km:
            y_truearray.append(1)
        else:
            y_truearray.append(0)
        if metrics == "faiss":
            if highest == 0.0:
                y_scorearray.append(0.0)
            else:
                y_scorearray.append(1.0 - cand_distance[candidates[i]]/highest)
        else:
            y_scorearray.append(1.0 - cand_distance[candidates[i]])
    
    return y_truearray, y_scorearray
    
    
def evaluate_ranking(gazetteer_name, candrank_dataset, deezymatch_model):
    
    maxCands = 20 # Candidates cutoff for MAP
    
#     if not Path("mapped_results/DeezyMapEval_" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model + ".txt", "w").is_file() and not Path("mapped_results/LevDamMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt").is_file() and not Path("mapped_results/ExactMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt").is_file():

    # Load gazetteer (for DeezyMatch)
    gazetteer = pd.read_pickle("../datasets/gazetteers/" + gazetteer_name + ".pkl")
    gazetteer = gazetteer[gazetteer['lat'].notna()]
    gazetteer = gazetteer[gazetteer['lon'].notna()]
    gazetteer["altname"] = gazetteer["altname"].str.normalize("NFKD")

    # Load gazetteer and lower-case it (for LevDam)
    gazetteer_lc = pd.read_pickle("../datasets/gazetteers/" + gazetteer_name + ".pkl")
    gazetteer_lc = gazetteer_lc[gazetteer_lc['lat'].notna()]
    gazetteer_lc = gazetteer_lc[gazetteer_lc['lon'].notna()]
    gazetteer_lc["altname"] = gazetteer_lc["altname"].str.lower().str.normalize("NFKD")

    # Load gold standard dataset
    datasetdf = pd.read_pickle("../datasets/candidate_ranking_datasets/" + candrank_dataset + ".pkl")
    datasetdf = datasetdf[(datasetdf['lat'].notnull()) & (datasetdf['lon'].notnull())]
    datasetdf["toponym"] = datasetdf["toponym"].str.normalize("NFKD")

    # Load DeezyMatch results
    deezyresultsdf = pd.read_pickle("ranker_results/" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model + ".pkl")
    deezyresultsdf["toponym"] = deezyresultsdf["query"].str.normalize("NFKD")

    # List of unique toponyms
    toponyms = list(datasetdf["toponym"].unique())

    # Gold standard dictionary: {toponym: (lat, lon)}
    gold_standard = dict()
    for i, row in datasetdf.iterrows():
        toponym = unicodedata.normalize('NFKD', str(row["toponym"]))
        coords = (row["lat"], row["lon"])
        if candrank_dataset == "wotr_test":
            coords = (float(row["lat"]), float(row["lon"]))
        if toponym in gold_standard:
            if not coords in gold_standard[toponym]:
                gold_standard[toponym].append(coords)
        else:
            gold_standard[toponym] = [coords]

    # Load LevDam results
    levdamresults = pd.read_pickle("levdam_results/" + candrank_dataset + "_" + gazetteer_name + ".pkl")
    levdamresults["toponym"] = levdamresults["toponym"].str.normalize("NFKD")

    mapDeezy = dict()
    mapLevdam = dict()
    mapExact = dict()

    # Store mapped ranking
    with open("mapped_results/DeezyMapEval_" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model + ".txt", "w") as fw1, open("mapped_results/LevDamMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt", "w") as fw2, open("mapped_results/ExactMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt", "w") as fw3:
        for toponym in gold_standard:
            print(toponym)
            toponym = unicodedata.normalize('NFKD', toponym)
            gscoords = gold_standard[toponym]
            gscoords = [coords for coords in gscoords if type(coords[0]) == float and type(coords[1]) == float]
            for coords in gscoords:

                # Deezy: find candidates
                dzcands = deezyresultsdf[deezyresultsdf["toponym"].str.lower().str.contains("^" + toponym.lower() + "$")]

                # LevDam: find candidates
                ldcands = levdamresults[levdamresults["toponym"].str.lower().str.contains("^" + toponym.lower() + "$")]

                # Exact: find candidates
                exact_results = mapeval_candidates({toponym.lower(): 0.0}, gazetteer_lc, coords, 10, maxCands, "", True)

                if not dzcands.empty and not ldcands.empty:
                    deezymap = mapeval_candidates(dzcands.iloc[0]["faiss_distance"], gazetteer, coords, 10, maxCands, "faiss", False)
                    fw1.write(toponym + "\t" + str(coords[0]) + "\t" + str(coords[1]) + "\t" + str(deezymap[0]) + "\t" + str(deezymap[1]) + "\n")

                    levdammap = mapeval_candidates(ldcands.iloc[0]["fuzzyCandidatesLevDam"], gazetteer_lc, coords, 10, maxCands, "levdam", True)
                    fw2.write(toponym + "\t" + str(coords[0]) + "\t" + str(coords[1]) + "\t" + str(levdammap[0]) + "\t" + str(levdammap[1]) + "\n")

                    fw3.write(toponym + "\t" + str(coords[0]) + "\t" + str(coords[1]) + "\t" + str(exact_results[0]) + "\t" + str(exact_results[1]) + "\n")
        
        
"""
Compute the MAP score
"""
def clip_candidates(a, b, numCandidates):
    """
    Clip retrieved candidates to numCandidates or, in case
    one method retrieived a smaller list than numCandidates,
    clip retrieved candidates to the same number as the smaller
    list.
    """
    a = a[:numCandidates]
    b = b[:numCandidates]
    if len(b) <= len(a):
        a = a[:len(b)]
    return a


def map_score(gazetteer_name, candrank_dataset, deezymatch_model, numCandidates):
    dfdeezy = pd.read_csv("mapped_results/DeezyMapEval_" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model + ".txt", sep="\t", index_col=False, header=None, usecols = [0, 1, 2, 3, 4], names = ["toponym", "lat", "lon", "dm_label", "dm_score"], na_filter=True)
    dflevdam = pd.read_csv("mapped_results/LevDamMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt", sep="\t", index_col=False, header=None, usecols = [0, 1, 2, 3, 4], names = ["toponym", "lat", "lon", "ld_label", "ld_score"], na_filter=True)
    dfexact = pd.read_csv("mapped_results/ExactMapEval_" + candrank_dataset + "_" + gazetteer_name + ".txt", sep="\t", index_col=False, header=None, usecols = [0, 1, 2, 3, 4], names = ["toponym", "lat", "lon", "exact_label", "exact_score"], na_filter=True)

    dfboth = pd.merge(dfdeezy, dflevdam, on=['toponym', 'lat', 'lon'])
    
    if numCandidates == 1:
        dfboth = pd.merge(dfboth, dfexact, on=['toponym', 'lat', 'lon'])

    # Remove rows for which we don't have results:
    dfboth = dfboth[dfboth.astype(str)['dm_score'] != '[]']
    dfboth = dfboth[dfboth.astype(str)['ld_score'] != '[]']

    # Convert scores and labels to array
    dfboth['dm_label'] = dfboth['dm_label'].apply(lambda x: ast.literal_eval(x))
    dfboth['dm_score'] = dfboth['dm_score'].apply(lambda x: ast.literal_eval(x))
    dfboth['ld_label'] = dfboth['ld_label'].apply(lambda x: ast.literal_eval(x))
    dfboth['ld_score'] = dfboth['ld_score'].apply(lambda x: ast.literal_eval(x))

    # Calculate average precision score:
    dfboth["dm_ap"] = dfboth.apply(lambda x: average_precision_score(x["dm_label"], x["dm_score"]), axis=1)
    dfboth["ld_ap"] = dfboth.apply(lambda x: average_precision_score(x["ld_label"], x["ld_score"]), axis=1)

    # Remove lines if there is no correct match in the first twenty candidates neither in DM or in LD:
    dfboth = dfboth.dropna(subset=["dm_ap", "ld_ap"], how='all')
    
    # Clip number of candidates:
    dfboth['dm_label'] = dfboth.apply(lambda x: clip_candidates(x['dm_label'], x['ld_label'], numCandidates), axis=1)
    dfboth['dm_score'] = dfboth.apply(lambda x: clip_candidates(x['dm_score'], x['ld_score'], numCandidates), axis=1)
    dfboth['ld_label'] = dfboth.apply(lambda x: clip_candidates(x['ld_label'], x['dm_label'], numCandidates), axis=1)
    dfboth['ld_score'] = dfboth.apply(lambda x: clip_candidates(x['ld_score'], x['dm_score'], numCandidates), axis=1)

    # Calculate average precision score:
    dfboth["dm_ap"] = dfboth.apply(lambda x: average_precision_score(x["dm_label"], x["dm_score"]), axis=1)
    dfboth["ld_ap"] = dfboth.apply(lambda x: average_precision_score(x["ld_label"], x["ld_score"]), axis=1)
    
    # Otherwise, convert nan to zeros:
    dfboth["ld_ap"] = dfboth["ld_ap"].fillna(0)
    dfboth["dm_ap"] = dfboth["dm_ap"].fillna(0)
    
    if numCandidates == 1:
        dfboth['exact_label'] = dfboth['exact_label'].apply(lambda x: ast.literal_eval(x))
        dfboth['exact_score'] = dfboth['exact_score'].apply(lambda x: ast.literal_eval(x))
        dfboth["exact_ap"] = dfboth.apply(lambda x: average_precision_score(x["exact_label"], x["exact_score"]), axis=1)
        dfboth["exact_ap"] = dfboth["exact_ap"].fillna(0)
        print("EXACT P@1", round(dfboth.exact_ap.mean(),2))
        print("DM P@1", round(dfboth.dm_ap.mean(),2))
        print("LD P@1", round(dfboth.ld_ap.mean(),2))
    else:
        print("DM MAP", round(dfboth.dm_ap.mean(),2))
        print("LD MAP", round(dfboth.ld_ap.mean(),2))
        
    print()