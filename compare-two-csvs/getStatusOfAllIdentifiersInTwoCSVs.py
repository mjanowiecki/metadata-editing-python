"""Creates a CSV with a list of all identifiers from both CSVs and records if the identifier
 is in both CSVs, only first CSV, or only second CSV."""

import pandas as pd
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')


df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

unique_1 = df_1[identifier].unique()
unique_2 = df_2[identifier].unique()
unique_1 = set(unique_1)
unique_2 = set(unique_2)
sheet_1 = unique_1 - unique_2
print(sheet_1)
sheet_2 = unique_2 - unique_1
print(sheet_2)
both_sheets = unique_1.intersection(unique_2)

frame = pd.merge(df_1, df_2, how='outer', on=[identifier],
                 suffixes=('_1', '_2'))

frame.reset_index(inplace=True)

all_items = []
for index, row in frame.iterrows():
    id_value = row[identifier]
    if id_value in sheet_1:
        row['where'] = 'sheet1 only'
    elif id_value in sheet_2:
        row['where'] = 'sheet2 only'
    elif id_value in both_sheets:
        row['where'] = 'both sheets'
    else:
        row['where'] = 'error'
    all_items.append(row)


new_df = pd.DataFrame.from_records(all_items)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'identifierStatus_'+dt+'.csv'
new_df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
