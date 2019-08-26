import pandas
import csv
import numpy as np
import re

codebook = pandas.read_csv("codebook.csv", header=None)
valid_trs = pandas.read_csv("valid_trs.csv", names=["Name", "ID"])
abundance = pandas.read_csv("abundance.tsv", sep='\t')

size = codebook.shape
codebook = codebook[4:]

count = 0

for (i, name) in enumerate(codebook[0]):
    if re.match(r"(?:b|B)lank", name) is not None:
        continue
    
    # if count < 10:
    #     count += 1
    # else:
    #     break
    gene_transcripts = valid_trs[valid_trs['Name'] == name]
    
    if len(gene_transcripts) == 0:
        print(("-------------------------------------------NO VALID TRS FOR " + name + '\n')*5)
        continue

    gene_transcripts_ids = gene_transcripts['ID'].str.slice(0,15,1)
    # print(gene_transcripts_ids)

    transcript_abundance = []
    transcript_ids_list = []
    print(name)
    for id in gene_transcripts_ids:
        if len(abundance[abundance['target_id'].str.match(id)]['tpm']) < 1:
            print(("----------------------------could not find id " + id + '\n')*3)
            continue
        transcript_abundance.append(float(abundance[abundance['target_id'].str.match(id)]['tpm']))
        transcript_ids_list.append(id)
    
    print(transcript_abundance)
    idx = int(np.argmax(transcript_abundance))
    print('go with position ' + str(idx))
    print(transcript_ids_list[idx])
    print("______________________________")



# print(codebook)
# print(valid_trs)
# print(abundance)