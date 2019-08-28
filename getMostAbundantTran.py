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

final_out = []

for (i, name) in enumerate(codebook[0]):
    if re.match(r"(?:b|B)lank", name) is not None:
        continue
    count += 1

    gene_transcripts = valid_trs[valid_trs['Name'] == name]
    
    if len(gene_transcripts) == 0:
        print(("-------------------------------------------NO VALID TRS FOR " + name + '\n')*5)
        final_out.append([name, '***INVALID***'])
        continue

    gene_transcripts_ids = gene_transcripts['ID'].str.slice(0,15,1)
    # print(gene_transcripts_ids)

    transcript_abundance = []
    transcript_ids_list = []
    print(name)
    for id in gene_transcripts_ids:
        print(id)
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


    for id_no_version in transcript_ids_list:
        if not id_no_version == transcript_ids_list[idx]:
            continue
        dobject = valid_trs[valid_trs['ID'].str.match(id_no_version)]['ID']
        for unwrapped_id in dobject:
            final_out.append([name, unwrapped_id])


print(final_out)
# pandas.DataFrame(final_out).to_csv()

with open('selected_transcripts.csv', 'w', newline='') as outFile:
    writer = csv.writer(outFile)
    writer.writerows(final_out)

outFile.close()

print(count)
# print(codebook)
# print(valid_trs)
# print(abundance)