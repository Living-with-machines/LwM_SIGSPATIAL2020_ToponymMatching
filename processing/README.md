# Processing and obtaining data

This file contains the instructions to obtain, process, and generate the data that is used in the experiments.

## Table of contents

## Data directory and structure

In our code, we assume the following directory structure:

```bash
processing
├── candidate_ranking_datasets
├── gazetteers
├── toponym_matching_datasets
└── resources
```

Description of main directories, in order of execution:
* [gazetteers](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master/processing/gazetteers): code to obtain or generate gazetteers that will be used to generate toponym matching dataset and to evaluate candidate ranking. Run them in the following order:
  1. [`generate_wikigazetteers.ipynb`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/gazetteers/generate_wikigazetteers.ipynb)
  2. [`prepare_gazetteers.ipynb`](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/master/processing/gazetteers/prepare_gazetteers.ipynb)
* [toponym_matching_datasets](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master/processing/toponym_matching_datasets): code and instructions to create and process the datasets used for evaluation of toponym matching (`WG:en`, `WG:es`, `WG:el`, `OCR dataset`, and `santos`).
* [candidate_ranking_datasets](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master/processing/candidate_ranking_datasets): code and instructions to obtain or prepare the datasets that are going to be used for geographical candidate selection evaluation.
* `resources`: external resources needed to obtain, process, or generate a dataset.
