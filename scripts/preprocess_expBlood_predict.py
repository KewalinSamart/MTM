# script to preprocess input Blood expression matrix for prediction
# filtering by test subjects
# created date: 04/29/24
# Kewalin Samart

import pandas as pd 
import numpy as np 

# we need filtered data here; so I am using the processed data by averaged data by sugject-tissue pairs
# read in normGTExv8_expdata_Blood.npy and convert npy to txt
# where rows: subject-tissue pairs, columns: genes
blood_expdata_matrix = np.load("/data/scratch/samartk/MTM/scripts/input_dir/normGTExv8_expdata_Blood.npy")
print(blood_expdata_matrix.shape)

# get sample ids (subject-tissue pairs)
blood_sample_ids = pd.read_csv("/data/scratch/samartk/MTM/scripts/input_dir/SUBJtissue_index_Blood.txt",sep="\t")["SUBJID_tissue"]

# get genes 
# read in gene ids 
gene_df = pd.read_csv("/data/scratch/samartk/MTM/data/genes_matv8.txt",sep="\t",names=["geneids"])
genes = gene_df['geneids'].to_list()

blood_expdata_matrix_df = pd.DataFrame(data=blood_expdata_matrix,
                                 index=blood_sample_ids,
                                 columns=genes)

# read in test blood subject-tissue pairs
test_blood_sampleids = pd.read_csv("/data/scratch/samartk/MTM/scripts/input_dir/test_SUBJtissue_index_Blood.txt",sep="\t")["SUBJID_tissue"]
testblood_expdata_matrix_df = blood_expdata_matrix_df[blood_expdata_matrix_df.index.isin(test_blood_sampleids)]

print(testblood_expdata_matrix_df.head)
testblood_expdata_matrix_df.to_csv("/data/scratch/samartk/MTM/data/MTM_expdataBlood_predict.txt",sep="\t",columns=genes)
testblood_expdata_matrix_df.to_csv("/data/scratch/samartk/MTM/scripts/input_dir/MTM_expdataBlood_predict.txt",sep="\t",columns=genes)

