import pandas as pd
import argparse
from datetime import datetime
import csv
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter metadata filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter replacement filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column in metadata where string should be replaced: ')

metadata = pd.read_csv(filename, dtype=object)
find_replace = pd.read_csv(filename2, dtype=object)
old_column = 'old_'+column_name
metadata[old_column] = metadata[column_name]

for index, row in find_replace.iterrows():
    old_string = row['old_string']
    new_string = row['new_string']
    if pd.notnull(old_string):
        print(index, new_string)
        metadata[column_name] = metadata[column_name].str.replace(old_string, new_string, regex=False)

comparison_column = np.where(metadata[old_column] == metadata[column_name], False, True)
metadata['replacement'] = comparison_column


# Create CSV for new DataFrame.
filename = filename[:-4]
dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
metadata.to_csv('wReplacements_'+filename+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)

