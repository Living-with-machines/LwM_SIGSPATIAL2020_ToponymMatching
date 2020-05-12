# Generating datasets for toponym matching evaluation

This folder contains the code and instructions to create the datasets used for intrinsic evaluation of toponym matching. 

## WikiGaz

Contents:
* `wikigaz/process_wikigaz.ipynb`: WikiGazetteer is a gazetteer based on Wikipedia and enriched with Geonames data. To build a WikiGazetteer (into a MySQL database) for a specific Wikipedia language and version follow [these instructions](https://github.com/Living-with-machines/lwm_GIR19_resolving_places/tree/master/gazetteer_construction). This notebook takes the relevant fields in the WikiGazetteer MySQL database and creates a more manageable pickle file. **Output:** A dataframe for the selected WikiGazetteer version, with one row per toponym and location, with the following columns: `index`, `name`, `wikititle`, `latitude`, `longitude`, `source`. See example:

    |        | name      | wikititle | latitude | longitude | source      |
    | ------ | --------- | --------- | -------- | --------- | ----------- |
    | 406296 | Limoges   | Limoges   | 45.8344  | 1.26167   | wikimain    |
    | 406297 | Limages   | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406298 | Llemotges | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406299 | Limoĝo    | Limoges   | 45.8344  | 1.26167   | geonamesalt |
    | 406300 | Limòtges  | Limoges   | 45.8344  | 1.26167   | geonamesalt |

* `wikigaz/generate_wikigaz_dataset.ipynb` (python script: `wikigaz/generate_dataset.py`): This notebook generates an equal number of positive and negative pairs from a list of toponyms. Positive candidates are derived from WikiGazetteer alternative names. To generate the negative candidates given a place name, we first divide it in ngrams, then retrieve all altnames that contain one of the ngrams and finally rank them using Levensthein distance. We filter out altnames that can correspond to locations within 50 km distance from the source place name. **Output:** A txt file with positive and negative toponym pairs, with three columns (without header): source toponym, target toponym, and True/False depending on whether they are alternate names of the same entity. Each row corresponds to a toponym pair:


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
