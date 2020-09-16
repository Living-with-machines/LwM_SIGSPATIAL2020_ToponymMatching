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
* `gazetteers`: code to obtain or generate gazetteers that will be used to generate toponym matching dataset and to evaluate candidate ranking. Run `generate_wikigazetteers.ipynb` first, and then `prepare_gazetteers.ipynb`.
* `toponym_matching_datasets`: code and [instructions](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/processing/toponym_matching_datasets/README.md) to create the new datasets used for evaluation of toponym matching (`WG:en`, `WG:es`, `WG:el` and `OCR dataset`).
* `candidate_ranking_datasets`: [code](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/processing/candidate_ranking_datasets/prepare_candrank_datasets.ipynb) and [instructions](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/processing/candidate_ranking_datasets/README.md) to obtain or prepare the datasets that are going to be used for geographical candidate selection evaluation.
* `resources`: external resources needed to obtain, process, or generate a dataset.