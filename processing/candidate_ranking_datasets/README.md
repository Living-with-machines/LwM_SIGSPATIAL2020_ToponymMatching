# Preparing datasets for external evaluation

This notebook prepares the datasets that are going to be used for external evaluation. Each dataset is stored into a dataframe. Some columns are common to all the dataframes, others are specific for a particular dataset. Columns present in all dataframes are:
- `source` (url or identifier of the document)
- `text` (full text of the document)
- `toponym` (each toponym as it appears in the text)
- `startCh` (start character of the toponym in the text)
- `endCh` (end character of the toponym in the text)
- `lat` (latitude of the resolved location)
- `lon` (longitude of the resolved location)
- `reference` (whether the main reference is Wikipedia identifier or coordinates. If the reference is Wikipedia, we've in any case derived its coordinates whenever possible)

## Obtaining the datasets

Download the following datasets and store them in the `datasets` folder:
- [x] [The War of the Rebellion dataset](https://github.com/utcompling/WarOfTheRebellion/archive/master.zip) (unzip it)
- [x] [La Argentina Manuscrita](https://recogito.pelagios.org/document/wzqxhk0h3vpikm/downloads) (Download the .csv file and rename it as `argentina_manuscrita.csv`)

Finally, we also created our own annotated dataset, which you can download from [here](https://zenodo.org/record/4034819) and store it in `datasets/candidate_ranking_datasets/`.
