"""Joins strings from numerous columns into a new column."""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename, header=0)
print(df.columns)

columnsToCombine = ['column1', 'column2']


def combine_by_row(row):
    all_items = []
    for column in columnsToCombine:
        if pd.notnull(row[column]):
            for value in str(row[column]).split('|'):
                all_items.append(value)
    all_items = list(set(all_items))
    all_items = '|'.join(all_items)
    return all_items


df['newColumn'] = df.apply(lambda row: combine_by_row(row), axis=1)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
new_filename = filename+'_mergedColumn_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
