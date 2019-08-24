import pandas
import csv
import numpy as np
import re

codebook = pandas.read_csv("codebook.csv", header=None)
valid_trs = pandas.read_csv("valid_trs.csv", names=["Name", "ID"])
abundance = pandas.read_csv("./../abundance/abundance.tsv", sep='\t')

size = codebook.shape
codebook = codebook[4:]

for (i, name) in enumerate(codebook[0]):
    if re.match(r"(?:b|B)lank", name) is not None:
        continue
    
    print(valid_trs[valid_trs['Name'].str.match('name')])
    



print(codebook)
print(valid_trs)
print(abundance)