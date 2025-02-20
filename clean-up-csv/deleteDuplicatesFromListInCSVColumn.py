"""Deletes any duplicate values from a list in a specific CSV column."""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to remove duplicates: ')

df = pd.read_csv(filename, header=0)

item_list = []
for index, row in df.iterrows():
    row = row.copy()
    to_fix = row.get(column_name)
    if pd.notna(to_fix):
        to_fix = to_fix.split('|')
        row['original_total'] = len(to_fix)
        fixed = sorted(list(set(to_fix)))
        row['new_total'] = len(fixed)
        fixed = '|'.join(fixed)
        row['no_duplicates'] = fixed
    item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_new = pd.DataFrame.from_records(item_list)
new_filename = 'noDuplicatesInList'+filename+'_'+dt+'.csv'
df_new.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)



