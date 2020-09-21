# A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching

This repository provides underlying code and materials for the paper `A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching`.

## Table of contents

* [Installation](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master#installation)
* [Data directory and structure](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#data-directory-and-structure)
* [Citation](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#citation)
* [Future work and contributing](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#future-work-and-contributing)
* [Get in touch](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#get-in-touch)
* [Acknowledgements](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#acknowledgements)
* [License](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/develop#license)

## Installation

Please follow the instructions on [the installation section of DeezyMatch](https://github.com/Living-with-machines/DeezyMatch#installation) to set up an environment and install all required packages to run DeezyMatch.

Once working Python and DeezyMatch environments are available, the following additional libraries need to be installed:

```bash
pip install pyxDamerauLevenshtein
pip install haversine
pip install pandarallel
pip install mysql-connector-python
pip install geopy
pip install python-Levenshtein
```

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

The `experiments/` folder contains two notebooks with the [experiments](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master/experiments) reported in the paper:
* [Toponym_Matching_Experiments.ipynb](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/develop/experiments/Toponym_Matching_Experiments.ipynb) has the experiments summarized in table 1.
* [Candidate_Ranking_Experiments.ipynb](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/blob/tm_experiments/experiments/Candidate_Ranking_Experiments.ipynb) has the experiments summarized in table 2. 

:warning: Make sure you have gone through the required `processing` steps (described [here](https://github.com/Living-with-machines/LwM_SIGSPATIAL2020_ToponymMatching/tree/master/processing)) and that you have all the data needed before you run the experiments.

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

A longer version of the article is available on arXiv:

```
Coll Ardanuy, M., Hosseini, K., McDonough, K., Krause, A., van Strien, D. and Nanni, F. (2020): A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching, arxiv:2009.08114.
```

and in BibTex:
```
@inproceedings{ardanuy2020geocandidate,
  title={DeezyMatch: A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching},
  author={Coll Ardanuy, Mariona and Hosseini, Kasra and McDonough, Katherine and Krause, Amrey and van Strien, Daniel and Nanni, Federico},
  booktitle={arxiv:2009.08114},
  year={2020}
}
```

## Future work and contributing

The authors of the paper plan to further develop the codes and extend the experiments. We welcome pull requests for improvements and issues if you encounter any errors.

## Get in touch

Contacts of the corresponding authors:
* Mariona Coll Ardanuy, mcollardanuy[at]turing.ac.uk
* Kasra Hosseini, khosseini[at]turing.ac.uk
* Federico Nanni, fnanni[at]turing.ac.uk

## Acknowledgements

Work for this paper was produced as part of [Living with Machines](http://livingwithmachines.ac.uk/). This project, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London. This work was also supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1. Newspaper data was kindly shared by [Findmypast](https://www.findmypast.co.uk/).

## License

- The source codes are licensed under MIT License Copyright (c) 2020 Living with Machines.
- The datasets hosted on [zenodo](https://zenodo.org/record/4034819) are licensed under CC-BY-4.0.
