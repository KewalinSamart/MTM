# script to preprocess inputs for MTM model
# created date: 04/27/24
# Kewalin Samart

import pandas as pd
import numpy as np

# read in sample_attributes.txt containing metadata for the subject-tissue pairs in the expression matrix
# we need to make sure that row names are subject-tissue pairs 
# with two attribute columns including tissue type "SMTSD" and subject ids "Subject_id"
metadata = pd.read_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/sample_attributes.txt",sep="\t")
print(metadata.columns)
# save tissue types
metadata['SMTSD'].to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/MTM_tissue_types.txt",sep="\t",header=False,index=False,index_label=None)

print(metadata.head)
sample_ids = metadata['SUBJID_tissue'].to_list()
#metadata_fmfixed = metadata.set_index('Subject_id')
metadata = metadata[['SUBJID_tissue','SMTSD','Subject_id']]
metadata.to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/MTM_sample_attrs.txt",sep="\t",index=False)

# save subject ids
metadata['Subject_id'].to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/MTM_subj_ids.txt",sep="\t",header=False,index=False)

# read in gene ids 
gene_df = pd.read_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/genes_matv8.txt",sep="\t",names=["geneids"])
genes = gene_df['geneids'].to_list()

# save sample data for testing the training 
ex_metadata = metadata.head(5000)
ex_metadata.to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/ex_MTM_sample_attrs.txt",sep="\t",header=True, index=False)
ex_subjids = metadata['Subject_id'].head(5000)
ex_subjids.to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/ex_MTM_subj_ids.txt",sep="\t",header=False,index=False)

'''
# we need filtered data here; so I am using the processed data by averaged data by sugject-tissue pairs
# read in avg_subjtissue_matv8.npy and convert npy to txt
# where rows: subject-tissue pairs, columns: genes
expdata_matrix = np.load("/Users/kewalinsamart/Documents/GitHub/MTM/data/avg_subjtissue_matv8.npy")
print(expdata_matrix.shape)
expdata_matrix_df = pd.DataFrame(data=expdata_matrix,
                                 index=sample_ids,
                                 columns=genes)
print(expdata_matrix_df.head)
expdata_matrix_df.to_csv("/Users/kewalinsamart/Documents/GitHub/MTM/data/MTM_expdata.txt",sep="\t",columns=genes)
'''