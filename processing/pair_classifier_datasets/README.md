# Generating datasets for toponym matching evaluation

This folder contains the code and instructions to create the datasets used for evaluation of DeezyMatch pair classifier component (`WikiGaz` and `OCR dataset`). The resulting datasets can be found ***[ADD LINK]***. Read the instructions below to create them from scratch.

In our experiments, we also use an existing resource created by [Santos et al. (2017)](https://eprints.lancs.ac.uk/id/eprint/89481/1/Manusc_Combining_Multiple_String_Similarity_Metrics_for_Effective_Toponym_Matching.pdf), which you will be able to download from [here](https://github.com/ruipds/Toponym-Matching/tree/master/dataset). 

[**To add later** The `standardize_datasets` notebook separates the resulting datasets into two: (1) trainval (90% of the data, used for training and validation), and (2) test (10% of the data, used for testing). Both are balanced in terms of number of matching and non-matching pairs. Run it at the end, after having created the different datasets following the instructions below.]

## WikiGaz

Contents:
* `pair_classifier_datasets/wikigaz/process_wikigaz.ipynb`: WikiGazetteer is a gazetteer based on Wikipedia and enriched with Geonames data. To build a WikiGazetteer (into a MySQL database) for a specific Wikipedia language and version, follow [these instructions](https://github.com/Living-with-machines/lwm_GIR19_resolving_places/tree/master/gazetteer_construction). This notebook takes the relevant fields in the WikiGazetteer MySQL database and creates a more manageable pickle file. **Output:** A dataframe for the selected WikiGazetteer version, with one row per toponym and location, with the following columns: `index`, `name`, `wikititle`, `latitude`, `longitude`, `source`. You can skip this step and instead download the pickle files for the English, Spanish, and Greek WikiGazetteer from [here](https://thealanturininstitute-my.sharepoint.com/:f:/g/personal/mcollardanuy_turing_ac_uk/El5Bw5rXCGxEkhKYUbd9cqABlSJmVULkLfpQMPcFzvVaDQ?e=ZukmYP). See example:

    |        | name      | wikititle | latitude | longitude | source      |
    | ------ | --------- | --------- | -------- | --------- | ----------- |
    | 406296 | Limoges   | Limoges   | 45.8344  | 1.26167   | wikimain    |
    | 406297 | Limages   | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406298 | Llemotges | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406299 | Limoĝo    | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406300 | Limòtges  | Limoges   | 45.8344  | 1.26167   | geonamesalt |

* `pair_classifier_datasets/wikigaz/generate_wikigaz_comb.py`: This script generates an equal number of positive and negative pairs from a list of toponyms. Positive candidates are derived from WikiGazetteer alternative names. We generate two types of positive/negative pairs: trivial and challenging. The **output** is a txt file with positive and negative toponym pairs, with three columns (without header): source toponym, target toponym, and True/False depending on whether they are alternate names of the same entity. Each row corresponds to a toponym pair (see table below).

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

[**To add later:** Following the procedure described in [Van Strien et al [2019](https://www.staff.universiteitleiden.nl/binaries/content/assets/governance-and-global-affairs/isga/artidigh_2020_7_cr.pdf), we aligned OCR'd texts with their human-corrected counterpart at the token level. In the `ocrdataset/extract_ocr_alignments.ipynb` notebook, we identify tokens recognized as being part of named entities in the human-corrected text. **Output:** a two-column tsv file, in which the first column corresponds to the token in the OCR text and the second column to the human-corrected aligned token]

The [ocrTokens.tsv file](https://thealanturininstitute-my.sharepoint.com/:u:/g/personal/mcollardanuy_turing_ac_uk/EQjwVXAFawBPrHiPkwysjlUBVQ9_B5EvCiyoI85yvTiOoQ?e=wbh3eV) contains aligned OCR'd texts with their human-corrected counterpart at the token level, the first column corresponds to the token in the OCR text and the second column to the human-corrected aligned token:

    | OCR token     | Human token  |
    | ------------- | ------------ |
    | Canbeira      | Canberra     |
    | Canberia      | Canberra     |
    | Kindeiparten  | Kindergarten |
    | lissington    | Essington    |
    | Canberia      | Canberra     |
    | Wnkehuist     | Wakehurst    |

* In `ocrdataset/create_dataset.ipynb`, we create a dataset that has similar characteristics to Santos2018 and WikiGaz: for each human-corrected token, we consider all its observed OCR'd variations in the dataset as positive pairings. We then capture the most observed OCR transformations in the dataset, and artificially build negative pairs by introducing weighted random transformations for characters in the human-corrected string. We build as many negative pairs as positive pairs exist for a human-corrected string. **Output:** `ocr_posneg.tsv`, a dataset of 173,116 token pairs, the first column corresponding to the correct spelling, the second column to the OCR variation, and the third column the whether the matching is true or not. See some examples in table \ref{tab:ocrdataset}).

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