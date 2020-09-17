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
- [x] [GeoVirus](https://github.com/milangritta/Pragmatic-Guide-to-Geoparsing-Evaluation/blob/master/data/Corpora/GeoVirus.xml)
- [x] [TR-News](https://github.com/milangritta/Pragmatic-Guide-to-Geoparsing-Evaluation/blob/master/data/Corpora/TR-News.xml)
- [x] [Local Global Lexicon](https://github.com/milangritta/Pragmatic-Guide-to-Geoparsing-Evaluation/blob/master/data/Corpora/lgl.xml)
- [x] [GeoWebNews](https://github.com/milangritta/Pragmatic-Guide-to-Geoparsing-Evaluation/blob/master/data/GWN.xml)
- [x] [La Argentina Manuscrita](https://recogito.pelagios.org/document/wzqxhk0h3vpikm/downloads) (Download the .csv file and rename it as `argentina_manuscrita.csv`)
- [x] [Pausanias: Periegesis](https://recogito.pelagios.org/document/35zv4zm4iqp4aw/downloads) (Download the .csv file and rename it as `pausanias_periegesis.csv`)

Finally, we also created our own annotated dataset, which will be available soon.
