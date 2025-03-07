"""Finds identifiers that only appear once in a CSV's identifier column. Creates a new CSV containing only the rows with non-repeated identifiers.
"""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

df = pd.read_csv(filename, header=0)

counts = df[identifier].value_counts()
print(counts.head)

item_list = []
for index, row in counts.items():
    if row == 1:
        item_list.append(index)
items = []
for index, row in df.iterrows():
    print(row)
    uri = row[identifier]
    if uri in item_list:
        items.append(row)


frame = pd.DataFrame.from_records(items)
print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
new_filename = 'uniqueIdsFrom'+filename+'_'+dt+'.csv'
frame.to_csv(new_filename, quoting=csv.QUOTE_ALL)
