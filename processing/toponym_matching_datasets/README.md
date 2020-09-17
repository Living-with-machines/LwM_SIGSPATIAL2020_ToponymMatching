# Datasets for toponym matching evaluation

This folder contains the code and instructions to create the datasets used for evaluation of toponym matching (`WG:en`, `WG:es`, `WG:el`, and `OCR` datasets). The resulting datasets can be found ***[ADD LINK WITH FINAL RESOURCES]***. Read the instructions below to create them from scratch.

## WikiGaz

* [`generate_wikigaz_comb.py`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/toponym_matching_datasets/wikigaz/generate_wikigaz_comb.py): This script assumes the user has already generated the WikiGazetteers in steps [`generate_wikigazetteers.ipynb`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/gazetteers/generate_wikigazetteers.ipynb) and [`prepare_gazetteers.ipynb`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/gazetteers/prepare_gazetteers.ipynb). This results in three dataframes (`wikiGaz_en_filtered.pkl`, `wikiGaz_es_filtered.pkl`, and `wikiGaz_el_filtered.pkl`, stored in `processing/resources/`) with the following columns: `index`, `name`, `wikititle`, `latitude`, `longitude`, `source`.

    |        | name      | wikititle | latitude | longitude | source      |
    | ------ | --------- | --------- | -------- | --------- | ----------- |
    | 406296 | Limoges   | Limoges   | 45.8344  | 1.26167   | wikimain    |
    | 406297 | Limages   | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406298 | Llemotges | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406299 | Limoĝo    | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406300 | Limòtges  | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    
  This script generates an equal number of positive and negative pairs from a list of toponyms. Positive candidates are derived from WikiGazetteer alternative names. We generate two types of positive/negative pairs: trivial and challenging (see section 4.3.2 in the [arxiv paper]**(ADD link to paper)** for more details). The **output** is a txt file with positive and negative toponym pairs, with three columns (without header): source toponym, target toponym, and True/False depending on whether they are alternate names of the same entity or not. Each row corresponds to a toponym pair (see table below).

    | Toponym | Altname | Matching |
    | ---------- | ------------- | ----- |
    | Orșova	 | Hrușova       | False |
    | Orșova	 | Hârșova       | False |
    | Orșova	 | Orsova        | True  |
    | Orșova	 | Oršava        | True  |
    | Criuleni	 | Tiuleni       | False |
    | Criuleni	 | Ciuciuleni    | False |
    | Criuleni	 | Kriulen’      | True  |
    | Criuleni	 | Kriuleni      | True  |
    | Chirivella | Chirivel      | False |
    | Chirivella | Xirivella     | True  |

## OCR dataset

Contents:
* [`extract_ocr_alignments.ipynb`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/toponym_matching_datasets/ocr/extract_ocr_alignments.ipynb): Following the procedure described in [Van Strien et al [2019](https://www.staff.universiteitleiden.nl/binaries/content/assets/governance-and-global-affairs/isga/artidigh_2020_7_cr.pdf), we aligned OCR'd texts with their human-corrected counterpart at the token level. The `extract_ocr_alignments.ipynb` notebook takes the output of [this notebook](https://github.com/Living-with-machines/lwm_ARTIDIGH_2020_OCR_impact_downstream_NLP_tasks/blob/master/aligning_trove.ipynb) (a pickle file called `aligned_df_with_spacy.pkl`, assumed to be stored in `processing/resources/`) as input and returns a two-column tsv file, where the first column corresponds to the token in the OCR text and the second column to its aligned human correction:

    | OCR token     | Human token  |
    | ------------- | ------------ |
    | Canbeira      | Canberra     |
    | Canberia      | Canberra     |
    | Kindeiparten  | Kindergarten |
    | lissington    | Essington    |
    | Canberia      | Canberra     |
    | Wnkehuist     | Wakehurst    |
    
    :warning: **Note:** You can skip this step and download the resulting `ocrTokens.tsv` file [from here](https://zenodo.org/record/4034819) instead. Store it in `toponym_matching/resources/`.

* `processing/toponym_matching_datasets/ocr/create_dataset.ipynb`: This notebook generates a dataset of positive of negative pairs based on OCR'd tokens and their corresponding human corrections. It takes `ocrTokens.tsv` as input, which contains aligned OCR'd tokens aligned to their human correction. In this notebook, for each human-corrected token, we consider all its observed OCR'd variations in the dataset as positive pairings. We then capture the most observed OCR transformations in the dataset, and artificially build negative pairs by introducing unobserved random transformations for characters in the human-corrected string. We build as many negative pairs as positive pairs exist for a human-corrected string (see section 4.3.3 in the [arxiv paper]**(ADD link to paper)** for more details). **Output:** `ocr_posneg.tsv`, a dataset of positive and negative token pairs, the first column corresponding to the correct spelling, the second column to the OCR variation, and the third column the whether the matching is true or not. See some examples in the following table:

    | Correct spelling | OCR spelling     | Matching         |
    | ---------------- | ---------------- | ---------------- |
    | Zurich           | Zunch            | TRUE             |
    | Zurich           | Zurv'            | FALSE            |
    | Zurich           | Zmich            | TRUE             |
    | Zurich           | ZuTuich          | FALSE            |
    | Zurich           | Zuiich           | TRUE             |
    | Zurich           | ZurMT            | FALSE            |
    | Zurich           | 7urich           | TRUE             |
    | Zurich           | _«urich          | FALSE            |
    | Zurich           | Zuilch           | TRUE             |
    | Zurich           | Zuæch            | FALSE            |

## Santos

In our experiments, we also use an existing resource created by [Santos et al. (2017)](https://eprints.lancs.ac.uk/id/eprint/89481/1/Manusc_Combining_Multiple_String_Similarity_Metrics_for_Effective_Toponym_Matching.pdf), which you will be able to download from [here](https://github.com/ruipds/Toponym-Matching/tree/master/dataset). Store it in `processing/toponym_matching_datasets/santos/`
   
# Normalize and split datasets

* [`split_normalize_datasets.py`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/toponym_matching_datasets/split_normalize_datasets.py): This script normalizes the resulting datasets (we remove pairs if one of the elements was an empty string, and remove duplicates (including reverse duplicates such as `Florence, Firenze, True` and `Firenze, Florence, True`), and we remove, for each true pair, a corresponding false pair, and vice versa.) and separates the resulting datasets into two: (1) trainval (90% of the data, used for training and validation), and (2) test (10% of the data, used for testing). Both are balanced in terms of number of matching and non-matching pairs. Run it at the end, after having created the different datasets. It takes a list of tuples as input (line 55), where each tuple is a different toponym matching dataset. Tuples consist of three parts:
  * Output name of the normalized and split dataset.
  * Path of the input dataset.
  * Alphabet of the dataset, which at the moment can be:
    * greek: the dataset will only consist of toponyms containing at least one greek character.
    * latin: the dataset will only consist of toponyms containing at least one latin character.
    * "" (empty): the dataset does not filter toponyms by alphabet.
