from DeezyMatch import train as dm_train
from DeezyMatch import plot_log
from DeezyMatch import finetune as dm_finetune
from DeezyMatch import inference as dm_inference
from DeezyMatch import combine_vecs
from DeezyMatch import candidate_ranker

from pathlib import Path
import pandas as pd
import time

"""
Find candidates with DeezyMatch
"""
def find_deezymatch_candidates(gazetteer_name, candrank_dataset, deezymatch_model, lc=False):
    
    input_filename = "input_dfm"
    if lc:
        input_filename = "input_dfm_lc"
        
    # GENERATE AND COMBINE CANDIDATE VECTORS
    
    # generate vectors for candidates (specified in dataset_path) 
    # using a model stored at pretrained_model_path and pretrained_vocab_path 
    if not Path("./candidates/" + gazetteer_name + "_" + deezymatch_model + "/embeddings/").is_dir():
        start_time = time.time()
        dm_inference(input_file_path="./models/" + deezymatch_model + "/" + input_filename + ".yaml",
                     dataset_path="../datasets/candidate_mentions_sets/" + gazetteer_name + ".txt", 
                     pretrained_model_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".model", 
                     pretrained_vocab_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".vocab",
                     inference_mode="vect",
                     scenario="candidates/" + gazetteer_name + "_" + deezymatch_model)
        elapsed = time.time() - start_time
        print("Generate candidate vectors: %s" % elapsed)
    
    # combine vectors stored in the scenario in candidates/ and save them in combined/
    if not Path("./combined/" + gazetteer_name + "_" + deezymatch_model).is_dir():
        start_time = time.time()
        combine_vecs(rnn_passes=["fwd", "bwd"], 
                     input_scenario="candidates/" + gazetteer_name + "_" + deezymatch_model, 
                     output_scenario="combined/" + gazetteer_name + "_" + deezymatch_model, 
                     print_every=100)
        elapsed = time.time() - start_time
        print("Combine candidate vectors: %s" % elapsed)
        
    # GENERATE AND COMBINE QUERY VECTORS
    
    # create set of query mentions:
    if not Path("../datasets/query_mentions_sets/" + candrank_dataset + ".txt").is_file():
        with open("../datasets/query_mentions_sets/" + candrank_dataset + ".txt", "w") as fw:
            for i in set(pd.read_pickle("../datasets/candidate_ranking_datasets/" + candrank_dataset + ".pkl").toponym.to_list()):
                if not any(char.islower() for char in i):
                    i = i.title()
                fw.write(i + "\t0\tfalse\n") 

    # generate vectors for queries (specified in dataset_path) 
    # using a model stored at pretrained_model_path and pretrained_vocab_path 
    if not Path("./queries/" + candrank_dataset + "_" + deezymatch_model + "/embeddings/").is_dir():
        start_time = time.time()
        dm_inference(input_file_path="./models/" + deezymatch_model + "/" + input_filename + ".yaml",
                     dataset_path="../datasets/query_mentions_sets/" + candrank_dataset + ".txt", 
                     pretrained_model_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".model", 
                     pretrained_vocab_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".vocab",
                     inference_mode="vect",
                     scenario="queries/" + candrank_dataset + "_" + deezymatch_model)
        elapsed = time.time() - start_time
        print("Generate query vectors: %s" % elapsed)

    # combine vectors stored in the scenario in queries/ and save them in combined/
    if not Path("./combined/" + candrank_dataset + "_" + deezymatch_model).is_dir():
        start_time = time.time()
        combine_vecs(rnn_passes=["fwd", "bwd"], 
                     input_scenario="queries/" + candrank_dataset + "_" + deezymatch_model, 
                     output_scenario="combined/" + candrank_dataset + "_" + deezymatch_model, 
                     print_every=100)
        elapsed = time.time() - start_time
        print("Combine query vectors: %s" % elapsed)

    # Select candidates based on L2-norm distance (aka faiss distance):
    # find candidates from candidate_scenario 
    # for queries specified in query_scenario
    if not Path("ranker_results/" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model + ".pkl").is_file():
        start_time = time.time()
        candidates_pd = \
            candidate_ranker(query_scenario="./combined/" + candrank_dataset + "_" + deezymatch_model,
                             candidate_scenario="./combined/" + gazetteer_name + "_" + deezymatch_model, 
                             ranking_metric="faiss", 
                             selection_threshold=100., 
                             num_candidates=20, 
                             search_size=20, 
                             output_path="ranker_results/" + candrank_dataset + "_" + gazetteer_name + "_" + deezymatch_model, 
                             pretrained_model_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".model", 
                             pretrained_vocab_path="./models/" + deezymatch_model + "/" + deezymatch_model + ".vocab")
        elapsed = time.time() - start_time
        print("Rank candidates: %s" % elapsed)