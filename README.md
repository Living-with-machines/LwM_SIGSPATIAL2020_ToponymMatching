# A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching

This repository provides underlying code and materials for the paper 'A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching'.

## Table of contents

## Installation

## Data directory and structure

In our code, we assume the following directory structure:

```bash
LwM_SIGSPATIAL2020_ToponymMatching/
├── datasets
│   ├── candidate_mentions_sets
│   ├── candidate_ranking_datasets
│   ├── gazetteers
│   ├── query_mentions_sets
│   └── toponym_matching_datasets
├── experiments
│   ├── inputs
│   │   ├── characters_v001.vocab
│   │   └── dataset-string-similarity_test.txt
│   ├── levdam_results
│   ├── mapped_results
│   ├── models
│   └── ranker_results
└── processing
    ├── candidate_ranking_datasets
    ├── candselection
    ├── gazetteers
    ├── toponym_matching_datasets
    └── resources
```

Description of main directories:
* `processing/`: contains code for preparing or generating the different datasets.
* `datasets/`: contains datasets used in the experiments, resulting from running the `processing/` codes.
* `experiments/`: contains the experiment codes and generated files.

The `experiments/` folder contains two notebooks that replicate the experiments in the paper ([Toponym_Matching_Experiments](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/experiments/Toponym_Matching_Experiments.ipynb) contains the experiments summarized in table XXX, and [Candidate Ranking Experiments](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/experiments/Candidate_Ranking_Experiments.ipynb) contains the experiments summarized in table XXX). Make sure you have gone through the steps described in the `processing` README file and that you have all data needed to run the experiments.

## Citation

If you use or adapt this code in your paper, please cite:

```
Coll Ardanuy, M., Hosseini, K., McDonough, K., Krause, A., van Strien, D. and Nanni, F. (2020): A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching, SIGSPATIAL: Poster Paper.
```

and in BibTex:
```
@inproceedings{ardanuy2020geocandidate,
  title={DeezyMatch: A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching},
  author={Coll Ardanuy, Mariona and Hosseini, Kasra and McDonough, Katherine and Krause, Amrey and van Strien, Daniel and Nanni, Federico},
  booktitle={SIGSPATIAL: Poster Paper},
  year={2020}
}
```

A longer version of the article in available on arXiv:

```
Coll Ardanuy, M., Hosseini, K., McDonough, K., Krause, A., van Strien, D. and Nanni, F. (2020): A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching, arxiv:xxxx.xxxxx.
```

and in BibTex:
```
@inproceedings{ardanuy2020geocandidate,
  title={DeezyMatch: A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching},
  author={Coll Ardanuy, Mariona and Hosseini, Kasra and McDonough, Katherine and Krause, Amrey and van Strien, Daniel and Nanni, Federico},
  booktitle={arxiv:xxxx.xxxxx},
  year={2020}
}
```

## Future work and contributing

The authors of the paper plan to continue development of the code and experiments. We welcome pull requests for improvements and issues for any errors you encounter.

## Get in touch

Contacts of the corresponding authors:
* Mariona Coll Ardanuy, mcollardanuy[at]turing.ac.uk
* Kasra Hosseini, khosseinizad[at]turing.ac.uk
* Federico Nanni, fnanni[at]turing.ac.uk

## Acknowledgements

Work for this paper was produced as part of [Living with Machines](http://livingwithmachines.ac.uk/). This project, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London. This work was also supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1. Newspaper data was kindly shared by [Findmypast](https://www.findmypast.co.uk/).

## License

This work is licensed under a xxxxx license.